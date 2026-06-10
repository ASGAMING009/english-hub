#!/bin/bash
set -e

echo "Running migrations..."
python manage.py migrate

echo "Starting gunicorn..."
gunicorn hub_site.wsgi:application
