# 📘 CatalogoCursos

Entrega para la asignatura **Plataformas de Colaboración Digital**.

-----

## 🧩 Decisión de implementación

Se implementó la aplicación **CatalogoCursos** utilizando **Python** y **Flask** como framework principal para el backend.

El proyecto incluye:

  * API REST para listar cursos en formato JSON.
  * Filtro por nombre de curso (`q`) que **ignora mayúsculas y acentos**.
  * Mensaje de error cuando no se encuentran resultados.
  * Frontend en HTML + JavaScript para probar las funciones.
  * Soporte **CORS** para comunicación entre frontend y backend.

-----

## 🧠 Estructura del proyecto

```
CatalogoCursos/
│
├── app.py # Servidor Flask
├── index.html # Interfaz web para probar la API
├── README.md # Documentación del proyecto
└── requirements.txt # Dependencias (Flask, flask-cors)
```

-----

## 🧱 Formato JSON de cursos

Se ampliaron los campos del catálogo (con ayuda de Copilot) para reflejar duración y nivel sugerido.

### Campos por curso

| Campo | Tipo | Descripción |
| :--- | :--- | :--- |
| `id` | int | Identificador único del curso |
| `name` | str | Nombre del curso |
| `area` | str | Área temática (por ejemplo, `CS`, `Math`) |
| `duration_hours` | int | Duración estimada en horas |
| `level` | str | Nivel sugerido (`"Básico"`, `"Intermedio"`, `"Avanzado"`) |

-----

## 🧾 Ejemplo de respuesta: `GET /courses`

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

### 🔍 Ejemplo con filtro por nombre

Solicitud:

```bash
GET /courses?q=algo
```

Respuesta:

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

Si no se encuentran resultados:

```json
{
  "message": "No se encontraron cursos"
}
```

### 🌐 Frontend incluido

El archivo `index.html` permite probar la API desde el navegador:

  * Campo de búsqueda interactivo.
  * Resultados mostrados con formato de tarjetas.
  * Muestra mensajes de carga o error.

Ejecutar Flask:

```bash
python app.py
```

Abrir el frontend:

```bash
python -m http.server 8080
```

Luego visitar en el navegador:

```
http://127.0.0.1:8080/index.html
```

### ⚙️ Dependencias recomendadas

Archivo `requirements.txt`:

```
flask
flask-cors
```

Instalación:

```bash
pip install -r requirements.txt
```

### 💡 Notas finales

  * El filtro es insensible a mayúsculas y acentos, gracias a la normalización Unicode.
  * El sistema está preparado para futuras mejoras, como filtros por nivel o rango de duración.
  * Puede integrarse con bases de datos o frameworks frontend modernos (React, Vue, etc.) en versiones futuras.