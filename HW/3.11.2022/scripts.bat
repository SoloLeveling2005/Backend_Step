@REM Создаем виртуальное окружение
python -m venv env
@REM Заходим в виртуальное окружение
call env/Scripts/activate.bat
@REM Устанавливаем джанго
pip install Django
@REM Создаем django проект
django-admin startproject django_settings .
@REM Создаем django приложение
django-admin startapp django_app
@REM Делаем миграцию
python manage.py makemigrations
python manage.py migrate
@REM Создаем суперюзера(например админ)
python manage.py createsuperuser
@REM Запускаем django приложение
python manage.py runserver