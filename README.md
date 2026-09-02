# Cowork

Plataforma de gestión de espacios de trabajo compartido (sedes, salas y reservas).

Proyecto backend desarrollado con Python y Django. Esta primera etapa cubre el núcleo del
proyecto, la aplicación `cowork` con rutas propias, una página de bienvenida y una página
de error 404 personalizada. El modelo de datos se incorpora en la siguiente etapa.

## Requisitos

- Python 3.13
- Django 5.2 (se instala desde `requirements.txt`)

## Instalación

Clonar el repositorio y ubicarse en la carpeta del proyecto:

```bash
git clone <url-del-repositorio>
cd backend_2
```

Crear el ambiente virtual:

```bash
python -m venv .venv
```

Activar el ambiente virtual:

```bash
.venv\Scripts\activate
```

En Linux o macOS:

```bash
source .venv/bin/activate
```

Instalar las dependencias:

```bash
pip install -r requirements.txt
```

## Ejecución

Con el ambiente virtual activo:

```bash
python manage.py runserver
```

- Página de bienvenida: http://127.0.0.1:8000/
- Página 404 personalizada: cualquier ruta inexistente, por ejemplo http://127.0.0.1:8000/prueba/

## Estructura

```
backend_2/
├── manage.py              Punto de entrada de los comandos de Django
├── requirements.txt       Dependencias del proyecto
├── config/                Núcleo del proyecto
│   ├── settings.py        Configuración global
│   ├── urls.py            URLconf raíz, delega en la aplicación
│   ├── wsgi.py            Adaptador para servidores WSGI
│   └── asgi.py            Adaptador para servidores ASGI
├── cowork/                Aplicación del proyecto
│   ├── urls.py            Rutas propias de la aplicación
│   ├── views.py           Vista de bienvenida
│   └── templates/cowork/
│       └── index.html     Plantilla de bienvenida
└── templates/
    └── 404.html           Plantilla de error 404 a nivel de proyecto
```

## Nota sobre DEBUG

`DEBUG` está en `False` en `config/settings.py`. Con `DEBUG = True` Django intercepta los
errores 404 y muestra su propia página de depuración, por lo que la plantilla `404.html`
nunca se renderiza. Por ese mismo motivo `ALLOWED_HOSTS` declara `127.0.0.1` y `localhost`.
