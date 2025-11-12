# CatalogoCursos
Entrega para plataformas de colaboración digital.

## Decisión de implementación
Hemos decidido utilizar la versión de la aplicación CatalogoCursos elaborada en Python y Flask.

## Formato JSON de cursos (actualizado con ayuda de Copilot)
Se añadieron los campos `duration_hours` y `level` a cada curso para reflejar la duración estimada y el nivel sugerido.

Campos por curso:
- `id` (int): Identificador único.
- `name` (str): Nombre del curso.
- `area` (str): Área temática (p. ej., CS, Math).
- `duration_hours` (int): Duración estimada en horas.
- `level` (str): Nivel sugerido ("Básico", "Intermedio", "Avanzado").

### Ejemplo de respuesta para `GET /courses`
```json
[
	{
		"id": 1,
		"name": "Algoritmos I",
		"area": "CS",
		"duration_hours": 20,
		"level": "Intermedio"
	},
	{
		"id": 2,
		"name": "Introducción a la Programación",
		"area": "CS",
		"duration_hours": 15,
		"level": "Básico"
	},
	{
		"id": 3,
		"name": "Matemática Discreta",
		"area": "Math",
		"duration_hours": 25,
		"level": "Avanzado"
	}
]
```

### Ejemplo con filtro por nombre
`GET /courses?q=algo`
```json
[
	{
		"id": 1,
		"name": "Algoritmos I",
		"area": "CS",
		"duration_hours": 20,
		"level": "Intermedio"
	}
]
```

> Nota (con ayuda de Copilot): estos campos abren la puerta a futuros filtros por nivel o por rango de duración.
