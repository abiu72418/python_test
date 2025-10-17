from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

todos = []

class Todo(BaseModel):
    id: int
    task: str
    completed: bool = False

@app.post('/todos/', response_model=Todo)
async def create_todo(todo: Todo):
    todos.append(todo)
    return todo

@app.get('/todos/', response_model=List[Todo])
async def get_todos():
    return todos

@app.delete('/todos/{todo_id}', response_model=Todo)
async def delete_todo(todo_id: int):
    global todos
    todos = [todo for todo in todos if todo.id != todo_id]
    return todos
