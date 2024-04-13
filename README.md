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

# Applying linters in the project
we use the "flake8" linter to apply pep 8 guidelines in our project 

We use the "flake8" linter to apply pep 8 guidelines in our project.

To find out if a file meets the guidelines, we execute the command:
- flake8 <file name>

We will use the file practiceFlake8.py to know what the flake8 command returns.

- Content of the practicalFlake8.py
- print('I'm fine')
- print('I'm bad')