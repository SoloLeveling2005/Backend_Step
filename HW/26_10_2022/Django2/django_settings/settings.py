
from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-w52clh$y=1g$nomh3&iz$d*+xkriv98#qpf4=r%v10%p3l3)bc'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
SQLITE = True
ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_app',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_settings.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'django_settings.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

if SQLITE:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'database/db.sqlite3',
        }
    }
else:
    # Не реальные данные (чтобы не забыть)
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': BASE_DIR / 'database/db.sqlite3',
            'USER': 'django_usr',
            'PASSWORD': '1',
            'HOST': '127.0.0.1',
            'PORT': '5432',
        }
    }

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Etc/GMT-6'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'  # префикс ссылки на статический файл
# STATIC_ROOT = Path(BASE_DIR / 'static')  # это уже путь (режим продакшена)(на линуксе статику будет отдавать nginx)
STATICFILES_DIRS = [
        Path(BASE_DIR / 'static'),
        Path(BASE_DIR / 'frontend/build/static'),
    ]
# if DEBUG:
#     STATICFILES_DIRS = [
#         # Path(BASE_DIR / 'static'),
#         Path(BASE_DIR / 'frontend/build/static'),
#     ]
# else:
#     STATICFILES_DIRS = [
#         Path(BASE_DIR / 'frontend/build/static'),
#     ]

# Файлы загружаемые пользователем (аватарки)
# MEDIA_URL = 'media/'
# MEDIA_ROOT = Path(BASE_DIR / 'static/media'),

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
