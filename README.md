# Actividad ORM SQLAlchemy - APE

Autor: Carlos Muñoz

## Entidades

- Facultad
- Carrera
- Profesor
- Recurso Académico

## Relaciones

- Una facultad tiene muchas carreras
- Una carrera pertenece a una facultad
- Una carrera tiene muchos profesores
- Un profesor perteneces a una carrera
- Un profesor puede crear muchos recursos académicos
- Cada recurso académico pertenece obligatorio a un profesor.

## Insralación

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt

