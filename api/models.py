from database import Base
from sqlalchemy import Column, Integer, String, Text, Date, ForeignKey, Time
from sqlalchemy.orm import relationship

class Rol(Base):
    __tablename__ = 'Roles'

    Rol_ID = Column(Integer, primary_key=True, autoincrement=True)
    Nombre_Rol = Column(String(50), nullable=False)

class Usuario(Base):
    __tablename__ = 'Usuarios'

    Usuario_ID = Column(Integer, primary_key=True, autoincrement=True)
    Nombre = Column(String(50), nullable=False)
    Apellido = Column(String(50), nullable=False)
    Correo_Electronico = Column(String(100), nullable=False)
    Contraseña = Column(String(100), nullable=False)
    Rol_ID = Column(Integer, ForeignKey('Roles.Rol_ID'))
    Encargado_Alumno_ID = Column(Integer, ForeignKey('Usuarios.Usuario_ID'))
    
    rol = relationship("Rol")
    alumnos = relationship("Alumno", back_populates="encargado")

class Asistencia(Base):
    __tablename__ = 'Asistencias'

    Asistencia_ID = Column(Integer, primary_key=True, autoincrement=True)
    Fecha = Column(Date, nullable=False)
    Hora = Column(Time, nullable=False)
    Usuario_ID = Column(Integer, ForeignKey('Usuarios.Usuario_ID'))
    Detalles = Column(Text)

class EventoAgenda(Base):
    __tablename__ = 'Agenda'

    Evento_ID = Column(Integer, primary_key=True, autoincrement=True)
    Evento = Column(String(100), nullable=False)
    Fecha = Column(Date, nullable=False)
    Ubicacion = Column(String(100))
    Descripcion = Column(Text)
    Usuario_ID = Column(Integer, ForeignKey('Usuarios.Usuario_ID'))

class Alumno(Base):
    __tablename__ = 'Alumnos'

    Alumno_ID = Column(Integer, primary_key=True, autoincrement=True)
    Nombre = Column(String(100), nullable=False)
    Detalles = Column(Text)
    Grado_ID = Column(Integer, ForeignKey('Grados.Grado_ID'))
    Encargado_ID = Column(Integer, ForeignKey('Usuarios.Usuario_ID'))

    grado = relationship("Grado")
    encargado = relationship("Usuario", foreign_keys=[Encargado_ID], back_populates="alumnos")

class Grado(Base):
    __tablename__ = 'Grados'

    Grado_ID = Column(Integer, primary_key=True, autoincrement=True)
    Nombre_Grado = Column(String(50), nullable=False)
    Detalles = Column(Text)

class AsignacionDocenteGrado(Base):
    __tablename__ = 'Asignacion_Docentes_Grados'

    Asignacion_ID = Column(Integer, primary_key=True, autoincrement=True)
    Docente_ID = Column(Integer, ForeignKey('Usuarios.Usuario_ID'))
    Grado_ID = Column(Integer, ForeignKey('Grados.Grado_ID'))
