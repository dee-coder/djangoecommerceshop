'''Use this for development '''

from .base import *
ALLOWED_HOSTS += ['127.0.0.1']
DEBUG = True

WSGI_APPLICATION = 'Django_oscar.wsgi.dev.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# CORS_ORIGIN_WHITELIST = ('http://localhost:8000', )