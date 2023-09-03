from database import Base
from sqlalchemy import Column, Integer, String, Text, Date, Boolean, ForeignKey, Table
from sqlalchemy.orm import relationship

grados_docentes = Table(
    "grados_docentes",
    Base.metadata,
    Column("grado_id", Integer, ForeignKey("Grados.ID")),
    Column("docente_id", Integer, ForeignKey("Docentes.ID")),
)


class Rol(Base):
    __tablename__ = "Roles"
    ID = Column(Integer, primary_key=True, autoincrement=True)
    NombreRol = Column(String(50), nullable=False)


class Grado(Base):
    __tablename__ = "Grados"
    ID = Column(Integer, primary_key=True, autoincrement=True)
    NombreGrado = Column(String(50), nullable=False)
    Docentes = relationship(
        "Docente", secondary=grados_docentes, back_populates="Grados"
    )


class Usuario(Base):
    __tablename__ = "Usuarios"
    ID = Column(Integer, primary_key=True, autoincrement=True)
    Nombres = Column(String(255), nullable=False)
    Apellidos = Column(String(255), nullable=False)
    Edad = Column(Integer)
    RolID = Column(Integer, ForeignKey("Roles.ID"))
    Rol = relationship("Rol", backref="usuarios")
    Activo = Column(Boolean, default=True)


class Docente(Base):
    __tablename__ = "Docentes"
    ID = Column(Integer, primary_key=True, autoincrement=True)
    UsuarioID = Column(Integer, ForeignKey("Usuarios.ID"))
    GradoID = Column(
        Integer, ForeignKey("Grados.ID")
    )  # Clave externa que referencia al Grado asignado
    Usuario = relationship("Usuario", backref="docente")
    Grado = relationship("Grado", backref="docente")
    Grados = relationship("Grado", secondary=grados_docentes, back_populates="Docentes")


class Encargado(Base):
    __tablename__ = "Encargados"
    ID = Column(Integer, primary_key=True, autoincrement=True)
    UsuarioID = Column(Integer, ForeignKey("Usuarios.ID"))
    TelefonosContacto = Column(String(255))
    Direccion = Column(String(255))
    DPI = Column(String(20))
    Usuario = relationship("Usuario", backref="encargado")
    AlumnosACargo = relationship("Alumno", back_populates="Encargado")


class Alumno(Base):
    __tablename__ = "Alumnos"
    ID = Column(Integer, primary_key=True, autoincrement=True)
    UsuarioID = Column(Integer, ForeignKey("Usuarios.ID"))
    GradoID = Column(
        Integer, ForeignKey("Grados.ID")
    )  # Clave externa que referencia al Grado asignado
    TareasAsignadas = Column(Integer)
    Usuario = relationship("Usuario", backref="alumno")
    Grado = relationship("Grado", backref="alumno")
    EncargadoID = Column(
        Integer, ForeignKey("Encargados.ID")
    )  # Clave externa que referencia al Encargado del Alumno
    Encargado = relationship("Encargado", back_populates="AlumnosACargo")


class Tarea(Base):
    __tablename__ = "Tareas"
    ID = Column(Integer, primary_key=True, autoincrement=True)
    DocenteID = Column(
        Integer, ForeignKey("Docentes.ID")
    )  # Clave externa que referencia al Docente que crea la tarea
    GradoID = Column(
        Integer, ForeignKey("Grados.ID")
    )  # Clave externa que referencia al Grado al que se asigna la tarea
    NombreTarea = Column(String(255), nullable=False)
    Descripcion = Column(Text)
    FechaCreacion = Column(Date, nullable=False)
    FechaExpiracion = Column(Date, nullable=False)


# Tabla intermedia para la relación muchos a muchos entre Tareas y Alumnos
class TareasAlumnos(Base):
    __tablename__ = "tareas_alumnos"
    TareaID = Column(Integer, ForeignKey("Tareas.ID"), primary_key=True)
    AlumnoID = Column(Integer, ForeignKey("Alumnos.ID"), primary_key=True)
