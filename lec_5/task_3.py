'''Форматирование ответов API'''

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.responses import JSONResponse
# FastAPI позволяет форматировать ответы API в различных форматах, например, в
# JSON или HTML. Для этого нужно использовать соответствующие функции модуля
# fastapi.responses.

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return "<h1>Hello World</h1>"

@app.get("/message")
async def read_message():
    message = {"message": "Hello World"}
    return JSONResponse(content=message, status_code=200)