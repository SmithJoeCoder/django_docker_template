"""
Django settings for django_template project.

Generated by 'django-admin startproject' using Django 3.2.12.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-+1yv$v4)s-e1d+8a$h3hky=#g15^+l*4tbnclkt1pap=uiyt4r"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

PROJECT_APPS = []

INSTALLED_APPS += PROJECT_APPS

THIRD_PARTY_APPS = [
    'django_celery_beat',
    'django_extensions',
    'psqlextra',
]

INSTALLED_APPS += THIRD_PARTY_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "django_template.urls"

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
            ],
        },
    },
]

WSGI_APPLICATION = "django_template.wsgi.application"

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DEFAULT_POSTGRES_SERVICE = os.environ.get('POSTGRES_SERVICE')
DEFAULT_POSTGRES_DB = os.environ.get('POSTGRES_DB')
DEFAULT_POSTGRES_USER = os.environ.get('POSTGRES_USER')
DEFAULT_POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
DEFAULT_POSTGRES_PORT = os.environ.get('POSTGRES_PORT')

DATABASES = {
    'default': {
        'ENGINE': 'psqlextra.backend',
        'HOST': DEFAULT_POSTGRES_SERVICE,
        'NAME': DEFAULT_POSTGRES_DB,
        'USER': DEFAULT_POSTGRES_USER,
        'PASSWORD': DEFAULT_POSTGRES_PASSWORD,
        'PORT': DEFAULT_POSTGRES_PORT,
    }
}

REDIS_HOST = os.environ.get('REDIS_HOST', 'redis')
REDIS_CACHE_LOCATION = f'redis://{REDIS_HOST}:6379'
CACHES = {
    "celery": {
        "BACKEND": "django_redis.cache.RedisCache",
        'LOCATION': f'{REDIS_CACHE_LOCATION}/0',  # db=0
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    },
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        'LOCATION': f'{REDIS_CACHE_LOCATION}/1',  # db=1
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    },
}

CELERY_ACCEPT_CONTENT = ['pickle', 'json']
CELERY_TIMEZONE = TIME_ZONE
CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL', f'redis://{REDIS_HOST}:6379')
CELERY_RESULT_BACKEND = os.getenv('CELERY_RESULT_BACKEND', None)
CELERY_TASK_DEFAULT_QUEUE = 'general'
CELERY_TASK_REJECT_ON_WORKER_LOST = (
    False if os.getenv('CELERY_TASK_REJECT_ON_WORKER_LOST', 'true').lower() == 'false' else True
)
CELERY_ACKS_LATE = False if os.getenv('CELERY_ACKS_LATE', 'true').lower() == 'false' else True
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'
