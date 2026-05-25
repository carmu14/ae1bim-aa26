from sqlalchemy import or_

from configuracion import Session
from crear_base_entidades import RecursoAcademico

#Uso de or_() devuleve los registros que cumplen al menos una de las condiciones
#Buscar recursos academicos que cumplan las condiciones propuestas

session = Session()

print("---- USO DE OR ----\n")

try:

    print("*** Se filtran los recursos acedemicos por tipo Video y Guia")
    recursos = (
        session.query(RecursoAcademico)
        .filter(
            or_(
                RecursoAcademico.tipo == "Video",
                RecursoAcademico.tipo == "Guía",
            )
        )
        .all()
    )

    for recurso in recursos:
        print(f"- {recurso.titulo} | Tipo: {recurso.tipo} | Url: {recurso.url} \n")

finally:
    session.close()