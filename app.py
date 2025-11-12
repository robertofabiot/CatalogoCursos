# app.py (Flask mínima)
"""
Aplicación Flask de ejemplo para catálogo de cursos.

Actualización (nov 2025, con ayuda de Copilot):
- Se amplió la constante COURSES agregando los campos 'duration_hours' y 'level'.
- Se corrigieron pequeños detalles de arranque (__name__/__main__).
- Se documentaron ejemplos de respuesta JSON.
- Se añadió compatibilidad para ignorar acentos y mayúsculas.
- Se agregó mensaje cuando no se encuentran resultados.
"""
from flask import Flask, jsonify, request
from flask_cors import CORS
import unicodedata

app = Flask(__name__)
CORS(app)

# Lista simulada de cursos (base de datos en memoria).
COURSES = [
    {"id": 1, "name": "Algoritmos I", "area": "CS", "duration_hours": 20, "level": "Intermedio"},
    {"id": 2, "name": "Introducción a la Programación", "area": "CS", "duration_hours": 15, "level": "Básico"},
    {"id": 3, "name": "Matemática Discreta", "area": "Math", "duration_hours": 25, "level": "Avanzado"},
]

def normalize_text(text):
    """
    Convierte el texto a minúsculas y elimina acentos para comparación insensible.
    Ejemplo: "Programación" -> "programacion"
    """
    return ''.join(
        c for c in unicodedata.normalize('NFD', text.lower())
        if unicodedata.category(c) != 'Mn'
    )

@app.route("/courses")
def list_courses():
    # Obtiene el parámetro 'q' de la URL, usado como filtro opcional
    q = request.args.get("q", "")
    q_norm = normalize_text(q)

    # Filtra cursos ignorando mayúsculas y acentos
    data = [
        c for c in COURSES
        if q_norm in normalize_text(c["name"])
    ] if q else COURSES

    # Si no hay resultados, se devuelve un mensaje
    if not data:
        return jsonify({"message": "No se encontraron cursos"}), 404

    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
