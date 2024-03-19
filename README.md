# todoApp
Application in Django with super user admin

## Members

- Leonardo Trujillo Vega- 1152071 - LeonardoTrve@ufps.edu.co
- Kevin Eslava Mantilla - 1152066 - Kevinalexisesma@ufps.edu.co
- Marlon Diaz Torres - 1152054    - Marlonjosedito@ufps.edu.co

## installation steps

- .\todoproject>.\venv\Scripts\activate.bat
- (venv) .\todoproject>pip install django
- (venv) .\todoproject>py

Inside the python console:
>>> import django
>>> print(django.get_version())
    5.0.3
>>> exit()

- (venv) C:\Users\Asus-PC\Downloads\todoproject>django-admin startproject todoapp .
- (venv) C:\Users\Asus-PC\Downloads\todoproject>python manage.py migrate
- (venv) C:\Users\Asus-PC\Downloads\todoproject>python manage.py createsuperuser 
- (venv) C:\Users\Asus-PC\Downloads\todoproject>python manage.py runserver

## Login of the super user created
### User: 
admin
### Password: 
admin123
