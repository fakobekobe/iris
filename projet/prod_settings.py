import dj_database_url
from .settings import *

DEBUG = False
ALLOWED_HOSTS = ['app-chlohe-iris.herokuapp.com']
TEMPLATE_DEBUG = False
SECRET_KEY = 'siqe7u-yaj$v*=p-4h#xpbo@e1gs)_ufwz88i^925fndi3!*kd'

DATABASES['default'] = dj_database_url.config()