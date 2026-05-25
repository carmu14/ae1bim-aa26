from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base, relationship
from configuracion import engine

Base = declarative_base()

class Facultad(Base):

    __tablename__ = "facultades"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False, unique=True)
    ubicacion = Column(String(120), nullable=False)
    nom_decano = Column(String(100), nullable=False)

    # Una facultad puede tener varias carreras 
    carreras = relationship(
        "Carrera",
        back_populates="facultad"
    )

    def __repr__(self):
        return "Facultad: %s - Ubicación: %s - Decano: %s" %(
            self.nombre,
            self.ubicacion,
            self.nom_decano
        )
    
class Carrera(Base):
    __tablename__ = "carreras"

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    codigo_interno = Column(String, nullable=False)

    #Clave foranea que relaciona la carrera con una facultad
    facultad_id = Column(Integer, ForeignKey("facultades.id"), nullable=False)

    #Cada carrera pertene obligatorio a una facultad
    facultad = relationship("Facultad", back_populates="carreras")

    #Una carrera puede tener muchos profesores
    profesores = relationship("Profesor", back_populates="carrera")

    def __repr__(self):
        return "Carreras: %s - nombre: %s - codigo= %s" %(
            self.id,
            self.nombre,
            self.codigo_interno
        )
    
class Profesor(Base):

    __tablename__ = "profesores"

    id = Column(Integer, primary_key=True)    
    nombres = Column(String(80), nullable=False)
    apellidos = Column(String(80), nullable=False)
    correo = Column(String(120), nullable=False, unique=True)
    especialidad = Column(String(100), nullable=False)

    #Clave foranea que relaciona el profesor con una carrera
    carrera_id = Column(Integer, ForeignKey("carreras.id"), nullable=False)

    #Cada profesor pertenece a una carrera
    carrera = relationship("Carrera", back_populates="profesores")

    #Un profesor puede crear varios recursos académicos
    recursos = relationship("RecursoAcademico", back_populates="profesor")

    def __repr__(self):
        return "Profesor: %s %s - Especialidad: %s" % (
            self.nombres,
            self.apellidos,
            self.especialidad
        )
    
class RecursoAcademico(Base):

    __tablename__ = "recursos_academicos"

    id = Column(Integer, primary_key=True)
    titulo = Column(String(150), nullable=False)
    fecha_publicacion = Column(Date, nullable=False)
    tipo = Column(String(50), nullable=False)
    clasificacion =  Column(String(80), nullable=False)
    url = Column(String(250), nullable=False, unique=True)

    #Clave foreana para indicar que profesor creó el recurso
    profesor_id = Column(Integer, ForeignKey("profesores.id"), nullable=False)

    #Cada recurso académico pertenece a un profesor
    profesor = relationship("Profesor", back_populates="recursos")

    def __repr__(self):
        return "Recurso: %s - Tipo: %s - Clasificación: %s - Fecha: %s - Url %s" %(
            self.titulo,
            self.tipo,
            self.clasificacion,
            self.fecha_publicacion,
            self.url
        )

def crear_tablas():
    print("Iniciando creación de la base de datos en SQLite...")
    print("Creando tablas: facultades, carreras, profesores y recursos_academicos")
    Base.metadata.create_all(engine)
    print("Base de datos y tablas creadas de forma correcta")

if __name__ == "__main__":
    crear_tablas()

    