@echo off
echo Running migrations...
python manage.py migrate

@REM echo Creating superuser...
@REM python manage.py createsuperuser

echo Starting server...
start http://localhost:8000/admin
python manage.py runserver
