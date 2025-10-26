Proyecto Forestal
Una aplicación Django para gestionar faenas de cosecha en distintos predios, con asignación opcional de operarios y predio activo por sesión.

Requisitos
Python 3.10+ (se probó con 3.13)
pip
Virtualenv (recomendado)
Django 5.2.x (versión usada en el proyecto)
(Opcional, para producción) PostgreSQL / MySQL
El repositorio contiene requirements.txt. Instala las dependencias con pip.

Instalación (Windows PowerShell)
Clona el repositorio: git clone https://github.com/Kingshiba204/Proyecto-Forestal.git
cd Proyecto-Forestal
Crear y activar un entorno virtual:
python -m venv venv
.\venv\Scripts\Activate.ps1
Instalar dependencias:
pip install -r requirements.txt

Pasos de migración y creación de datos de prueba
Crear migraciones:
python manage.py makemigrations

Aplicar migraciones:
python manage.py migrate

Crear un superusuario (administrador):
python manage.py createsuperuser

Ejecución local
Ejecutar servidor de desarrollo:
python manage.py runserver
Abrir en el navegador: http://127.0.0.1:8000/
Panel admin: http://127.0.0.1:8000/admin/

Usuario de prueba
Usuario: admin
Contraseña: admin123

Estructura y dónde se aplica cada requisito
Templates
Ubicación: faenas/templates/faenas/ y templates/registration/
base.html contiene la plantilla base con navegación (bloques de contenido).
Herencia de templates: las vistas usan {% extends "faenas/base.html" %}.
CSRF: formularios incluyen {% csrf_token %}.

Models
Definidos en models.py.
Modelos principales: Predio y Faena.
Relaciones: Faena.predio = ForeignKey(Predio) (obligatoria); Faena.operario_asignado = ForeignKey(User, null=True, blank=True) (opcional).
Faena incluye choices para estado (ej.: programada, en_ejecucion, finalizada, cancelada).

ORM
Todas las consultas se realizan con Django ORM (no SQL crudo).
Ejemplos en views.py:
Filtrar por predio activo:
Ordenamiento: .order_by('fecha_inicio', 'estado')
Documentación del código: revisa los archivos views.py y models.py para ejemplos.

Sessions
Predio activo guardado en sesión: request.session['predio_activo'] = <predio_id>.
Lectura: predio_activo_id = request.session.get('predio_activo').
El sistema filtra el listado de faenas por el predio_activo durante la sesión del usuario.

Security (seguridad)
Autenticación obligatoria en vistas de negocio: @login_required en vistas.
Flujos de login/logout:
Login: accounts/login/ (vista personalizada o la de Django).
Logout: método POST (se implementa en template como formulario con {% csrf_token %}).
CSRF activado por middleware por defecto; cada formulario tiene {% csrf_token %}.
Cabeceras de seguridad básicas en settings.py:
X_FRAME_OPTIONS = 'DENY'
DEBUG = False en producción
Otros middleware básicos en settings: SecurityMiddleware, CsrfViewMiddleware, AuthenticationMiddleware.
Recomendación: en producción, usar HTTPS, configurar ALLOWED_HOSTS y revisar SECURE_* settings.

Configuración de la conexión a la BD SQLite
En settings.py:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
No requiere más configuración para desarrollo local.
