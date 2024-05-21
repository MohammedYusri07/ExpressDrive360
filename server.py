# server.py
import asyncio
import websockets

async def handler(websocket, path):
    # Step 1: Send initial connection request
    input("Press Enter to send connection request to ESP8266: ")
    await websocket.send("Hi, Let's be connected")
    print("Sent connection request to ESP8266")

    # Step 2: Wait for ESP8266 response
    response = await websocket.recv()
    print(f"Received response from ESP8266: {response}")

    if response == "Y":
        # Step 3: ESP8266 agreed, finalize connection
        input("Press Enter to finalize connection: ")
        await websocket.send("Connection Established")
        print("Connection Established")
    else:
        # Step 4: ESP8266 disagreed, terminate process
        print("ESP8266 declined the connection.")
        await websocket.send("No contact Established")

async def main():
    async with websockets.serve(handler, "0.0.0.0", 5000):
        await asyncio.Future()  # Run forever

asyncio.run(main())
