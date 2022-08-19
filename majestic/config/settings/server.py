from .base import *
from os import environ as env


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.get('DJANGO_SECRET_KEY', 'django-insecure-)*gf_-pcx3=s!-1#l9^zjek2kl+(dn_ua1oh4@_m%q*y%o2+2m')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.get('DJANGO_DEBUG', True)
ALLOWED_HOSTS = env.get("DJANGO_ALLOWED_HOSTS", "127.0.0.1 localhost denvyz.tmweb.ru").split(" ")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Application definition
WSGI_APPLICATION = env.get('DJANGO_WSGI_APPLICATION', 'config.wsgi.application')


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
STATIC_URL = '/static/'
if DEBUG:
    STATICFILES_DIRS = [
        BASE_DIR.parent.joinpath('static'),
    ]
else:
    STATIC_ROOT = env.get('DJANGO_STATIC_ROOT', BASE_DIR.parent.joinpath('static'))

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.joinpath('media')