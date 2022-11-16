from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .models import *
from vieprofessionnelle.models import *
from django.contrib.auth.decorators import login_required, permission_required
from etatcivil.models import TypePiece, Nationalite, Niveau, NiveauScolaire, SituationMatrimoniale
from localisation.models import *
from django.http import JsonResponse
import os

# Les constatntes et les variables globales
_active_onglet = "" # Variable globale pour l'activation des onglets


# Gestion du secteur -----------------------------------------------
@login_required
@permission_required('vieprofessionnelle.add_membre', raise_exception=True)
def index(request):
    context = {
        'titre': "Tableau de bord",
    }
    # On vérifie si la clé de session existe pour ajouter ou supprimer un cookie
    reponse = render(request, 'presentation/index.html', context)
    if request.session.get('user_id'):
        # On ajoute le cookie ou on le met à jour
        reponse.set_cookie(key='id_utilisateur', value=request.session.get('user_id'), expires=63072000)  # 63072000 = 2 ans
    else:
        # On supprime le cookie
        reponse.delete_cookie('id_utilisateur')

    return reponse


@login_required
@permission_required('vieprofessionnelle.add_membre', raise_exception=True)
def ajouter_secteuragricole(request):

    typepieces = TypePiece.objects.order_by('id')
    nationalites = Nationalite.objects.order_by('id')
    niveaux = Niveau.objects.order_by('id')
    situationmatrimoniales = SituationMatrimoniale.objects.order_by('id')
    districts = District.objects.order_by("libelle")
    regions = Region.objects.order_by("libelle")
    departements = Departement.objects.order_by("libelle")
    villes = Ville.objects.order_by("libelle")
    communes = Commune.objects.order_by("libelle")
    secteuragricoles = SecteurAgricole.objects.order_by("nom")
    typeparents = TypeParent.objects.order_by("libelle")
    parents = Parent.objects.order_by("nomprenoms")

    # Initialisation de l'affichage de l'onglet active
    active_sercteuragricole = ['', 'false', '']
    active_liste = ['', 'false', '']

    if _active_onglet == "active_sercteuragricole":
        active_sercteuragricole = ['active', 'true', 'show active']
    elif _active_onglet == "active_liste":
        active_liste = ['active', 'true', 'show active']
    else:
        # Affichage par défaut
        active_sercteuragricole = ['active', 'true', 'show active']


    context = {
        'titre': "Identification - Secteur Agricole",
        'typepieces': typepieces,
        'nationalites': nationalites,
        'niveaux': niveaux,
        'situationmatrimoniales': situationmatrimoniales,
        "districts": districts,
        "regions": regions,
        "departements": departements,
        "villes": villes,
        "communes": communes,
        "secteuragricoles": secteuragricoles,
        "typeparents": typeparents,
        "parents": parents,

        "active_sercteuragricole": active_sercteuragricole,
        "active_liste": active_liste,
    }

    if request.method == "POST":
        parents = request.POST.getlist('parent', None)
        for p in parents:
            print(p)


    return render(request,"presentation/secteuragricole.html", context)


@login_required
@permission_required('vieprofessionnelle.add_membre', raise_exception=True)
def details_niveauscolaire(request):
    if request.method == "GET":
        id = request.GET.get('id', None)
        if id:
            ajax_niveauscolaire = NiveauScolaire.objects.filter(niveau=id).order_by('id')

            if ajax_niveauscolaire:
                data = [{'id': niveauscolaire.id, 'libelle': niveauscolaire.classe} for niveauscolaire in ajax_niveauscolaire]

                return JsonResponse({'data': data}, status=200)

    return HttpResponseRedirect(reverse('presentation:ajouter_secteuragricole'))

@login_required
@permission_required('presentation.change_membre', raise_exception=True)
def modifier_secteuragricole(request):
   pass


@login_required
@permission_required('presentation.delete_membre', raise_exception=True)
def supprimer_secteuragricole(request, id):
  pass
# Fin de la Gestion du secteur -------------------------------------
