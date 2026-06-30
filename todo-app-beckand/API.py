
from  fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()
tasks: list['TaskReadSchema']

@app.get('/Hello-world')
def read_base_page():
    return{'messege': "gello world"}



class TaskReadSchema(BaseModel):
    id: str
    title: str
    completed: bool

@app.get('/tasks')
def read_tasks():
    return tasks

@app.post('/tasks')
def create_task()
print('hi')


from dataclasses import dataclass

@dataclass
class inbenItem:
    name: str
    unit_price: float
    hand: int = 0
    
    def total_cost(self) -> float