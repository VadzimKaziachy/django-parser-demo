#!/bin/bash
python manage.py migrate
python manage.py collectstatic --noinput
uwsgi --http :8001 --module web.wsgi
exec "$@"