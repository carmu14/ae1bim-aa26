from configuracion import engine, Session
from crear_base_entidades import Facultad, RecursoAcademico

#Uso de all() para devolver:
#Las facultades, mostrar sus carreras y profesores asociados

session = Session()

print("\n---- USO DE ALL ----\n")

try:
    print("\n---- FACULTADES ----")
    facultades = session.query(Facultad).all()

    print("***Se presentan las facultades, sus carreras y profesores asociados***\n")

    for facultad in facultades:
        print(f"* {facultad.nombre} | Decano: {facultad.nom_decano}")
        for carrera in facultad.carreras:
            print(f" - Carrera: {carrera.nombre} ({carrera.codigo_interno})")
            for profesor in carrera.profesores:
                print(f"     Profesor: {profesor.nombres} {profesor.apellidos}"
                      f" | Especialidad: {profesor.especialidad}"
                      )
    
    #Presentación de recursos
    print("\n--- RECURSOS ACADEMICOS ----")
    print("***Se listan todos los recursos académicos junto con el profesor creador***\n")
    recursos = session.query(RecursoAcademico).all()

    for recurso in recursos:
        print(recurso)
        print("   Profesor creador: ", recurso.profesor.nombres, recurso.profesor.apellidos)

finally:
    session.close()                
