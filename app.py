# app.py (Flask mínima)
# Generado con ayuda de Copilot: estructura base de Flask y ruta simple.
from flask import Flask, jsonify, request

app = Flask(__name__)

COURSES = [
    {"id": 1, "name": "Algoritmos I", "area": "CS "},
    {"id": 2, "name": "Introducción a la Programación", "area": "CS"},
    {"id": 3, "name": "Matemática Discreta", "area": "Math"},
]

@app.route("/courses")
def list_courses():
    q = request.args.get("q", "").lower()
    data = [c for c in COURSES if q in c["name"].lower()] if q else COURSES
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
