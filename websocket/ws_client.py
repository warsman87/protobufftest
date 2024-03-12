import asyncio
import websockets
import message_pb2 as message_pb2

async def send_message():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        a =  message_pb2.MyMessage()
        a.content = "Hallo"
        await websocket.send(a.SerializeToString())
        
        response = await websocket.recv()
        my_response = message_pb2.MyMessage()
        my_response.ParseFromString(response)
        print(f"Received echo: {my_response.content}")

asyncio.run(send_message())