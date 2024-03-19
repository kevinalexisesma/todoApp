# todoApp
Application in Django with super user admin

## Members

- Leonardo Trujillo Vega- 1152071 - LeonardoTrve@ufps.edu.co
- Kevin Eslava Mantilla - 1152066 - Kevinalexisesma@ufps.edu.co
- Marlon Diaz Torres - 1152054    - Marlonjosedito@ufps.edu.co

- ## installation steps

- C:\Users\Asus-PC\Downloads\todoproject>.\venv\Scripts\activate.bat
-(venv) C:\Users\Asus-PC\Downloads\todoproject>pip install django
-(venv) C:\Users\Asus-PC\Downloads\todoproject>py
    Python 3.12.2 (tags/v3.12.2:6abddd9, Feb 6 2024,21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
    Type "help", "copyright", "credits" or "license" for more information.
>>> import django
>>> print(django.get_version())
    5.0.3
>>> exit()
-(venv) C:\Users\Asus-PC\Downloads\todoproject>django-admin startproject todoapp .
-(venv) C:\Users\Asus-PC\Downloads\todoproject>python manage.py runserver
-(venv) C:\Users\Asus-PC\Downloads\todoproject>python manage.py migrate
-(venv) C:\Users\Asus-PC\Downloads\todoproject>python manage.py createsuperuser
##Login
###User: admin
###Password: admin123
