from django.db import models
from django.contrib.auth.models import User, Group

# Liste des variables Globales
LISTE_MODELS = {
    'auth':{'utilisateur': User, 'groupe': Group,}
}

