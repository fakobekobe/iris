from django.db import models
from django.contrib.auth.models import User, Group
from localisation.models import *
from etatcivil.models import *
from vieprofessionnelle.models import *

# Liste des variables Globales
LISTE_MODELS = {
    'Authentification':{'Utilisateur': User, 'Groupe': Group,},
    'Localisation':{
        'District': District,
        'Région': Region,
        'Département': Departement,
        'Ville': Ville,
        'Commune' : Commune,
        'Quartier' : Quartier,
        'Marché' : Marche,
    },
    'Etat_civil':{
        'Type_de_pièce': TypePiece,
        'Niveau': Niveau,
        'Niveau_scolaire': NiveauScolaire,
        'Sexe': Sexe,
        'Nationalité': Nationalite,
        'Situation_matrimoniale': SituationMatrimoniale,
    },
    'Vie_professionnelle':{
        'Type_secteur': TypeSecteur,
    },
}

