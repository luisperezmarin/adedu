from fastapi import FastAPI, HTTPException, Depends, status
from typing import Annotated, List
from database import Base, engine, SessionLocal
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from models import Rol, Grado, Usuario, Docente, Tarea
from schemas import (
    TareaBase,
    DocenteBase,
    RolBase,
    GradoBase,
    UsuarioBase,
)

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost:8000",
    "http://localhost:4200",
    "http://192.168.111.18:8000",
    "http://192.168.111.7:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


@app.post("/tareas", status_code=status.HTTP_201_CREATED)
async def create_post(task: TareaBase, db: db_dependency):
    db_task = Tarea(**task.model_dump())
    db.add(db_task)
    db.commit()


@app.get("/tarea/{task_id}", status_code=status.HTTP_200_OK)
async def read_post(task_id: int, db: db_dependency):
    task = db.query(Tarea).filter(Tarea.id == task_id).first()
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Tarea not found"
        )
    return task


@app.post("/usuarios", status_code=status.HTTP_201_CREATED)
async def create_user(user: UsuarioBase, db: db_dependency):
    db_user = Usuario(**user.model_dump())
    db.add(db_user)
    db.commit()


@app.get("/usuarios/{user_id}", status_code=status.HTTP_200_OK)
async def read_user(user_id: int, db: db_dependency):
    user = db.query(Usuario).filter(Usuario.ID == user_id).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado"
        )
    return user


@app.get("/usuarios", status_code=status.HTTP_200_OK)
async def get_users(db: db_dependency, skip: int = 0, limit: int = 100):
    users = db.query(Usuario).offset(skip).limit(limit).all()
    return users


@app.post("/roles", status_code=status.HTTP_201_CREATED)
async def create_role(role: RolBase, db: db_dependency):
    db_role = Rol(**role.model_dump())
    db.add(db_role)
    db.commit()


@app.get("/roles", status_code=status.HTTP_200_OK)
async def get_roles(db: db_dependency, skip: int = 0, limit: int = 100):
    roles = db.query(Rol).offset(skip).limit(limit).all()
    return roles
