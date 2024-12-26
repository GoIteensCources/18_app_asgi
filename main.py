import asyncio
from fastapi import FastAPI, WebSocket, Request
from fastapi.templating import Jinja2Templates
from starlette.websockets import WebSocketDisconnect

app = FastAPI(docs_url="/docs")
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def get_chat(request: Request):
    return templates.TemplateResponse(
        request=request, name="websocket_client.html"
    )


@app.get("/hello")
async def hello_rout(user: str = "Anonimus"):
    await asyncio.sleep(0.1)
    return f"Hello, {user}!"


# Життєвий Цикл WebSocket-З'єднання:
@app.websocket("/ws/base")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()  # Ініціалізація (Handshake)
    print("Connect raise")
    try:
        while True:  # Трансфер Даних
            data = await websocket.receive_text()
            print(data)
            await websocket.send_text(f" Server get message: {data}")

    except WebSocketDisconnect:  # Управління З'єднанням
        print("Client raise disconnect")
    except Exception as e:
        print(f"Critical Error: {e}")

    finally:  # Закриття З'єднання
        if not websocket.client_state.DISCONNECTED:
            await websocket.close()


if __name__ == "__main__":
    from server_run import uvicorn_run, hypercorn_run

    # hypercorn_run(app)
    uvicorn_run()
