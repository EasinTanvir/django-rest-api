# install virtual env

python -m venv .venv

# enavle virtual env

.venv\Scripts\activate

# install requirements

pip install -r requirements.txt

# Install New Django Project

django-admin startproject api

# setup New app within project

python manage.py startapp restapi

# run migrations

python manage.py makemigrations
python manage.py migrate

# Run server

python manage.py runserver

# Exist from virtual env

deactivate
