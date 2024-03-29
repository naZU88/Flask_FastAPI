'''Валидация данных запроса и ответа'''
#FastAPI позволяет автоматически валидировать данные запроса и ответа с помощью модуля pydantic

from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

#по-сути мы создали валидатор, который проверяет переменные на значение и опциональность
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

# Этот код добавляет обработчики POST и PUT запросов, которые принимают объект
# Item и возвращают его же. Если данные не соответствуют описанию класса Item, то
# FastAPI вернет ошибку 422 с описанием ошибки.

@app.post("/items/")
async def create_item(item: Item):
    return item

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_id": item_id, "item": item}
