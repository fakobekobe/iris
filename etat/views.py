from django.shortcuts import render
from vieprofessionnelle.models import *


# Les constatntes et les variables globales
_active_onglet = ""  # Variable globale pour l'activation des onglets


def etat(request):
    # Initialisation de l'affichage de l'onglet active
    active_membre = ['', 'false', '']
    active_cooperative = ['', 'false', '']
    active_statistique = ['', 'false', '']

    if _active_onglet == "active_membre":
        active_membre = ['active', 'true', 'show active']
    elif _active_onglet == "active_cooperative":
        active_cooperative = ['active', 'true', 'show active']
    elif _active_onglet == "active_statistique":
        active_statistique = ['active', 'true', 'show active']
    else:
        # Affichage par défaut
        active_membre = ['active', 'true', 'show active']

    typesecteurs = TypeSecteur.objects.order_by('id')
    districts = District.objects.order_by('id')
    nationalites = Nationalite.objects.order_by('id')
    niveaux = Niveau.objects.order_by('id')

    context = {
        'titre': 'Etats',
        'typesecteurs': typesecteurs,
        'districts': districts,
        'nationalites': nationalites,
        'niveaux': niveaux,

        'active_membre': active_membre,
        'active_cooperative': active_cooperative,
        'active_statistique': active_statistique,
    }
    return render(request, 'etat/etat.html', context)
