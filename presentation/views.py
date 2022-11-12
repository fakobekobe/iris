from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .models import *
from vieprofessionnelle.models import *
from django.contrib.auth.decorators import login_required, permission_required
from etatcivil.models import TypePiece, Nationalite
import os


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

    context = {
        'titre': "Identification - Secteur Agricole",
        'typepieces': typepieces,
        'nationalites': nationalites,
    }


    return render(request,"presentation/secteuragricole.html", context)


@login_required
@permission_required('presentation.change_membre', raise_exception=True)
def modifier_secteuragricole(request):
   pass


@login_required
@permission_required('presentation.delete_membre', raise_exception=True)
def supprimer_secteuragricole(request, id):
  pass
# Fin de la Gestion du secteur -------------------------------------
