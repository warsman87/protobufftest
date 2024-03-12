import asyncio
import message_pb2 as message_pb2

# Define an asynchronous function to handle a client connection
async def handle_client(reader, writer):

    # Read data from the client (up to 1024 bytes)
    data = await reader.read(1024) 

    # Create an instance of MyMessage and parse the received data into it
    message = message_pb2.MyMessage()
    message.ParseFromString(data)
    
    # Get the client's address
    addr = writer.get_extra_info('peername')
    print(f"Received {message.content} from {addr}")

    # Create a response message and set its content
    response_message = message_pb2.MyMessage()
    response_message.content = "Message received: " + message.content

    # Write the serialized response message to the socket
    writer.write(response_message.SerializeToString())
    # Wait until the write operation is finished
    await writer.drain()

    # Close the connection
    print("Close the connection")
    writer.close()
    # Wait until the connection is fully closed
    await writer.wait_closed()

async def main():
    # Start a server that listens on IP address 127.0.0.1 and port 12345
    # and uses handle_client to handle connections
    server = await asyncio.start_server(
        handle_client, '127.0.0.1', 12345)

    # Get the server's address
    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')

    # Run the server until it is stopped
    async with server:
        await server.serve_forever()

# Run the main function
asyncio.run(main())