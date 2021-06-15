#!/usr/bin/env bash

python manage.py makemigrations

python manage.py migrate

python manage.py collectstatic

exec gunicorn recruitment_agency.wsgi:application --bind 0.0.0.0:8000
