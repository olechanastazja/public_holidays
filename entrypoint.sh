#!/bin/sh

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# Load countries fixtures
echo "Load countries fixtures"
python manage.py loaddata countries

# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput


# Start server
echo "Starting server"
python manage.py runserver 0.0.0.0:8000