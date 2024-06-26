from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
import json
from src.offers import Parser

app = FastAPI()
parser = Parser.instance()


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = {'offers': parser.get_data()}
        # client_sent = await websocket.receive_text()
        # print(client_sent)
        print(f"data sent {len(data['offers'])}")
        await websocket.send_json(data)
