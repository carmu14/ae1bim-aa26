from datetime import date

from configuracion import Session, engine

from crear_base_entidades import Base, Carrera, Facultad, Profesor, RecursoAcademico


def poblar_base():
    print("Inciando poblado de la base de datos")

    print("Verificando que las tablas existan")
    Base.metadata.create_all(engine)

    print("Abrimos una nueva sesion...")
    session = Session()

    try:
        print("Limpiando datos para evitar registros duplicados")
        session.query(RecursoAcademico).delete()
        session.query(Profesor).delete()
        session.query(Carrera).delete()
        session.query(Facultad).delete()

        #Creamos las facultades
        print("Creando objeto de tipo Facultad...")
        ingenieria = Facultad(
            nombre="Facultad de Ingenierias y Arquitectura",
            ubicacion="Campus Utpl, bloque A",
            nom_decano="Dr. Rene Elizalde",
        )
        ciencias = Facultad(
            nombre="Facultad de Ciencias Exactas y Naturales",
            ubicacion="Campus Utpl, bloque B",
            nom_decano="Mgs. Carlos Campos",
        )
        administrativas = Facultad(
            nombre="Facultad de Ciencias Economicas y Empresariales",
            ubicacion="Campus Utpl, bloque C",
            nom_decano="Mgs. Pablo Prueba",
        )

        # Creacion de carreras asociadas a su respectiva facultad.
        print("Creando objetos de tipo Carrera...")
        software = Carrera(
            nombre="Tecnologias de la Información",
            codigo_interno="TIN-001",
            facultad=ingenieria,
        )
        redes = Carrera(
            nombre="Redes y Analítica de Datos",
            codigo_interno="EAD-002",
            facultad=ingenieria,
        )
        ambiental = Carrera(
            nombre="Gestión Ambiental",
            codigo_interno="GAM-001",
            facultad=ciencias,
        )
        riesgos = Carrera(
            nombre="Gestión de Riesgos y Desastres",
            codigo_interno="GRD-002",
            facultad=ciencias,
        )
        contabilidad = Carrera(
            nombre="Contabilidad y Auditoria",
            codigo_interno="CAU-001",
            facultad=administrativas,
        )
        economia = Carrera(
            nombre="Economía",
            codigo_interno="ECO-002",
            facultad=administrativas,
        )

        # Creacion de profesores asociados a carreras.
        print("Creando objetos de tipo Profesor...")
        profesor_1 = Profesor(
            nombres="Luis Fernando",
            apellidos="Mendoza Torres",
            correo="luis_mendoza@universidad.edu.ec",
            especialidad="Ingenieria de Software",
            carrera=software,
        )
        profesor_2 = Profesor(
            nombres="Anibal Alejandro",
            apellidos="Danse Vaca",
            correo="anibal_danse@universidad.edu.ec",
            especialidad="Programación",
            carrera=software,
        )
        profesor_3 = Profesor(
            nombres="Maria Cecilia",
            apellidos="Torres",
            correo="maria_torres@universidad.edu.ec",
            especialidad="Base de Datos",
            carrera=redes,
        )
        profesor_4 = Profesor(
            nombres="Lupe Rosaura",
            apellidos="Espinoza Torres",
            correo="lupe_espinoza@universidad.edu.ec",
            especialidad="Infraestructura",
            carrera=redes,
        )
        profesor_5 = Profesor(
            nombres="Mariana Isabel",
            apellidos="Ortega Ruiz",
            correo="mariana_ortega@universidad.edu.ec",
            especialidad="Minería",
            carrera=ambiental,
        )
        profesor_6 = Profesor(
            nombres="Paul Leonardo",
            apellidos="Calle Riofrio",
            correo="paul_calle@universidad.edu.ec.ec",
            especialidad="Logística y Transporte",
            carrera=riesgos,
        )
        profesor_7 = Profesor(
            nombres="Javier Ricardo",
            apellidos="Salinas Mora",
            correo="javier_salinas@universidad.edu.ec",
            especialidad="Gestión en Contabilidad",
            carrera=contabilidad,
        )
        profesor_8 = Profesor(
            nombres="María José",
            apellidos="Guevara Tapia",
            correo="maria_guevara@universidad.edu.ec",
            especialidad="Finanzas",
            carrera=economia,
        )

        # Creacion de recursos academicos asociados a su profesor creador.
        print("Creando objetos de tipo RecursoAcademico...")
        recurso_1 = RecursoAcademico(
            titulo="Guía de SQLAlchemy para principiantes",
            fecha_publicacion=date(2026, 5, 1),
            tipo="Guía",
            clasificacion="Desarrollo Web",
            url="https://recursos.universidad.edu.ec/sqlalchemy-guia",
            profesor=profesor_1,
        )
        recurso_2 = RecursoAcademico(
            titulo="Caso de estudio de algoritmos",
            fecha_publicacion=date(2023, 3, 15),
            tipo="Caso de estudio",
            clasificacion="Clasifica DW2",
            url="https://recursos.universidad.edu.ec/recurso_dw02",
            profesor=profesor_1,
        )
        recurso_3 = RecursoAcademico(
            titulo="Video resumen de generación de algoritmos",
            fecha_publicacion=date(2022, 3, 15),
            tipo="Video",
            clasificacion="Clasifica RIF01",
            url="https://recursos.universidad.edu.ec/recurso_rif02",
            profesor=profesor_2,
        )
        recurso_4 = RecursoAcademico(
            titulo="Guía de programación orientada a objetos",
            fecha_publicacion=date(2026, 10, 1),
            tipo="Guía",
            clasificacion="Clasifica RIF02",
            url="https://recursos.universidad.edu.ec/recurso_rif03",
            profesor=profesor_2,
        )
        recurso_5 = RecursoAcademico(
            titulo="Practica de normalizacion de bases de datos",
            fecha_publicacion=date(2023, 5, 8),
            tipo="Practica",
            clasificacion="Bases de datos",
            url="https://recursos.universidad.edu.ec/normalizacion-practica",
            profesor=profesor_3,
        )
        recurso_6 = RecursoAcademico(
            titulo="Guía de bases de datos no relacionales",
            fecha_publicacion=date(2023, 5, 9),
            tipo="Guía",
            clasificacion="Bases de Datos",
            url="https://recursos.universidad.edu.ec/guia_nosql",
            profesor=profesor_3,
        )
        recurso_7 = RecursoAcademico(
            titulo="Video informativo",
            fecha_publicacion=date(2026, 4, 20),
            tipo="Video",
            clasificacion="Clasifi 1",
            url="https://recursos.universidad.edu.ec/recurso1",
            profesor=profesor_4,
        )
        recurso_8 = RecursoAcademico(
            titulo="Caso de estudio de planificacion estrategica",
            fecha_publicacion=date(2026, 3, 15),
            tipo="Caso de estudio",
            clasificacion="Clasifi 2",
            url="https://recursos.universidad.edu.ec/recurso2",
            profesor=profesor_4,
        )
        recurso_9 = RecursoAcademico(
            titulo="Guía de contenidos",
            fecha_publicacion=date(2026, 4, 20),
            tipo="Guía",
            clasificacion="Clasif MIN001",
            url="https://recursos.universidad.edu.ec/recursos_grd01",
            profesor=profesor_5,
        )
        recurso_10 = RecursoAcademico(
            titulo="Caso de estudio de suelos",
            fecha_publicacion=date(2026, 3, 15),
            tipo="Caso de estudio",
            clasificacion="Clasif MIN002",
            url="https://recursos.universidad.edu.ec/recursos_grd02",
            profesor=profesor_5,
        )
        recurso_11 = RecursoAcademico(
            titulo="Video sobre recursos didacticos",
            fecha_publicacion=date(2026, 5, 20),
            tipo="Video",
            clasificacion="Clasifica LT01",
            url="https://recursos.universidad.edu.ec/recurso_lt01",
            profesor=profesor_6,
        )
        recurso_12 = RecursoAcademico(
            titulo="Caso de estudio de planificacion estrategica",
            fecha_publicacion=date(2026, 5, 15),
            tipo="Caso de estudio",
            clasificacion="Clasifica LT02",
            url="https://recursos.universidad.edu.ec/recurso_lt02",
            profesor=profesor_6,
        )
        recurso_13 = RecursoAcademico(
            titulo="Caso de estudio de impuestos ecuador",
            fecha_publicacion=date(2025, 4, 20),
            tipo="Caso de estudio",
            clasificacion="Clasifica CAO01",
            url="https://recursos.universidad.edu.ec/recurso_ca01",
            profesor=profesor_7,
        )
        recurso_14 = RecursoAcademico(
            titulo="Guia didactica contabilidad",
            fecha_publicacion=date(2024, 3, 15),
            tipo="Guía",
            clasificacion="Clasifica CAO02",
            url="https://recursos.universidad.edu.ec/recurso_ca02",
            profesor=profesor_7,
        )
        recurso_15 = RecursoAcademico(
            titulo="Guía Didactica planificacción de la materia",
            fecha_publicacion=date(2025, 4, 20),
            tipo="Guía",
            clasificacion="Clasifica ECO01",
            url="https://recursos.universidad.edu.ec/recurso_eco01",
            profesor=profesor_8,
        )
        recurso_16 = RecursoAcademico(
            titulo="Caso de estudio de economias globales",
            fecha_publicacion=date(2024, 3, 15),
            tipo="Caso de estudio",
            clasificacion="Clasifica ECO02",
            url="https://recursos.universidad.edu.ec/recurso_econ02",
            profesor=profesor_8,
        )        

        #Se usa add_all para agregar todos los objetos a las sesión
        print("Guardando los objetos relacionados en la base de datos...")
        session.add_all([ingenieria, ciencias, administrativas, 
                         software, redes, ambiental, riesgos, contabilidad, economia,
                         profesor_1, profesor_2, profesor_3, profesor_4, profesor_5, profesor_6, profesor_7, profesor_8,
                         recurso_1, recurso_2, recurso_3, recurso_4, recurso_5, recurso_6, recurso_7, recurso_8, recurso_9, 
                         recurso_10, recurso_11, recurso_12, recurso_13, recurso_14, recurso_15, recurso_16]
                        )
        session.commit()
        print("Datos insertados correctamente.")
    
    except Exception as error:
        #En caso de error se realiza rollback
        session.rollback()
        print(f"Error al poblar la base:  {error}")
    finally:
        print("Se cierra sesión con la base de datos")
        session.close()

if __name__ == "__main__":
    poblar_base()