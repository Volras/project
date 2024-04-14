from fastapi import FastAPI,Depends
from pydantic import BaseModel
from typing import *

from contextlib import asynccontextmanager

from database import create_tables, delete_tables
from router import router as tasks_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("База очищена")
    await create_tables()
    print("База готова к работе")
    yield
    print("Выключение")


app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)

# @app.get("/tasks")
# def get_tasks():
#     task = Task(name="Запиши это видео")
#     return {"data": task}