from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

print("Cargando configuración de la base de datos...")
DATABASE_URL = "sqlite:///base_universidades.db"
# Creamos el motor de conexión
engine = create_engine(DATABASE_URL, echo=False)

# Nos permite abrir una conexión a la base para realizar las tareas correspondientes.
Session = sessionmaker(bind=engine)

print(f"Base de datos configurada: {DATABASE_URL}")
