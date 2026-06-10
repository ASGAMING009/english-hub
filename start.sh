#!/bin/bash
set -e

echo "Running migrations..."
python manage.py migrate

echo "Loading initial data..."
if [ -f "local_data.json" ]; then
  python manage.py loaddata local_data.json 2>/dev/null || echo "Data already loaded or file not found"
fi

echo "Starting gunicorn..."
gunicorn hub_site.wsgi:application
