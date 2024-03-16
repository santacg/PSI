#!/bin/bash
#
set -o errexit  # exit on error

pip install -r requirements.txt

python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate
