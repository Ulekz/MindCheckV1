
# 🧠 MindCheck – Evaluador de Bienestar Emocional

MindCheck es una aplicación web desarrollada con Flask que permite a los usuarios realizar una evaluación rápida de su estado emocional, recibir recursos personalizados según su nivel de ansiedad y contactar al equipo de apoyo. El sistema también incluye un panel administrativo seguro para visualizar, eliminar y exportar mensajes.

---

## 🚀 Funcionalidades principales

- 🧪 **Test de ansiedad** con resultados personalizados.
- 📚 **Recursos de apoyo emocional** según el nivel detectado.
- 📬 **Formulario de contacto** funcional.
- 🔐 **Login de administrador** .
- 📥 **Visualización de mensajes recibidos** con paginación.
- 🗑️ **Eliminación de mensajes** individual.
- 🔍 **Búsqueda por nombre o correo**.
- 📤 **Exportación a CSV**.
- 💬 **Frases motivadoras aleatorias** en el home.
- ⚙️ **Diseño moderno y responsivo**.

---

## 🛠 Tecnologías utilizadas

- Python 3.13
- Flask 3.1.0
- SQLite3
- HTML5, CSS3, Bootstrap 5.3
- Font Awesome
- Jinja2 Templates

---

## 🧰 Instalación local

1. Clona el repositorio:

```bash
git clone https://github.com/tu_usuario/MindCheckV1.git
cd MindCheckV1
```

2. Crea un entorno virtual:

```bash
python -m venv .venv
```

3. Actívalo:

- En Windows:

```bash
.\.venv\Scriptsctivate
```

- En Linux/macOS:

```bash
source .venv/bin/activate
```

4. Instala dependencias:

```bash
pip install -r requirements.txt
```

5. Ejecuta la app:

```bash
python app.py
```

---

## 🔑 Acceso al panel de administración

- Usuario: `admin`
- Contraseña: `admin123`

> *Puedes modificar los usuarios desde `database.py`.*

---

## 📁 Estructura del proyecto

```
MindCheckV1/
├── app.py
├── database.py
├── requirements.txt
├── templates/
├── static/
└── mindcheck.db (se genera automáticamente)
```

---

## ❤️ Contribuciones

Este proyecto forma parte de un ejercicio académico con enfoque social.  
Si deseas proponer mejoras o contribuir, ¡eres bienvenido/a!

---

## 📄 Licencia

Este proyecto es de uso libre para fines educativos y no comerciales.
