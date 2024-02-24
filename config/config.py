SECRET_KEY = "django-insecure-jlk94803hk3lj198(*&^%$^&gkj*379670&%$@#$875t7gr!#@@$%^&*43sod"

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '0.0.0.0']
MAIN_HOSTS = "http://127.0.0.1:8000"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'db',
        'PORT': '5432',
    }
}

STATIC_ROOT = "/usr/src/FourGimSchool/static"

MEDIA_ROOT = "/usr/src/FourGimSchool/media"

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = "zhyrgal.tagaibekov@yandex.ru"
EMAIL_HOST_PASSWORD = "pbxzozfstwthostb"
EMAIL_USE_SSL = True
