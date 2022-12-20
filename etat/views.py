from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from vieprofessionnelle.models import *
from django.contrib.auth.decorators import login_required, permission_required
from django.http import JsonResponse
from django.utils.html import strip_tags
from django.db.models import F, Q

# Les constatntes et les variables globales
_active_onglet = ""  # Variable globale pour l'activation des onglets


@login_required
@permission_required('vieprofessionnelle.add_membre', raise_exception=True)
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
    utilisateurs = User.objects.order_by('id')

    context = {
        'titre': 'Etats',
        'typesecteurs': typesecteurs,
        'districts': districts,
        'nationalites': nationalites,
        'niveaux': niveaux,
        'utilisateurs': utilisateurs,

        'active_membre': active_membre,
        'active_cooperative': active_cooperative,
        'active_statistique': active_statistique,
    }
    return render(request, 'etat/etat.html', context)


@login_required
@permission_required('vieprofessionnelle.add_membre', raise_exception=True)
def fiche_identification(request):
    if request.method == 'POST':
        typesecteur = request.POST.get('typesecteur', None)
        secteur = request.POST.get('secteur', None)
        activite = request.POST.get('activite', None)

        district = request.POST.get('select_district', None)
        region = request.POST.get('select_region', None)
        departement = request.POST.get('select_departement', None)
        ville = request.POST.get('select_ville', None)
        commune = request.POST.get('select_commune', None)
        quartier = request.POST.get('select_quartier', None)
        marche = request.POST.get('select_marche', None)

        identifiant = strip_tags(request.POST.get('identifiant', '')).strip()
        nomprenoms = strip_tags(request.POST.get('nomprenoms', '')).strip()
        nationalite = request.POST.get('nationalite', None)
        niveau = request.POST.get('niveau', None)
        niveauscolaire = request.POST.get('niveauscolaire', None)
        utilisateur = request.POST.get('utilisateur', None)

        # Les variables
        membres = []
        # On débute par les deux critaires
        if identifiant or nomprenoms:
            if identifiant:
                membres = Membre.objects.filter(identifiant__iexact=identifiant)
            if nomprenoms and not membres:
                membres = Membre.objects.filter(nom_prenoms__iexact=nomprenoms)
        else:
            pass

        print(membres)

        return JsonResponse({'data': 'ok'}, status=200)

    return HttpResponseRedirect(reverse('etat:etat'))