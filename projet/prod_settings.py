import dj_database_url
from .settings import *

DEBUG = False
ALLOWED_HOSTS = ['chlohe-iris.herokuapp.com','app-chlohe-iris.herokuapp.com','apps-chlohe-iris.herokuapp.com']
TEMPLATE_DEBUG = False

DATABASES['default'] = dj_database_url.config()

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"