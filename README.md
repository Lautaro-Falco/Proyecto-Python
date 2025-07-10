# 🎮 Proyecto Django: Biblioteca de Videojuegos

Este es un proyecto web desarrollado con Django como parte de la cursada de Python en CoderHouse. El objetivo es crear una biblioteca interactiva donde los usuarios puedan cargar, listar y eliminar videojuegos, desarrolladores y reseñas.

---

## 🔧 Funcionalidades principales

- ✅ Carga de videojuegos, desarrolladores y reseñas mediante formularios.
- 📋 Listado completo de videojuegos con filtros por nombre, género o desarrollador.
- ❌ Eliminación individual de cualquier videojuego, desarrollador o reseña.
- 💡 Navegación simple con Bootstrap y diseño responsive.

---

## 🧩 Modelos implementados

- `Videojuego`: título, género, desarrollador, fecha de salida, puntaje.
- `Desarrollador`: nombre y país.
- `Reseña`: usuario, comentario y puntaje.

---

## 🚀 Tecnologías utilizadas

- Python 3
- Django 4.x
- Bootstrap 5
- HTML5 + CSS3

---

## 💻 ¿Cómo ejecutar el proyecto?

1. Clonar el repositorio:

2. git clone https://github.com/tu_usuario/nombre_del_repo.git

3. pip install -r requirements.txt

4. python manage.py runserver

5. http://127.0.0.1:8000/

## 📁 Estructura del proyecto
```
├── juegos/
│   ├── templates/juegos/
│   │   ├── base.html
│   │   ├── carga.html
│   │   ├── listado.html
│   │   ├── eliminar_videojuego.html
│   │   ├── eliminar_desarrollador.html
│   │   ├── eliminar_resena.html
│   └── views.py
│   └── urls.py
│   └── models.py
├── manage.py
└── README.md
```
## 🧑‍💻 Autor

**Lautaro Falco**  
Estudiante de Data Science - CoderHouse  
Este proyecto fue realizado con fines educativos.

## 👨‍🏫 Profesor

**Cristian Biancotti**

Profesor de Python - CoderHouse 

