import asyncio
import message_pb2 as message_pb2

# Define an asynchronous function to send a message and receive a response
async def send_and_receive_message():
    # Open a connection to a server listening on IP address 127.0.0.1 and port 12345
    reader, writer = await asyncio.open_connection('127.0.0.1', 12345)

    # Create an instance of MyMessage
    my_message = message_pb2.MyMessage()
    my_message.content = "Hello, World!"
    print("Send:", my_message.content)

    # Write the serialized message to the socket
    writer.write(my_message.SerializeToString())

    # Wait until the write operation is finished
    await writer.drain()

    # Read the response from the server (up to 1024 bytes)
    data = await reader.read(1024)

    # Create a new instance of MyMessage for the response
    response_message = message_pb2.MyMessage()
    
    # Parse the response data into the MyMessage object
    response_message.ParseFromString(data)
    print("Received:", response_message.content)

    # Close the connection
    print("Close the connection")
    writer.close()
    # Wait until the connection is fully closed
    await writer.wait_closed()

# Run the send_and_receive_message function with asyncio.run, 
# which starts the event loop and runs the function
asyncio.run(send_and_receive_message())