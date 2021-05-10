#!/bin/bash
set -e
echo "Making database migrations"
python manage.py makemigrations
echo "Applying database migrations"
python manage.py migrate
echo "Creating superuser"
python manage.py createsuperuser_if_not_exists
echo "Collecting static files"
python manage.py collectstatic --noinput

python manage.py runserver 0.0.0.0:8000