from typing import List
from fastapi import APIRouter

from models import Item, ItemIn
from databases import database, items

router = APIRouter(prefix="/items", tags=["Items"])

@router.post("/items/", response_model=Item)
async def create_item(item: ItemIn):
    query = items.insert().values(**item.dict())
    last_record_id = await database.execute(query)
    return {**item.dict(), "id": last_record_id}


@router.get("/items/", response_model=List[Item])
async def read_items():
    query = items.select()
    return await database.fetch_all(query)


@router.put("/items/{items_id}", response_model=Item)
async def update_item(item_id: int, new_item: ItemIn):
    query = items.update().where(items.c.id ==item_id).values(**new_item.dict())
    await database.execute(query)
    return {**new_item.dict(), "id": item_id}


@router.delete("/items/{items_id}")
async def delete_item(item_id: int):
    query = items.delete().where(items.c.id == item_id)
    await database.execute(query)
    return {'message': 'Item deleted'}
