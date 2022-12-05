from django.db import models
from django.contrib.auth.models import User, Group
from localisation.models import *
from etatcivil.models import *
from vieprofessionnelle.models import *

class Parametre(models.Model):
    monnaie = models.CharField(max_length=10, null=True, blank=True, default="")
    id_chapeau = models.CharField(max_length=10, null=True, blank=True, default="")

# Liste des variables Globales
LISTE_MODELS = {
    'Authentification': {'Utilisateur': User, 'Groupe': Group, },
    'Localisation': {
        'District': District,
        'Région': Region,
        'Département': Departement,
        'Ville': Ville,
        'Commune': Commune,
        'Quartier': Quartier,
        'Marché': Marche,
    },
    'Etat_civil': {
        'Type_de_pièce': TypePiece,
        'Niveau': Niveau,
        'Niveau_scolaire': NiveauScolaire,
        'Sexe': Sexe,
        'Nationalité': Nationalite,
        'Situation_matrimoniale': SituationMatrimoniale,
    },
    'Vie_professionnelle': {
        'Type_de_secteur': TypeSecteur,
        'Secteur': Secteur,
        'Membre': Membre,
        'Secteur_agricole': SecteurAgricole,
        'Secteur_informel': SecteurInformel,
        'Secteur_femme_active': SecteurFemmeActive,
        'Type_de_parent': TypeParent,
        'Parent': Parent,
        'Type_état_de_santé': TypeEtatSante,
        'Etat_de_santé': EtatSante,
        'Type_document': TypeDocument,
        'Document': Document,
        'Chapeau': Chapeau,
        'Type_de_personne_ressource': TypePersonneRessource,
        'Personne_ressource': PersonneRessource,
        'Quantité_du_groupement': QuantiteGroupement,
        'Type_de_responsabilité': TypeResponsabilite,
        'Montant_du_financement': MontantFinancement,
    },
    'Paramètres': {
        'Paramètre': Parametre,
    },
}

