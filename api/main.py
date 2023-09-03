from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Annotated
from database import Base, engine, SessionLocal
from sqlalchemy.orm import Session

from models import Rol, Grado, Usuario, Docente, Tarea
from schemas import (
    TareaBase,
    DocenteBase,
    RolBase,
    GradoBase,
    UsuarioBase,
)

app = FastAPI()

Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


@app.post("/tasks", status_code=status.HTTP_201_CREATED)
async def create_post(task: TareaBase, db: db_dependency):
    db_task = Tarea(**task.model_dump())
    db.add(db_task)
    db.commit()


@app.get("/task/{task_id}", status_code=status.HTTP_200_OK)
async def read_post(task_id: int, db: db_dependency):
    task = db.query(Tarea).filter(Tarea.id == task_id).first()
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Tarea not found"
        )
    return task


@app.post("/users", status_code=status.HTTP_201_CREATED)
async def create_user(user: UsuarioBase, db: db_dependency):
    db_user = Usuario(**user.model_dump())
    db.add(db_user)
    db.commit()


@app.get("/users/{user_id}", status_code=status.HTTP_200_OK)
async def read_user(user_id: int, db: db_dependency):
    user = db.query(Usuario).filter(Usuario.id == user_id).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Usuario not found"
        )
    return user
