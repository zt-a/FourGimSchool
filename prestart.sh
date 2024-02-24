#!/usr/bin/env bash

sleep 10;
python manage.py makemigrations

sleep 10;
python manage.py migrate

sleep 10;
python manage.py collectstatic

sleep 10;
python manage.py runserver 0.0.0.0:8000