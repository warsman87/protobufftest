import asyncio
import websockets
from message_pb2 import MyMessage

async def echo(websocket, path):
    async for message in websocket:
        my_message = MyMessage()
        my_message.ParseFromString(message)
        print(f"Received message: {my_message.content}")

        # Verarbeite die Nachricht oder führe andere asynchrone Operationen durch
        # Achten Sie auf die Syntaxkorrektur für die String-Zusammensetzung
        my_message.content = f"Echo: {my_message.content} zurück!"
        await websocket.send(my_message.SerializeToString())

async def main():
    async with websockets.serve(echo, "localhost", 8765):
        await asyncio.Future()  # Dies läuft für immer, bis der Server explizit gestoppt wird

# Starten des Servers mit asyncio.run()
if __name__ == "__main__":
    asyncio.run(main())
