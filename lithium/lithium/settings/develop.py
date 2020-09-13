from .base import *  # noqa


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$%i1baf*de&_j#v@y5m#960*#1s2s&6h7x%su#*qnh2v83bdkt'