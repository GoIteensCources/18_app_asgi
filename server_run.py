

def uvicorn_run():
    import uvicorn
    uvicorn.run("main:app", reload=True, ssl_keyfile="key.pem", ssl_certfile="cert.pem")


def hypercorn_run(app):
    import asyncio
    from hypercorn.config import Config
    from hypercorn.asyncio import serve

    config = Config()
    config.bind = ["localhost:8000", "localhost:8001", "localhost:8003"]
    config.use_reloader = True
    asyncio.run(serve(app, config))
