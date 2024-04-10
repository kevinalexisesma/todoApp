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

- (venv) \todoproject>django-admin startproject todoapp .
- (venv) \todoproject>python manage.py migrate
- (venv) \todoproject>python manage.py createsuperuser 
- (venv) \todoproject>python manage.py runserver

# Create a new virtual environment and install the project dependencies.
cd nombre-repositorio
pipenv install

# Install the dependencies from requirements.txt
pip install -r requirements.txt