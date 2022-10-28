from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required, permission_required
from django.http import JsonResponse

# Les constatntes et les variables globales
_active_onglet = "" # Variable globale pour l'activation des onglets

@login_required
@permission_required('auth.view_user', raise_exception=True)
@permission_required('auth.view_group', raise_exception=True)
def vieprofessionnelle(request):

    pass

# Gestion du type de secteur -----------------------------------------------
@login_required
@permission_required('vieprofessionnelle.add_typesecteur', raise_exception=True)
def ajouter_typesecteur(request):
    pass


@login_required
@permission_required('vieprofessionnelle.change_typesecteur', raise_exception=True)
def modifier_typesecteur(request):
    pass


@login_required
@permission_required('vieprofessionnelle.delete_typesecteur', raise_exception=True)
def supprimer_typesecteur(request, id):
    pass
# Fin de la Gestion du type de secteur -------------------------------------
