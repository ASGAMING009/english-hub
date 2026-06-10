#!/bin/bash
set -e

echo "Running migrations..."
python manage.py migrate

echo "Loading initial data..."
if [ -f "local_data.json" ]; then
  python manage.py loaddata local_data.json --ignorenonexistent
else
  echo "No local_data.json found, skipping data import"
fi

echo "Starting gunicorn..."
gunicorn hub_site.wsgi:application
