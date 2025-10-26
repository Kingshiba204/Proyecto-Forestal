# 🌲 Proyecto Forestal: Módulo de Gestión de Faenas (TI2041 - Actividad N°4)

> **Carrera:** Analista Programador
> **Asignatura:** Programación Back End
> **Código/Sección:** T12041
> **Docente:** German Mardones
> **Institución:** Inacap

Esta es una aplicación web Django para administrar faenas de cosecha en distintos predios, enfocada en la administración interna y la gestión de permisos por sesión.

---

## 🚀 Requisitos del Sistema

* **Lenguaje:** Python 3.10+
* **Framework:** Django 5.2.x
* **Gestor de Paquetes:** `pip`
* **Entorno:** `Virtualenv`.

## 🛠️ Instalación y Ejecución (Windows PowerShell)

### 1. Requisitos e Instalación

1.  **Clonar el repositorio:**
    ```bash
    git clone [https://github.com/Kingshiba204/Proyecto-Forestal.git](https://github.com/Kingshiba204/Proyecto-Forestal.git)
    cd Proyecto-Forestal
    ```
2.  **Crear y activar el entorno virtual:**
    ```bash
    python -m venv venv
    .\venv\Scripts\Activate.ps1
    ```
3.  **Instalar dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

### 2. Pasos de Migración y Creación de Superusuario

| Comando | Descripción |
| :--- | :--- |
| `python manage.py makemigrations` | Genera los archivos de migración. |
| `python manage.py migrate` | Aplica todas las migraciones a la base de datos (crea tablas de la app `faenas` y de `auth`). |
| `python manage.py createsuperuser` | Crea un usuario administrador/de prueba. **(Necesario para el login)** |

### 3. Ejecución Local

| Comando | Descripción |
| :--- | :--- |
| `python manage.py runserver` | Inicia el servidor de desarrollo. |
| **URL de Acceso:** `http://127.0.0.1:8000/` | Te redirigirá al login debido a la autenticación obligatoria. |

---

## 🔒 Usuario de Prueba

Utilice las credenciales creadas con `createsuperuser` para acceder:

* **Usuario:** `admin`
* **Contraseña:** `admin123` (o la que se haya definido)

---

## 💻 Descripción de la Aplicación y Módulos

### A. Templates (Django Templates)

| Módulo | Descripción | Requisitos Aplicados |
| :--- | :--- | :--- |
| **Herencia** | `base.html` sirve como plantilla maestra. | Herencia de plantilla base. |
| **Navegación** | La barra de navegación es visible (Faenas, Predio activo, Salir). | Navegación visible. |
| **Formularios** | Todas las plantillas de formularios contienen `{% csrf_token %}`. | Protección CSRF. |
| **Mensajes** | Se usa `django.contrib.messages` para mostrar notificaciones. | Uso de mensajes de sistema. |

### B. Models y ORM (Object-Relational Mapping)

| Módulo | Descripción | Requisitos Aplicados |
| :--- | :--- | :--- |
| **Modelos** | `Predio` y `Faena` definidos en `faenas/models.py`. | Relaciones mínimas. |
| **Relaciones** | `Faena` se vincula a `Predio` (obligatorio). Asignación a `Operario` (`User`) es opcional. | Vinculación obligatoria y opcional. |
| **ORM** | Operaciones CRUD, consultas y ordenamiento se realizan con métodos del ORM de Django. | Prohibido usar SQL crudo. |
| **Validaciones** | Validación en `FaenaForm` asegura que `fecha_fin` no sea anterior a `fecha_inicio`. | Validaciones funcionales documentadas. |

### C. Sessions (Sesiones)

| Módulo | Descripción | Requisitos Aplicados |
| :--- | :--- | :--- |
| **Predio Activo** | El ID del predio se guarda en la sesión (`request.session['predio_activo_id']`). | El usuario debe seleccionar un "Predio activo". |
| **Filtrado** | El listado de faenas se filtra automáticamente por el ID del predio almacenado en la sesión. | El sistema filtra el listado por el predio activo. |
| **Interfaz** | El nombre del predio activo se muestra en el `base.html`. | Muestra claramente el predio activo en la interfaz. |

### D. Security (Seguridad)

| Módulo | Descripción | Requisitos Aplicados |
| :--- | :--- | :--- |
| **Autenticación** | Vistas de negocio protegidas con `@login_required`. | Autenticación para vistas de negocio. |
| **CSRF** | El *middleware* está activo, y todos los formularios usan `{% csrf_token %}`. | CSRF activo en formularios. |
| **Cabeceras** | Se configura `X_FRAME_OPTIONS = 'DENY'` en `settings.py`. | Ajustes básicos de cabeceras de seguridad. |

---

## 💾 Configuración de la Conexión a BD

El proyecto está configurado para usar **SQLite** por defecto, sin requerir configuración adicional para el entorno de desarrollo local.

* **Motor:** `django.db.backends.sqlite3`
* **Ubicación:** `db.sqlite3` en la raíz del proyecto.
