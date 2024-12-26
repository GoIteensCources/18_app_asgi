# ASGI
ASGI (Asynchronous Server Gateway Interface) - явилося як розширення WSGI для підтримки асинхронної обробки, що відкриває можливості для ефективнішої роботи з веб-сокетами, довготривалими з'єднаннями та іншими асинхронними операціями.

## Uvicorn with HTTPS
```python
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from fastapi import FastAPI

app = FastAPI(docs_url="/docs")
app.add_middleware(HTTPSRedirectMiddleware)
```

Створення самопідписанного сертифікату:
```bash
openssl genpkey -algorithm RSA -out key.pem
openssl req -new -key key.pem -out csr.pem
openssl x509 -req -in csr.pem -signkey key.pem -out cert.pem
```
Запуск uvicorn з сертифікатами
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 443 --ssl-keyfile=key.pem --ssl-certfile=cert.pem
```