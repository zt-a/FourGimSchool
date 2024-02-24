
import os
from pathlib import Path
from django.utils.translation import gettext_lazy as _

BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = True

SECRET_KEY = "django-insecure-d0f5^@y6mavm2*uksamxz+)7o=(473z8znfx7&qyo@tyo&)sog"


ALLOWED_HOSTS = ['*']
MAIN_HOSTS = 'http://127.0.0.1:8000'


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
]
INSTALLED_APPS = [
    'modeltranslation',

    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django.contrib.humanize',
    'django.contrib.sitemaps',
    'django.contrib.redirects',
    'django.contrib.postgres',

    'main.apps.MainConfig',
    'news.apps.NewsConfig',
    'accounts.apps.AccountsConfig',
    'archive.apps.ArchiveConfig',
    'personal.apps.PersonalConfig',
    'books.apps.BooksConfig',
    'history.apps.HistoryConfig',
    'gallery.apps.GalleryConfig',
    'event.apps.EventConfig',
    'blog.apps.BlogConfig',
    'forum.apps.ForumConfig',
    'achievement.apps.AchievementConfig',
    'contact_news.apps.ContactNewsConfig',

    'crispy_forms',
    'rosetta'
]

CRISPY_TEMPLATE_PACK = 'bootstrap5'

ROOT_URLCONF = "app.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                'django.template.context_processors.i18n',
            ],
        },
    },
]

WSGI_APPLICATION = "app.wsgi.application"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


LANGUAGE_CODE = "ru"

TIME_ZONE = "Asia/Bishkek"

USE_I18N = True

USE_TZ = True

USE_L10N = True

SITE_ID = 1


STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

AUTH_USER_MODEL = 'accounts.CustomUser'

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = "zhyrgal.tagaibekov@yandex.ru"
EMAIL_HOST_PASSWORD = "pbxzozfstwthostb"
EMAIL_USE_SSL = True

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
SERVER_EMAIL = EMAIL_HOST_USER
EMAIL_ADMIN = EMAIL_HOST_USER

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]


LANGUAGES = [
    ('ky', _('Kyrgyz')),
    ('ru', _('Russian')),
]
MODELTRANSLATION_LANGUAGES = ('ru', 'ky')
MODELTRANSLATION_FALLBACK_LANGUAGES = ('ru', 'ky')
MODELTRANSLATION_DEFAULT_LANGUAGE = 'ru'
MODELTRANSLATION_PREPOPULATE_LANGUAGE = 'ru'

MODELTRANSLATION_TRANSLATION_FILES = (
    'achievement.translation',
    'blog.translation',
    'event.translation',
    'forum.translation',
    'gallery.translation',
    'history.translation',
    'main.translation',
    'news.translation',
)

if not DEBUG:
    from config.config import *

