web: gunicorn Myquasar42.wsgi:application
web: gunicorn Myquasar42.wsgi:application --log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py migrate
