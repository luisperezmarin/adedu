from datetime import date
from pydantic import BaseModel
from typing import List


class TareaBase(BaseModel):
    DocenteID: int
    GradoID: int
    NombreTarea: str
    Descripcion: str
    FechaCreacion: date
    FechaExpiracion: date


class DocenteBase(BaseModel):
    UsuarioID: int


class RolBase(BaseModel):
    NombreRol: str


class RolCreate(RolBase):
    pass


class Rol(RolBase):
    ID: int

    class Config:
        from_attributes = True


class GradoBase(BaseModel):
    NombreGrado: str


class GradoCreate(GradoBase):
    pass


class Grado(GradoBase):
    ID: int
    Docentes: List[DocenteBase] = []

    class Config:
        from_attributes = True


class UsuarioBase(BaseModel):
    Nombres: str
    Apellidos: str
    Edad: int
    RolID: int


class UsuarioCreate(UsuarioBase):
    pass


class Usuario(UsuarioBase):
    ID: int
    Rol: Rol

    class Config:
        from_attributes = True


class DocenteCreate(DocenteBase):
    Grados: List[GradoBase] = []


class Docente(DocenteBase):
    ID: int
    Usuario: Usuario
    Grados: List[Grado] = []

    class Config:
        from_attributes = True


class EncargadoBase(BaseModel):
    UsuarioID: int
    TelefonosContacto: str
    Direccion: str
    DPI: str


class EncargadoCreate(EncargadoBase):
    pass


class Encargado(EncargadoBase):
    ID: int
    Usuario: Usuario

    class Config:
        from_attributes = True


class AlumnoBase(BaseModel):
    UsuarioID: int
    GradoID: int
    EncargadoID: int


class AlumnoCreate(AlumnoBase):
    pass


class Alumno(AlumnoBase):
    ID: int
    Usuario: Usuario
    Grado: Grado
    Encargado: Encargado
    TareasAsignadas: List[TareaBase] = []

    class Config:
        from_attributes = True


class TareaCreate(TareaBase):
    pass


class Tarea(TareaBase):
    ID: int

    class Config:
        from_attributes = True
