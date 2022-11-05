python -m venv venv
call venv/Scripts/activate.bat
django-admin startproject django_settings .
django-admin startapp django_app
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver