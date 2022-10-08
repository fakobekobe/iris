import dj_database_url
from .settings import *

DEBUG = False
ALLOWED_HOSTS = ['app-chlohe-iris.herokuapp.com']
TEMPLATE_DEBUG = False

DATABASES['default'] = dj_database_url.config()

MIDDLEWARE += ["whitenoise.middleware.WhiteNoiseMiddleware"]
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"