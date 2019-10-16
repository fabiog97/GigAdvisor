web: gunicorn Gig.wsgi
release: python manage.py migrate
web: run-program waitress-serve --port=3306 settings.wsgi:application