from configuracion import Session
from crear_base_entidades import Facultad

#Uso de filter() para buscar un objeto especifico
#luego consume sus datos relacionados

session = Session()

print("\n---- USO DE FILTER----\n")

try:

    print("*** Busqueda de la facultad de Ingenieria***")
    facultad = (
        session.query(Facultad)
        .filter(Facultad.nombre == "Facultad de Ingenierias y Arquitectura")
        .first()
    )

    if facultad is None:
        print("No se encontro ninguna facultada relacionada \n")
    else:
        print("Facultad encontrada, se listan sus carreras mediante facultad.carreras \n")
        print(f"Carreras que pertenecen a {facultad.nombre}: ")
        for carrera in facultad.carreras:
            print(f"- {carrera.nombre} ({carrera.codigo_interno})")

finally:
    session.close()