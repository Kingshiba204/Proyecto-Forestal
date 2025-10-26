# 🌲 Proyecto Forestal: Módulo de Gestión de Faenas (TI2041 - Actividad N°4)

> **Carrera:** Analista Programador
> [cite_start]**Asignatura:** Programación Back End [cite: 2]
> [cite_start]**Código/Sección:** T12041 [cite: 2]
> [cite_start]**Docente:** German Mardones [cite: 2]
> [cite_start]**Institución:** Inacap [cite: 3]

[cite_start]Esta es una aplicación web Django para administrar faenas de cosecha en distintos predios[cite: 4], enfocada en la administración interna y la gestión de permisos por sesión.

---

## 🚀 Requisitos del Sistema

* **Lenguaje:** Python 3.10+
* **Framework:** Django 5.2.x (se usó la versión estable más reciente).
* **Gestor de Paquetes:** `pip`
* **Entorno:** `Virtualenv` (recomendado).


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

### [cite_start]2. Pasos de Migración y Creación de Superusuario [cite: 43]

| Comando | Descripción |
| :--- | :--- |
| `python manage.py makemigrations` | Genera los archivos de migración basados en `models.py`. |
| `python manage.py migrate` | Aplica todas las migraciones a la base de datos (crea tablas de la app `faenas` y de `auth`). |
| `python manage.py createsuperuser` | Crea un usuario administrador/de prueba. **(Necesario para el login)** |

### 3. Ejecución Local

| Comando | Descripción |
| :--- | :--- |
| `python manage.py runserver` | Inicia el servidor de desarrollo. |
| **URL de Acceso:** `http://127.0.0.1:8000/` | [cite_start]Te redirigirá al login debido a la autenticación obligatoria. [cite: 8] |

---

## 🔒 Usuario de Prueba

Utilice las credenciales creadas con `createsuperuser` para acceder:

* **Usuario:** `admin`
* **Contraseña:** `admin123` (o la que se haya definido)

---

## [cite_start]💻 Descripción de la Aplicación y Módulos [cite: 44]

### [cite_start]A. Templates (Django Templates) [cite: 24, 25, 27]

| Módulo | Descripción | Requisitos Aplicados |
| :--- | :--- | :--- |
| **Herencia** | `base.html` sirve como plantilla maestra para el layout y la navegación. | [cite_start]Bloques de contenido y herencia de plantilla base. [cite: 25] |
| **Navegación** | La barra de navegación es visible (`Faenas`, `Predio activo`, `Salir`). | [cite_start]Navegación visible. [cite: 28] |
| **Formularios** | Todas las plantillas de formularios (`faena_form.html`) contienen `{% csrf_token %}`. | [cite_start]Protección CSRF. [cite: 27] |
| **Mensajes** | Se usa `django.contrib.messages` para mostrar confirmaciones y errores. | [cite_start]Uso de mensajes de sistema. [cite: 26] |

### [cite_start]B. Models y ORM (Object-Relational Mapping) [cite: 29, 33]

| Módulo | Descripción | Requisitos Aplicados |
| :--- | :--- | :--- |
| **Modelos** | `Predio` y `Faena` están definidos en `faenas/models.py`. | [cite_start]Relaciones mínimas. [cite: 21] |
| **Relaciones** | [cite_start]`Faena` se vincula a `Predio` (obligatorio)[cite: 22]. [cite_start]La asignación a `Operario` (`User`) es opcional[cite: 23]. | [cite_start]Vinculación obligatoria y opcional. [cite: 22, 23] |
| **ORM** | Todas las operaciones CRUD y consultas (filtros, ordenamiento) se realizan con métodos del ORM de Django (e.g., `Faena.objects.filter(...)`). | [cite_start]Prohibido usar SQL crudo. [cite: 33] |
| **Validaciones** | Se implementa una validación funcional en `FaenaForm` para asegurar la coherencia de fechas (`fecha_fin` no puede ser anterior a `fecha_inicio`). | [cite_start]Validaciones funcionales documentadas. [cite: 14] |

### [cite_start]C. Sessions (Sesiones) [cite: 16, 18]

| Módulo | Descripción | Requisitos Aplicados |
| :--- | :--- | :--- |
| **Predio Activo** | El usuario selecciona un predio en la vista `seleccionar_predio`. El ID se guarda en la sesión: `request.session['predio_activo_id']`. | [cite_start]El usuario debe seleccionar un "Predio activo". [cite: 17] |
| **Filtrado** | Todas las listas de faenas se filtran automáticamente por el `predio_activo_id` almacenado en la sesión. | [cite_start]El sistema filtra el listado de faenas por el predio activo. [cite: 18] |
| **Interfaz** | El nombre del predio activo se muestra claramente en el `base.html`. | [cite_start]Muestra claramente el predio activo en la interfaz. [cite: 20] |

### [cite_start]D. Security (Seguridad) [cite: 34, 35, 36, 37]

| Módulo | Descripción | Requisitos Aplicados |
| :--- | :--- | :--- |
| **Autenticación** | Las vistas de negocio están protegidas con `@login_required`. | [cite_start]Autenticación para vistas de negocio. [cite: 35] |
| **CSRF** | El *middleware* está activo, y todos los formularios usan `{% csrf_token %}`. | [cite_start]CSRF activo en formularios. [cite: 36] |
| **Cabeceras** | Se configura `X_FRAME_OPTIONS = 'DENY'` en `settings.py`. | [cite_start]Ajustes básicos de cabeceras de seguridad. [cite: 37, 38] |

---

## [cite_start]💾 Configuración de la Conexión a BD [cite: 39, 40]

El proyecto está configurado para usar **SQLite** por defecto.

* [cite_start]**Motor:** `django.db.backends.sqlite3` [cite: 40]
* **Ubicación:** `db.sqlite3` en la raíz del proyecto.

No se requiere ninguna configuración adicional para el entorno de desarrollo local.
