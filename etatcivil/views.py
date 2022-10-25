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
def etatcivil(request):

    typepieces = TypePiece.objects.all().order_by("libelle")
    niveaux = Niveau.objects.all().order_by("id")

    # Initialisation de l'affichage de l'onglet active
    active_typepiece = ['','false','']
    active_niveau = ['','false','']

    if _active_onglet == "typepiece":
        active_typepiece =  ['active', 'true', 'show active']
    elif _active_onglet == "niveau":
        active_niveau =  ['active', 'true', 'show active']
    else:
        # Affichage par défaut
        active_typepiece =  ['active', 'true', 'show active']


    context = {
        "titre" : "Etat civil",
        "typepieces" : typepieces,
        "niveaux" : niveaux,

        "active_typepiece": active_typepiece,
        "active_niveau": active_niveau,

    }

    return render(request, "etatcivil/etatcivil.html", context)

# Gestion du type de pièce -----------------------------------------------

@login_required
@permission_required('etatcivil.add_typepiece', raise_exception=True)
def ajouter_typepiece(request):

    global _active_onglet
    _active_onglet = "typepiece"  # On initialise la variable

    if request.method == "POST":
        # On initialise les variables
        type = request.POST.get("type", None)
        libelle = request.POST.get("libelle", None)

        if type and libelle:
            # On vérifie si le code et le libelle existe
            # On format les chaine
            type = type.upper()
            libelle = libelle.upper()

            try:
                typepiece = TypePiece.objects.get(type = type)
                messages.error(request, f"Ce code :[{type}] existe déjà.")
                return HttpResponseRedirect(reverse('etatcivil:etatcivil'))

            except TypePiece.DoesNotExist:
                try:
                    typepiece = TypePiece.objects.get(libelle = libelle)
                    messages.error(request, f"Ce libellé :[{libelle}] existe déjà.")
                    return HttpResponseRedirect(reverse('etatcivil:etatcivil'))
                except TypePiece.DoesNotExist:
                    pass
            #----
            typepiece = TypePiece()
            typepiece.type = type
            typepiece.libelle = libelle
            typepiece.save()

            messages.success(request,"Enregistrement réussi.")

            return HttpResponseRedirect(reverse('etatcivil:etatcivil'))
    else:
        return HttpResponseRedirect(reverse('etatcivil:etatcivil'))

@login_required
@permission_required('etatcivil.change_typepiece', raise_exception=True)
def modifier_typepiece(request):

    global _active_onglet
    _active_onglet = "typepiece"  # On initialise la variable

    if request.method == "POST":

        try:
            typepiece = TypePiece.objects.get(id=request.POST.get('id'))
        except TypePiece.DoesNotExist:
            messages.error(request, "Ce type de pièce n'existe pas.")
            return HttpResponseRedirect(reverse('etatcivil:etatcivil'))


        if typepiece:
            # On format les chaine
            type = request.POST.get("type")
            libelle = request.POST.get("libelle")
            type = type.upper()
            libelle = libelle.upper()

            typepiece.type = type
            typepiece.libelle = libelle
            typepiece.save()

            messages.success(request, "Modification réussie.")

            return HttpResponseRedirect(reverse('etatcivil:etatcivil'))
    else:
        return HttpResponseRedirect(reverse('etatcivil:etatcivil'))

@login_required
@permission_required('etatcivil.delete_typepiece', raise_exception=True)
def supprimer_typepiece(request, id):

    global _active_onglet
    _active_onglet = "typepiece"  # On initialise la variable

    try:
        typepiece = TypePiece.objects.get(id=id)
    except TypePiece.DoesNotExist:
        messages.error(request, "Ce type de pièce n'existe pas.")
        return HttpResponseRedirect(reverse('etatcivil:etatcivil'))

    if typepiece:
        typepiece.delete()
        messages.info(request, "Suppression réussie.")

    return HttpResponseRedirect(reverse('etatcivil:etatcivil'))

# Fin de la Gestion du type de pièce -------------------------------------

# Gestion du niveau -----------------------------------------------

@login_required
@permission_required('etatcivil.add_niveau', raise_exception=True)
def ajouter_niveau(request):

    global _active_onglet
    _active_onglet = "niveau"  # On initialise la variable

    if request.method == "POST":
        # On initialise les variables
        niveau = request.POST.get("niveau", None)

        if niveau:
            # On vérifie si le niveau existe
            # On format les chaine
            niveau = niveau.capitalize()

            try:
                niveaux = Niveau.objects.get(niveau = niveau)
                messages.error(request, f"Ce niveau :[{niveau}] existe déjà.")
                return HttpResponseRedirect(reverse('etatcivil:etatcivil'))

            except Niveau.DoesNotExist:
                pass
            #----
            niveaux = Niveau()
            niveaux.niveau = niveau
            niveaux.save()

            messages.success(request,"Enregistrement réussi.")

            return HttpResponseRedirect(reverse('etatcivil:etatcivil'))
    else:
        return HttpResponseRedirect(reverse('etatcivil:etatcivil'))

@login_required
@permission_required('etatcivil.change_niveau', raise_exception=True)
def modifier_niveau(request):

    global _active_onglet
    _active_onglet = "niveau"  # On initialise la variable

    if request.method == "POST":

        try:
            niveaux = Niveau.objects.get(id=request.POST.get('id'))
        except Niveau.DoesNotExist:
            messages.error(request, "Ce niveau n'existe pas.")
            return HttpResponseRedirect(reverse('etatcivil:etatcivil'))


        if niveaux:
            # On format les chaine
            niveau_nouveau = request.POST.get("niveau")
            niveau_nouveau = niveau_nouveau.capitalize()

            # On récupère l'ancienne valeur
            ancien_niveau = niveaux.niveau

            # On vérifie si le niveau a changé
            if niveau_nouveau != ancien_niveau:
                # On vérifie si le niveau modifié existe déjà
                try:
                    niveau_test = Niveau.objects.get(niveau = niveau_nouveau)
                    messages.error(request, "Ce Niveau existe déjà.")
                    return HttpResponseRedirect(reverse('etatcivil:etatcivil'))

                except Niveau.DoesNotExist:
                    pass

            niveaux.niveau = niveau_nouveau
            niveaux.save()

            messages.success(request, "Modification réussie.")

            return HttpResponseRedirect(reverse('etatcivil:etatcivil'))
    else:
        return HttpResponseRedirect(reverse('etatcivil:etatcivil'))

@login_required
@permission_required('etatcivil.delete_niveau', raise_exception=True)
def supprimer_niveau(request, id):

    global _active_onglet
    _active_onglet = "niveau"  # On initialise la variable

    try:
        niveaux = Niveau.objects.get(id=id)
    except Niveau.DoesNotExist:
        messages.error(request, "Ce niveau n'existe pas.")
        return HttpResponseRedirect(reverse('etatcivil:etatcivil'))

    if niveaux:
        niveaux.delete()
        messages.info(request, "Suppression réussie.")

    return HttpResponseRedirect(reverse('etatcivil:etatcivil'))

# Fin de la Gestion du niveau -------------------------------------
