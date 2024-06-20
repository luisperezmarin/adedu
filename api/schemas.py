from pydantic import BaseModel
from typing import List

class RolBase(BaseModel):
    Nombre_Rol: str

class RolCreate(RolBase):
    pass

class Rol(RolBase):
    Rol_ID: int

    class Config:
        from_orm = True

class UsuarioBase(BaseModel):
    Nombre: str
    Apellido: str
    Correo_Electronico: str
    Contraseña: str
    Rol_ID: int
    Encargado_Alumno_ID: int

class UsuarioCreate(UsuarioBase):
    pass

class Usuario(UsuarioBase):
    Usuario_ID: int
    rol: Rol
    alumnos: List["Alumno"]

    class Config:
        from_orm = True

class AsistenciaBase(BaseModel):
    Fecha: str
    Hora: str
    Usuario_ID: int
    Detalles: str

class AsistenciaCreate(AsistenciaBase):
    pass

class Asistencia(AsistenciaBase):
    Asistencia_ID: int

    class Config:
        from_orm = True

class EventoAgendaBase(BaseModel):
    Evento: str
    Fecha: str
    Ubicacion: str
    Descripcion: str
    Usuario_ID: int

class EventoAgendaCreate(EventoAgendaBase):
    pass

class EventoAgenda(EventoAgendaBase):
    Evento_ID: int
    usuario: Usuario

    class Config:
        from_orm = True

class AlumnoBase(BaseModel):
    Nombre: str
    Detalles: str
    Grado_ID: int
    Encargado_ID: int

class AlumnoCreate(AlumnoBase):
    pass

class Alumno(AlumnoBase):
    Alumno_ID: int
    grado: "Grado"
    encargado: Usuario

    class Config:
        from_orm = True

class GradoBase(BaseModel):
    Nombre_Grado: str
    Detalles: str

class GradoCreate(GradoBase):
    pass

class Grado(GradoBase):
    Grado_ID: int

    class Config:
        from_orm = True

class AsignacionDocenteGradoBase(BaseModel):
    Docente_ID: int
    Grado_ID: int

class AsignacionDocenteGradoCreate(AsignacionDocenteGradoBase):
    pass

class AsignacionDocenteGrado(AsignacionDocenteGradoBase):
    Asignacion_ID: int

    class Config:
        from_orm = True
