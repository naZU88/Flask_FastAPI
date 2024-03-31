'''Создание моделей для взаимодействия с таблицей в БД'''

import datetime
from decimal import Decimal
from pydantic import BaseModel, Field


class UserIn(BaseModel):
    name: str = Field(max_length=32)
    surname: str = Field(max_length=32)
    email: str = Field(max_length=128)
    password: str = Field(min_length=8, max_length=32)

class User(BaseModel):
    id: int
    name: str = Field(max_length=32)
    surname: str = Field(max_length=32)
    email: str = Field(max_length=128)
    password: str = Field(min_length=8, max_length=32)

class OrderIn(BaseModel):
    user_id: int
    item_id: int
    date: datetime
    status: str = Field(max_length=32)

class Order(BaseModel):
    id: int
    user_id: int
    item_id: int
    date: datetime
    status: str = Field(max_length=32)


class ItemIn(BaseModel):
    name: str = Field(max_length=32)
    description: str = Field(max_length=300)
    price: Decimal

    
class Item(BaseModel):
    id: int
    name: str = Field(max_length=32)
    description: str = Field(max_length=300)
    price: Decimal
