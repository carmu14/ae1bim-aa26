from configuracion import Session
from crear_base_entidades import Profesor

#Uso de order_by() para ordenar los resultados según la columna indicada

session = Session()

print("\n---- USO DE ORDER_BY----\n")

try:

    print("*** Consulta de profesores y se ordena alfabeticamente por apellido***")
    profesores = session.query(Profesor).order_by(Profesor.apellidos).all()

    for profesor in profesores:
        print(f"- {profesor.apellidos} {profesor.nombres} | Especialidad: {profesor.especialidad}")

finally:
    session.close()