release: python manage.py migrate --noinput
web: gunicorn booketlist.wsgi:application --bind 0.0.0.0:$PORT --workers 4 --log-file -
