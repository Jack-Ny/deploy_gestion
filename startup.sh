#!/bin/bash
echo "Starting Django application..."

# Appliquer les migrations de la base de données
python manage.py migrate --noinput

# Collecter les fichiers statiques
python manage.py collectstatic --noinput
python manage.py loaddata data.json

# Lancer Gunicorn pour démarrer l'application
exec gunicorn myproject.wsgi:application --bind 0.0.0.0:8000
