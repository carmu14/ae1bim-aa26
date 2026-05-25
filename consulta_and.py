from sqlalchemy import and_

from configuracion import Session
from crear_base_entidades import Profesor

#Uso de and_() todas las condiciones sean verdaderas
#Buscar profesores que cumplan las condiciones propuestas

session = Session()

print("---- USO DE AND ----\n")

try:
    print("*** Se filtra los profesores con especialidad 'Base de Datos y correo que comience por mari'")
    profesores = (
        session.query(Profesor)
        .filter(
            and_(
                Profesor.especialidad == "Base de Datos",
                Profesor.correo.like("mari%"),
            )
        )
        .all()
    )

    for profesor in profesores:
        print(f"- {profesor.nombres} {profesor.apellidos} | {profesor.correo} \n")

finally:
    session.close()