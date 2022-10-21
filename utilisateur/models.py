from django.db import models
from django.contrib.auth.models import User, Group
from localisation.models import *

# Liste des variables Globales
LISTE_MODELS = {
    'Authentification':{'Utilisateur': User, 'Groupe': Group,},
    'Localisation':{'District': District, 'Région': Region, 'Département': Departement, 'Ville': Ville},
}

