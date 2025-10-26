# proyecto_forestal_clean

Proyecto Django para "faenas" .

Instrucciones rápidas (PowerShell)para la instalacion:

```powershell
cd C:\Users\Equipo\Desktop\BackEnd_Act\proyecto_forestal_clean
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
