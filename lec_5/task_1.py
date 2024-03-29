from fastapi import FastAPI

app = FastAPI()

#функции в FatAPI возвращают json-объект

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}") #в FastAPI параметры передаются в фигурных скобках
async def read_item(item_id: int, q: str = None): #все параметры, которые неявно передались в запрос после знака ?, также попадают в функцию и могут там отработать
    #к примеру, можно перейти по такому адресу http://127.0.0.1:8000/items/5?q=test
    return {"item_id": item_id, "q": q}

#выше был пример get-запроса. Следующий запрос - POST. Метод POST используется для отправки данных на сервер
@app.post("/items/")
async def create_item(item: Item):
    return item

#Метод PUT используется для обновления данных на сервере
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_id": item_id, "item": item}

#Метод DELETE используется для удаления данных на сервере
@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    return {"item_id": item_id}


