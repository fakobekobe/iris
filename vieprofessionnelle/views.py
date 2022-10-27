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

# Gestion du type de pièce -----------------------------------------------

@login_required
@permission_required('vieprofessionnelle.add_metier', raise_exception=True)
def ajouter_metier(request):
    pass


@login_required
@permission_required('vieprofessionnelle.change_metier', raise_exception=True)
def modifier_typepiece(request):
    pass


@login_required
@permission_required('vieprofessionnelle.delete_metier', raise_exception=True)
def supprimer_typepiece(request, id):
    pass


# Fin de la Gestion du type de pièce -------------------------------------
