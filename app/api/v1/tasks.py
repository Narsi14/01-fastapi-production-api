from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/tasks", tags=["Tasks"])


class Task(BaseModel):
    title: str
    decription: str | None = None


class TaskResponse(BaseModel):
    id: int
    title: str
    decription: str | None = None
    status: str


tasks: list[TaskResponse] = []


@router.post("", response_model=TaskResponse, status_code=200)
async def create_task(task: Task):
    task_id = len(tasks) + 1

    new_task = TaskResponse(
        id=task_id, title=task.title, decription=task.decription, status="pending"
    )
    tasks.append(new_task)

    return new_task


@router.get("", response_model=list[TaskResponse], status_code=200)
async def get_tasks():
    return tasks


@router.get("/{task_id}", response_model=TaskResponse, status_code=200)
async def get_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")
