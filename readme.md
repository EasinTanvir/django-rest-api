# enavle virtual env

python -m venv .venv  
.venv\Scripts\activate

# install requirements

pip install -r requirements.txt

# Install New Django Project

django-admin startproject api

# Install New app

python manage.py startapp restapi

# migrations

python manage.py makemigrations
python manage.py migrate

# Run server

python manage.py runserver

# Exist from virtual env

deactivate
