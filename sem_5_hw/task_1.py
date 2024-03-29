# Необходимо создать API для управления списком задач. Каждая задача должна содержать заголовок и описание. Для каждой задачи должна 
# быть возможность указать статус (выполнена/не выполнена).

# API должен содержать следующие конечные точки:
# — GET /tasks — возвращает список всех задач.
# — GET /tasks/{id} — возвращает задачу с указанным идентификатором.
# — POST /tasks — добавляет новую задачу.
# — PUT /tasks/{id} — обновляет задачу с указанным идентификатором.
# — DELETE /tasks/{id} — удаляет задачу с указанным идентификатором.

# Для каждой конечной точки необходимо проводить валидацию данных запроса и ответа. Для этого использовать библиотеку Pydantic.

from fastapi import FastAPI, HTTPException
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()
tasks = []

class Task(BaseModel):
    task_id: int
    title: str
    description: Optional[str] = None
    status: str 

class TaskIn(BaseModel):
    title: str
    description: str
    status: str

@app.get('/tasks', response_model=list[Task])
async def get_tasks():
    return tasks

@app.get('/tasks/{id}', response_model=Task)
async def get_task(id):
    for task in tasks:
        if task.id == id:
            return task

@app.post('/tasks', response_model=Task)
async def add_task(new_task: TaskIn):
    new_task = Task(task_id=len(tasks)+1, title=new_task.title, description=new_task.description, status=new_task.status)
    tasks.append(new_task)
    return new_task

@app.put('/tasks/{id}', response_model=Task)
async def put_task(id, new_task: TaskIn):
    for task in tasks:
        if task.id == id:
            task.title = new_task.title
            task.description = new_task.description
            task.status = new_task.status
            return Task
    raise HTTPException(status_code=404, detail='Задача не найдена')    


@app.delete('/tasks/{id}')
async def delete_task(id):
    for task in tasks:
        if task.id == id:
            tasks.remove(task)
            return {'message': 'Задача успешно уалена!'}
    raise HTTPException(status_code=404, detail='Задача не найдена')

if __name__ == '__main__':
    uvicorn.run('task_1:app', host='127.0.0.1', port=8000, reload=True)