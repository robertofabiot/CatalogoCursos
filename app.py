# app.py (Flask mínima)
# Generado con ayuda de Copilot: estructura base de Flask y ruta simple.
from flask import Flask, jsonify, request

app = Flask(_name_)

# Lista simulada de cursos (base de datos en memoria)
# Cada curso tiene un 'id', un 'name' y un 'area' para clasificarlo
COURSES = [
    {"id": 1, "name": "Algoritmos I", "area": "CS"},
    {"id": 2, "name": "Introducción a la Programación", "area": "CS"},
    {"id": 3, "name": "Matemática Discreta", "area": "Math"},
]

# Ruta principal para listar los cursos disponibles
# Ejemplo de uso:
#   GET /courses           -> devuelve todos los cursos
#   GET /courses?q=algo    -> devuelve solo los cursos que contengan "algo" en el nombre
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

if _name_ == "_main_":
    app.run(debug=True)
