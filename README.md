# Backend – Jobless as a Service™

> Backend funcional para un sistema sin propósito.  
> Diseñado para registrar el fracaso, automatizar la humillación y convertir la desesperanza en datos estructurados.

---

## 🗂 Índice

1. [🧠 Tecnologías](#-tecnologías)
2. [📁 Estructura base](#-estructura-base)
3. [🔧 Instalación rápida](#-instalación-rápida)
4. [🛠 Modelos previstos](#-modelos-previstos)
5. [📡 API prevista](#-api-prevista)
6. [📜 Licencia](#-licencia)

---

## 🧠 Tecnologías

- Python 3.10+
- Django 4.x
- Django REST Framework
- PostgreSQL o SQLite (según nivel de resignación)
- django-cors-headers
- python-decouple
- (Opcional) FastAPI para microservicio MCP (insultador profesional)

---

## 📁 Estructura base

backend/
├── core/ # App principal del sistema
├── backend/ # Configuración del proyecto Django
├── manage.py
├── requirements.txt
├── .env
├── .gitignore
├── README.md
├── LICENSE

---

## 🔧 Instalación rápida

1. Crear y activar entorno virtual:

```bash
python -m venv venv
source venv/bin/activate
.\venv\Scripts\activate
```

2. Instalar dependencias:

```bash
pip install -r requirements.txt
```

3. Crear archivo `.env` y configurar variables de entorno:

```bash
SECRET_KEY=tu_clave_aleatoria
DEBUG=True
ALLOWED_HOSTS=localhost
DATABASE_URL=sqlite:///db.sqlite3
```

4. Migrar base de datos:

```bash
python manage.py migrate
```

5. Crear superusuario:

```bash
python manage.py createsuperuser
```

6. Correr el servidor:

```bash
python manage.py runserver
```

7. Acceder a la API en `http://localhost:8000/api/` y al panel de administración en `http://localhost:8000/admin/`.

---

## 🛠 Modelos previstos

Estos modelos representan piezas rotas de un individuo funcional.

`PerfilHumillado`
Identidad digital de alguien que ya no espera nada.
Campos: nombre, biografía, manifiesto, fecha de inicio del paro, nivel de rendición, avatar.

`Rechazo`
Cada aplicación ignorada o descartada sin motivo.
Registrado como dato irrelevante pero persistente.

`Interaccion`
Insultos y frases destructivas enviadas entre perfiles.
Porque el fracaso compartido también puede doler.

`FraseFlotante`
Mensajes nihilistas que rotan en el topbar del frontend.
No sirven, pero se ven bien.

---

## 📡 API prevista

```
json
GET    /api/perfiles/             → Listado de perfiles humillados
GET    /api/perfil/<id>/          → Detalle de un perfil
POST   /api/perfiles/             → Crear nuevo perfil condenado

GET    /api/frases/               → Frases rotativas para el topbar

POST   /api/humillarme/           → Obtener frase destructiva (vía MCP)
POST   /api/interactuar/<tipo>/   → Enviar insulto a otro perfil

GET    /api/rechazos/             → Rechazos registrados
POST   /api/rechazos/             → Agregar nuevo rechazo
```

---
