import os
from dotenv import load_dotenv

# Путь к файлу .env
dotenv_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '.env')

# Загрузка переменных среды из файла .env
load_dotenv(dotenv_path)

SECRET_KEY = os.getenv('SECRET_KEY')

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',')
MAIN_HOSTS = os.getenv('MAIN_HOSTS', 'http://127.0.0.1:8000')

DATABASES = {
    'default': {
        'ENGINE': os.getenv('DB_ENGINE', 'django.db.backends.postgresql'),
        'NAME': os.getenv('DB_NAME', 'postgres'),
        'USER': os.getenv('DB_USER', 'postgres'),
        'PASSWORD': os.getenv('DB_PASSWORD', 'postgres'),
        'HOST': os.getenv('DB_HOST', 'db'),
        'PORT': os.getenv('DB_PORT', '5432'),
    }
}

STATIC_ROOT = os.getenv('STATIC_ROOT', '/home/ubuntu/FourGimSchool/static')

MEDIA_ROOT = os.getenv('MEDIA_ROOT', '/home/ubuntu/FourGimSchool/media')


EMAIL_BACKEND = os.getenv('EMAIL_BACKEND', 'django.core.mail.backends.smtp.EmailBackend')
EMAIL_HOST = os.getenv('EMAIL_HOST', 'smtp.yandex.ru')
EMAIL_PORT = int(os.getenv('EMAIL_PORT', 465))
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', 'zhyrgal.tagaibekov@yandex.ru')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', 'pbxzozfstwthostb')
EMAIL_USE_SSL = os.getenv('EMAIL_USE_SSL', 'True').lower() == 'true'
