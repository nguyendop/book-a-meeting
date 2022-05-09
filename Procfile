web: gunicorn BookMeeting.wsgi
release: python manage.py makemigrations --noiput
release: python manage.py collectstatic --noiput
release: python manage.py migrate --noiput