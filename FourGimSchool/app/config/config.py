import os
from pathlib import Path

_env = False

SECRET_KEY = "django-insecure-jlk94803hk3lj198(*&^%$^&gkj*379670&%$@#$875t7gr!#@@$%^&*43sod"

BASE_DIR = Path(__file__).resolve().parent.parent

MAIN_HOSTS = "http://127.0.0.1:8000"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'postgres',
        'PORT': '5432',
    }
}

STATIC_ROOT = "/var/www/html/FourGimSchool/FourGimSchool/app/static"

MEDIA_ROOT = "/var/www/html/FourGimSchool/FourGimSchool/app/media"


# EMAIL SETTINGS
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = "zhyrgal.tagaibekov@yandex.ru"
EMAIL_HOST_PASSWORD = "pbxzozfstwthostb"
EMAIL_USE_SSL = True

LOCALE_PATHS = [
    "/var/www/html/FourGimSchool/FourGimSchool/app/locale"
]

if _env:
    SECRET_KEY = os.environ.get('SECRET_KEY', SECRET_KEY)

    BASE_DIR = Path(__file__).resolve().parent.parent

    MAIN_HOSTS = os.environ.get('MAIN_HOSTS')

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ.get('DB_NAME', 'your_database_name'),
            'USER': os.environ.get('DB_USER', 'your_database_user'),
            'PASSWORD': os.environ.get('DB_PASSWORD', 'your_database_password'),
            'HOST': os.environ.get('DB_HOST', 'db'),
            'PORT': os.environ.get('DB_PORT', '5432'),
        }
    }

    STATIC_ROOT = os.environ.get('STATIC_ROOT', STATIC_ROOT)

    MEDIA_ROOT = os.environ.get('MEDIA_ROOT', MEDIA_ROOT)

    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = os.environ.get('EMAIL_HOST', EMAIL_HOST)
    EMAIL_PORT = os.environ.get('EMAIL_PORT', EMAIL_PORT)
    EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', EMAIL_HOST_USER)
    EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSOWORD', EMAIL_HOST_PASSWORD)
    EMAIL_USE_SSL = os.environ.get('EMAIL_USE_SSL', EMAIL_USE_SSL)

    LOCALE_PATHS = [
        os.environ.get('LOCALE_PATHS', LOCALE_PATHS[0])
    ]


