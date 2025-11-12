# app.py (Flask mínima)
"""
Aplicación Flask de ejemplo para catálogo de cursos.

Actualización (nov 2025, con ayuda de Copilot):
- Se amplió la constante COURSES agregando los campos 'duration_hours' y 'level'.
- Se corrigieron pequeños detalles de arranque (__name__/__main__).
- Se documentaron ejemplos de respuesta JSON.
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

# Lista simulada de cursos (base de datos en memoria).
# Estructura (con ayuda de Copilot):
#   - id (int): Identificador único del curso.
#   - name (str): Nombre del curso.
#   - area (str): Área temática (p. ej., "CS", "Math").
#   - duration_hours (int): Duración estimada en horas.
#   - level (str): Nivel sugerido ("Básico", "Intermedio", "Avanzado").
COURSES = [
    {"id": 1, "name": "Algoritmos I", "area": "CS", "duration_hours": 20, "level": "Intermedio"},
    {"id": 2, "name": "Introducción a la Programación", "area": "CS", "duration_hours": 15, "level": "Básico"},
    {"id": 3, "name": "Matemática Discreta", "area": "Math", "duration_hours": 25, "level": "Avanzado"},
]

# Ruta principal para listar los cursos disponibles.
# Ejemplos de uso (con ayuda de Copilot):
#   GET /courses            -> devuelve todos los cursos
#   GET /courses?q=algo     -> devuelve solo los cursos que contengan "algo" en el nombre
# Ejemplo de respuesta (un elemento):
# {
#   "id": 2,
#   "name": "Introducción a la Programación",
#   "area": "CS",
#   "duration_hours": 15,
#   "level": "Básico"
# }
@app.route("/courses")
def list_courses():
    # Se obtiene el parámetro 'q' de la URL, usado como filtro opcional
    # Si la URL es /courses?q=prog, q tendrá el valor "prog"
    q = request.args.get("q", "").lower()

    # Si se recibe un filtro 'q', se buscan solo los cursos cuyo nombre contenga ese texto
    # Se convierte todo a minúsculas para que la búsqueda no distinga mayúsculas/minúsculas
    data = [c for c in COURSES if q in c["name"].lower()] if q else COURSES

    # Se devuelve la lista (filtrada o completa) en formato JSON
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
