import asyncio
import websockets

async def handler(websocket, path):
    print("Client connected")
    try:
        # Step 1: Send initial greeting message
        await websocket.send("Hi, Let's be connected")
        print("Sent: Hi, Let's be connected")

        # Step 2: Receive agreement message from client
        message = await websocket.recv()
        print(f"Received: {message}")

        # Step 3: Check if the client agrees to connect
        if message == "Y":
            await websocket.send("Agreed")
            print("Sent: Agreed")

            # Step 4: Final confirmation message
            await websocket.send("Connection Established")
            print("Sent: Connection Established")
            # Now you can proceed with data sharing
            while True:
                data = await websocket.recv()
                print(f"Received data: {data}")
                # Sending data back to client (if needed)
                await websocket.send(f"Data received: {data}")
        else:
            print("Client disagreed to connect.")
    except websockets.ConnectionClosed:
        print("Connection closed")

async def main():
    async with websockets.serve(handler, "0.0.0.0", 5000):
        await asyncio.Future()  # run forever

asyncio.run(main())
