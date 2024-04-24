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
We use the "flake8" linter to apply pep 8 guidelines in our project.

We use the following commands to install Flake 8.
-pip install flake8

To know if a file meets the guidelines, we execute the command:
- flake8 <filename>

We will use the file practiFlake8.py to find out what the flake8 command returns.

- Content of practiceFlake8.py
- print('I'm fine')
- print('I'm bad')

If we execute the command it will not show us anything because the content is correct, so we will damage it for a moment so that flake8 returns us a result:

- Content of practiceFlake8.py
- print('I'm fine')
-     print('I'm bad')

By adding that indentation and running the command:

- flake8 practiceFlake8.py

It returns us:
- practiceFlake8.py:2:5: E999 IndentationError: unexpected indent