from django.db import models
from django.contrib.auth.models import User, Group
from localisation.models import *

# Liste des variables Globales
LISTE_MODELS = {
    'auth':{'utilisateur': User, 'groupe': Group,},
    'localisation':{'district': District, 'region': Region,},
}

