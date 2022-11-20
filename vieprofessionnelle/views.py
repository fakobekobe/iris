from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required, permission_required
from django.http import JsonResponse
import os
from datetime import datetime


# Les constatntes et les variables globales
_active_onglet = "" # Variable globale pour l'activation des onglets

@login_required
@permission_required('auth.view_user', raise_exception=True)
@permission_required('auth.view_group', raise_exception=True)
def vieprofessionnelle(request):
    typesecteurs = TypeSecteur.objects.order_by("type")
    secteurs = Secteur.objects.order_by("secteur")
    typeparents = TypeParent.objects.order_by("libelle")
    parents = Parent.objects.order_by("nomprenoms")
    typeetatsantes = TypeEtatSante.objects.order_by("libelle")
    typedocuments = TypeDocument.objects.order_by("libelle")
    documents = Document.objects.order_by("-id")
    membres = Membre.objects.order_by("-id")

    # Initialisation de l'affichage de l'onglet active
    active_typesecteur = ['', 'false', '']
    active_secteur = ['', 'false', '']
    active_typeparent = ['', 'false', '']
    active_parent = ['', 'false', '']
    active_typeetatsante = ['', 'false', '']
    active_typedocument = ['', 'false', '']
    active_document = ['', 'false', '']

    if _active_onglet == "typesecteur":
        active_typesecteur = ['active', 'true', 'show active']
    elif _active_onglet == "secteur":
        active_secteur = ['active', 'true', 'show active']
    elif _active_onglet == "typeparent":
        active_typeparent = ['active', 'true', 'show active']
    elif _active_onglet == "parent":
        active_parent = ['active', 'true', 'show active']
    elif _active_onglet == "typeetatsante":
        active_typeetatsante = ['active', 'true', 'show active']
    elif _active_onglet == "typedocument":
        active_typedocument = ['active', 'true', 'show active']
    elif _active_onglet == "document":
        active_document = ['active', 'true', 'show active']
    else:
        # Affichage par défaut
        active_typesecteur = ['active', 'true', 'show active']

    context = {
        "titre": "Vie professionnelle",
        "typesecteurs": typesecteurs,
        "secteurs": secteurs,
        "typeparents": typeparents,
        "parents": parents,
        "typeetatsantes": typeetatsantes,
        "typedocuments": typedocuments,
        "documents": documents,
        "membres": membres,


        "active_typesecteur": active_typesecteur,
        "active_secteur": active_secteur,
        "active_typeparent": active_typeparent,
        "active_parent": active_parent,
        "active_typeetatsante": active_typeetatsante,
        "active_typedocument": active_typedocument,
        "active_document": active_document,

    }

    return render(request, "vieprofessionnelle/vieprofessionnelle.html", context)

# Gestion du type de secteur -----------------------------------------------
@login_required
@permission_required('vieprofessionnelle.add_typesecteur', raise_exception=True)
def ajouter_typesecteur(request):
    global _active_onglet
    _active_onglet = "typesecteur"  # On initialise la variable

    if request.method == "POST":
        # On initialise les variables
        type = request.POST.get("type", None)

        if type:  # On vérifie si les champs ont été renseignés

            # On format les chaines
            type = type.upper()

            try:
                objet_typesecteur = TypeSecteur.objects.get(type=type)
                messages.error(request, f"Ce type :[{type}] existe déjà.")
                return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))

            except TypeSecteur.DoesNotExist:
                pass

            # ----
            objet_typesecteur = TypeSecteur()
            objet_typesecteur.type = type
            objet_typesecteur.save()

            messages.success(request, "Enregistrement réussi.")

            return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))
    else:
        return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))


@login_required
@permission_required('vieprofessionnelle.change_typesecteur', raise_exception=True)
def modifier_typesecteur(request):
    global _active_onglet
    _active_onglet = "typesecteur"  # On initialise la variable

    if request.method == "POST":

        try:
            objet_typesecteur = TypeSecteur.objects.get(id=request.POST.get('id'))
        except TypeSecteur.DoesNotExist:
            messages.error(request, "Ce type de secteur n'existe pas.")
            return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))

        if objet_typesecteur:
            # On format les chaine
            type_nouveau = request.POST.get("type", None)
            type_nouveau = type_nouveau.upper()

            # On récupère l'ancienne valeur
            type_ancien = objet_typesecteur.type

            # On vérifie si la valeur a changé
            if type_nouveau != type_ancien:
                # On vérifie si le valeur modifié existe déjà
                try:
                    TypeSecteur.objects.get(type=type_nouveau)
                    messages.error(request, f"Ce type de secteur [{type_nouveau}] existe déjà.")
                    return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))

                except TypeSecteur.DoesNotExist:
                    pass

            # On effectue la modification
            objet_typesecteur.type = type_nouveau
            objet_typesecteur.save()

            messages.success(request, "Modification réussie.")

            return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))
    else:
        return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))


@login_required
@permission_required('vieprofessionnelle.delete_typesecteur', raise_exception=True)
def supprimer_typesecteur(request, id):
    global _active_onglet
    _active_onglet = "typesecteur"  # On initialise la variable

    try:
        objet_typesecteur = TypeSecteur.objects.get(id=id)
    except TypeSecteur.DoesNotExist:
        messages.error(request, "Ce type de secteur n'existe pas.")
        return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))

    if objet_typesecteur:
        objet_typesecteur.delete()
        messages.info(request, "Suppression réussie.")

    return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))
# Fin de la Gestion du type de secteur -------------------------------------

# Gestion du secteur -----------------------------------------------
@login_required
@permission_required('vieprofessionnelle.add_secteur', raise_exception=True)
def ajouter_secteur(request):
    global _active_onglet
    _active_onglet = "secteur"  # On initialise la variable

    if request.method == "POST":
        # On initialise les variables
        secteur = request.POST.get("secteur", None)
        typesecteur = request.POST.get("select_typesecteur", None)

        if secteur and typesecteur:  # On vérifie si les champs ont été renseignés

            # On format les chaines
            secteur = secteur.capitalize()

            try:
                objet_secteur = Secteur.objects.get(secteur=secteur)
                messages.error(request, f"Ce secteur :[{secteur}] existe déjà.")
                return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))

            except Secteur.DoesNotExist:
                pass

            # ----
            objet_secteur = Secteur()
            objet_secteur.secteur = secteur
            objet_secteur.typesecteur = TypeSecteur.objects.get(id=typesecteur)
            objet_secteur.save()

            messages.success(request, "Enregistrement réussi.")

            return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))
    else:
        return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))


@login_required
@permission_required('vieprofessionnelle.change_secteur', raise_exception=True)
def modifier_secteur(request):
    global _active_onglet
    _active_onglet = "secteur"  # On initialise la variable

    if request.method == "POST":

        try:
            objet_secteur = Secteur.objects.get(id=request.POST.get('id'))
        except Secteur.DoesNotExist:
            messages.error(request, "Ce secteur n'existe pas.")
            return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))

        if objet_secteur:
            # On format les chaine
            secteur_nouveau = request.POST.get("secteur", None)
            secteur_nouveau = secteur_nouveau.capitalize()

            typesecteur = request.POST.get("select_typesecteur", None)

            # On récupère l'ancienne valeur
            secteur_ancien = objet_secteur.secteur

            # On vérifie si la valeur a changé
            if secteur_nouveau != secteur_ancien:
                # On vérifie si le valeur modifié existe déjà
                try:
                    Secteur.objects.get(secteur=secteur_nouveau)
                    messages.error(request, f"Ce secteur [{secteur_nouveau}] existe déjà.")
                    return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))

                except Secteur.DoesNotExist:
                    pass

            # On effectue la modification
            objet_secteur.secteur = secteur_nouveau
            objet_secteur.typesecteur = TypeSecteur.objects.get(id=typesecteur)
            objet_secteur.save()

            messages.success(request, "Modification réussie.")

            return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))
    else:
        return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))


@login_required
@permission_required('vieprofessionnelle.delete_secteur', raise_exception=True)
def supprimer_secteur(request, id):
    global _active_onglet
    _active_onglet = "secteur"  # On initialise la variable

    try:
        objet_secteur = Secteur.objects.get(id=id)
    except Secteur.DoesNotExist:
        messages.error(request, "Ce secteur n'existe pas.")
        return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))

    if objet_secteur:
        objet_secteur.delete()
        messages.info(request, "Suppression réussie.")

    return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))

@login_required
@permission_required('vieprofessionnelle.add_secteur', raise_exception=True)
def details_secteur(request):

    if request.method == "GET":
        id = request.GET.get('id', None)
        if id:
            ajax_secteur = Secteur.objects.filter(typesecteur=id).order_by('secteur')

            if ajax_secteur:
                data = [{'id': secteur.id, 'libelle': secteur.secteur} for secteur in ajax_secteur]

                return JsonResponse({'data': data}, status=200)

    return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))
# Fin de la Gestion du secteur -------------------------------------

# Gestion du type de parent -----------------------------------------------
@login_required
@permission_required('vieprofessionnelle.add_typeparent', raise_exception=True)
def ajouter_typeparent(request):
    global _active_onglet
    _active_onglet = "typeparent"  # On initialise la variable

    if request.method == "POST":
        # On initialise les variables
        libelle = request.POST.get("libelle", None)

        if libelle:  # On vérifie si le champ a été renseigné

            # On format les chaines
            libelle = libelle.capitalize()

            try:
                objet_typeparent = TypeParent.objects.get(libelle=libelle)
                messages.error(request, f"Ce type de parent :[{libelle}] existe déjà.")
                return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))

            except TypeParent.DoesNotExist:
                pass

            # ----
            objet_typeparent = TypeParent()
            objet_typeparent.libelle = libelle
            objet_typeparent.save()

            messages.success(request, "Enregistrement réussi.")

            return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))
    else:
        return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))


@login_required
@permission_required('vieprofessionnelle.change_typeparent', raise_exception=True)
def modifier_typeparent(request):
    global _active_onglet
    _active_onglet = "typeparent"  # On initialise la variable

    if request.method == "POST":

        try:
            objet_typeparent = TypeParent.objects.get(id=request.POST.get('id'))
        except TypeParent.DoesNotExist:
            messages.error(request, "Ce type de parent n'existe pas.")
            return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))

        if objet_typeparent:
            # On format les chaine
            libelle_nouveau = request.POST.get("libelle", None)
            libelle_nouveau = libelle_nouveau.capitalize()

            # On récupère l'ancienne valeur
            libelle_ancien = objet_typeparent.libelle

            # On vérifie si la valeur a changé
            if libelle_nouveau != libelle_ancien:
                # On vérifie si le valeur modifié existe déjà
                try:
                    TypeParent.objects.get(libelle=libelle_nouveau)
                    messages.error(request, f"Ce type de parent [{libelle_nouveau}] existe déjà.")
                    return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))

                except TypeParent.DoesNotExist:
                    pass

            # On effectue la modification
            objet_typeparent.libelle = libelle_nouveau
            objet_typeparent.save()

            messages.success(request, "Modification réussie.")

            return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))
    else:
        return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))


@login_required
@permission_required('vieprofessionnelle.delete_typeparent', raise_exception=True)
def supprimer_typeparent(request, id):
    global _active_onglet
    _active_onglet = "typeparent"  # On initialise la variable

    try:
        objet_typeparent = TypeParent.objects.get(id=id)
    except TypeParent.DoesNotExist:
        messages.error(request, "Ce type de parent n'existe pas.")
        return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))

    if objet_typeparent:
        objet_typeparent.delete()
        messages.info(request, "Suppression réussie.")

    return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))
# Fin de la Gestion du type de parent -------------------------------------

# Gestion du parent -----------------------------------------------
@login_required
@permission_required('vieprofessionnelle.add_parent', raise_exception=True)
def ajouter_parent(request):
    global _active_onglet
    _active_onglet = "parent"  # On initialise la variable

    if request.method == "POST":
        # On initialise les variables
        nomprenoms = request.POST.get("nomprenoms", None)
        datenaissance = request.POST.get("datenaissance", None)
        adresse = request.POST.get("adresse", None)
        contact = request.POST.get("contact", None)

        if not datenaissance : # On teste si la date n'existe pas
            datenaissance = None

        typeparent = request.POST.get("select_typeparent", None)

        if nomprenoms and typeparent:  # On vérifie si les champs ont été renseignés

            # On format les chaines
            nomprenoms = nomprenoms.title()

            # ----
            objet_parent = Parent()
            objet_parent.nomprenoms = nomprenoms
            objet_parent.datenaissance = datenaissance
            objet_parent.adresse = adresse
            objet_parent.contact = contact
            objet_parent.dateenre = datetime.now()
            objet_parent.typeparent = TypeParent.objects.get(id=typeparent)
            objet_parent.save()

            # Traitement JSON ------------------------
            if request.POST.get('id_json', None):
                data = {
                    'id': objet_parent.id,
                    'nomprenoms': objet_parent.nomprenoms,
                    'message': "Enregistrement réussi",
                }

                return JsonResponse({'data': data}, status=200)
            #------------------------------------------------------

            messages.success(request, "Enregistrement réussi.")
            return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))
        else:

            # Traitement JSON -----------------------------------
            if request.POST.get('id_json', None):
                return JsonResponse({'data': 'non'}, status=404)
            #------------------------------------------------------

            messages.error(request, "Veuillez remplir les champs.")
            return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))
    else:
        return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))


@login_required
@permission_required('vieprofessionnelle.change_parent', raise_exception=True)
def modifier_parent(request):
    global _active_onglet
    _active_onglet = "parent"  # On initialise la variable

    if request.method == "POST":

        try:
            objet_parent = Parent.objects.get(id=request.POST.get('id'))
        except Parent.DoesNotExist:
            messages.error(request, "Ce parent n'existe pas.")
            return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))

        if objet_parent:
            # On format les chaine
            parent_nouveau = request.POST.get("nomprenoms", None)
            parent_nouveau = parent_nouveau.title()

            date_nouveau = request.POST.get("datenaissance", None)
            adresse = request.POST.get("adresse", None)
            contact = request.POST.get("contact", None)
            typeparent = request.POST.get("select_typeparent", None)

            # On effectue la modification
            objet_parent.nomprenoms = parent_nouveau
            objet_parent.datenaissance = date_nouveau
            objet_parent.adresse = adresse
            objet_parent.contact = contact
            if not objet_parent.dateenre:
                objet_parent.dateenre = datetime.now()
            objet_parent.typeparent = TypeParent.objects.get(id=typeparent)
            objet_parent.save()

            messages.success(request, "Modification réussie.")

            return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))
    else:
        return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))


@login_required
@permission_required('vieprofessionnelle.delete_parent', raise_exception=True)
def supprimer_parent(request, id):
    global _active_onglet
    _active_onglet = "parent"  # On initialise la variable

    try:
        objet_parent = Parent.objects.get(id=id)
    except Parent.DoesNotExist:
        messages.error(request, "Ce parent n'existe pas.")
        return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))

    if objet_parent:
        objet_parent.delete()
        messages.info(request, "Suppression réussie.")

    return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))
# Fin de la Gestion du parent -------------------------------------

# Gestion du type d'etat de santé -----------------------------------------------
@login_required
@permission_required('vieprofessionnelle.add_typeetatsante', raise_exception=True)
def ajouter_typeetatsante(request):
    global _active_onglet
    _active_onglet = "typeetatsante"  # On initialise la variable

    if request.method == "POST":
        # On initialise les variables
        libelle = request.POST.get("libelle", None)

        if libelle:  # On vérifie si le champ a été renseigné

            # On format les chaines
            libelle = libelle.capitalize()

            try:
                objet_typeetatsante = TypeEtatSante.objects.get(libelle=libelle)
                messages.error(request, f"Ce type d'état de santé :[{libelle}] existe déjà.")
                return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))

            except TypeEtatSante.DoesNotExist:
                pass

            # ----
            objet_typeetatsante = TypeEtatSante()
            objet_typeetatsante.libelle = libelle
            objet_typeetatsante.save()

            messages.success(request, "Enregistrement réussi.")

            return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))
    else:
        return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))


@login_required
@permission_required('vieprofessionnelle.change_typeetatsante', raise_exception=True)
def modifier_typeetatsante(request):
    global _active_onglet
    _active_onglet = "typeetatsante"  # On initialise la variable

    if request.method == "POST":

        try:
            objet_typeetatsante = TypeEtatSante.objects.get(id=request.POST.get('id'))
        except TypeEtatSante.DoesNotExist:
            messages.error(request, "Ce type d'état de santé n'existe pas.")
            return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))

        if objet_typeetatsante:
            # On format les chaine
            libelle_nouveau = request.POST.get("libelle", None)
            libelle_nouveau = libelle_nouveau.capitalize()

            # On récupère l'ancienne valeur
            libelle_ancien = objet_typeetatsante.libelle

            # On vérifie si la valeur a changé
            if libelle_nouveau != libelle_ancien:
                # On vérifie si le valeur modifié existe déjà
                try:
                    TypeEtatSante.objects.get(libelle=libelle_nouveau)
                    messages.error(request, f"Ce type d'état de santé [{libelle_nouveau}] existe déjà.")
                    return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))

                except TypeEtatSante.DoesNotExist:
                    pass

            # On effectue la modification
            objet_typeetatsante.libelle = libelle_nouveau
            objet_typeetatsante.save()

            messages.success(request, "Modification réussie.")

            return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))
    else:
        return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))


@login_required
@permission_required('vieprofessionnelle.delete_typeetatsante', raise_exception=True)
def supprimer_typeetatsante(request, id):
    global _active_onglet
    _active_onglet = "typeetatsante"  # On initialise la variable

    try:
        objet_typeetatsante = TypeEtatSante.objects.get(id=id)
    except TypeEtatSante.DoesNotExist:
        messages.error(request, "Ce type d'éta de santé n'existe pas.")
        return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))

    if objet_typeetatsante:
        objet_typeetatsante.delete()
        messages.info(request, "Suppression réussie.")

    return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))
# Fin de la Gestion du type d'etat de santé -------------------------------------

# Gestion du type de document -----------------------------------------------
@login_required
@permission_required('vieprofessionnelle.add_typedocument', raise_exception=True)
def ajouter_typedocument(request):
    global _active_onglet
    _active_onglet = "typedocument"  # On initialise la variable

    if request.method == "POST":
        # On initialise les variables
        libelle = request.POST.get("libelle", None)

        if libelle:  # On vérifie si le champ a été renseigné

            # On format les chaines
            libelle = libelle.capitalize()

            try:
                objet_typedocument = TypeDocument.objects.get(libelle=libelle)
                messages.error(request, f"Ce type de document :[{libelle}] existe déjà.")
                return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))

            except TypeDocument.DoesNotExist:
                pass

            # ----
            objet_typedocument = TypeDocument()
            objet_typedocument.libelle = libelle
            objet_typedocument.save()

            messages.success(request, "Enregistrement réussi.")

            return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))
    else:
        return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))


@login_required
@permission_required('vieprofessionnelle.change_typedocument', raise_exception=True)
def modifier_typedocument(request):
    global _active_onglet
    _active_onglet = "typedocument"  # On initialise la variable

    if request.method == "POST":

        try:
            objet_typedocument = TypeDocument.objects.get(id=request.POST.get('id'))
        except TypeDocument.DoesNotExist:
            messages.error(request, "Ce type de document n'existe pas.")
            return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))

        if objet_typedocument:
            # On format les chaine
            libelle_nouveau = request.POST.get("libelle", None)
            libelle_nouveau = libelle_nouveau.capitalize()

            # On récupère l'ancienne valeur
            libelle_ancien = objet_typedocument.libelle

            # On vérifie si la valeur a changé
            if libelle_nouveau != libelle_ancien:
                # On vérifie si le valeur modifié existe déjà
                try:
                    TypeDocument.objects.get(libelle=libelle_nouveau)
                    messages.error(request, f"Ce type de document[{libelle_nouveau}] existe déjà.")
                    return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))

                except TypeDocument.DoesNotExist:
                    pass

            # On effectue la modification
            objet_typedocument.libelle = libelle_nouveau
            objet_typedocument.save()

            messages.success(request, "Modification réussie.")

            return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))
    else:
        return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))


@login_required
@permission_required('vieprofessionnelle.delete_typedocument', raise_exception=True)
def supprimer_typedocument(request, id):
    global _active_onglet
    _active_onglet = "typedocument"  # On initialise la variable

    try:
        objet_typedocument = TypeDocument.objects.get(id=id)
    except TypeDocument.DoesNotExist:
        messages.error(request, "Ce type de document n'existe pas.")
        return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))

    if objet_typedocument:
        objet_typedocument.delete()
        messages.info(request, "Suppression réussie.")

    return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))
# Fin de la Gestion du type de document -------------------------------------


# Gestion du document -----------------------------------------------
@login_required
@permission_required('vieprofessionnelle.add_document', raise_exception=True)
def ajouter_document(request):
    global _active_onglet
    _active_onglet = "document"  # On initialise la variable

    if request.method == "POST":
        # On initialise les variables
        membre = request.POST.get("select_membre", None)
        typedocument = request.POST.get("select_typedocument", None)
        dateenre = request.POST.get("dateenre", None)

        if membre and typedocument:  # On vérifie si le champ a été renseigné
            if len(request.FILES) != 0:
                photo = request.FILES["photo"]
            else:
                photo = "armoirie.png"

            if not dateenre:
                dateenre = None

            membre = Membre.objects.get(id=membre)
            typedocument = TypeDocument.objects.get(id=typedocument)
        else:
            messages.error(request, f"Veuillez renseigner les champs.")
            return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))

        # ----
        objet_document = Document()
        objet_document.membre = membre
        objet_document.typedocument = typedocument
        objet_document.dateenre = dateenre
        objet_document.photo = photo
        objet_document.save()

        messages.success(request, "Enregistrement réussi.")

        return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))
    else:
        return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))


@login_required
@permission_required('vieprofessionnelle.change_document', raise_exception=True)
def modifier_document(request):
    global _active_onglet
    _active_onglet = "document"  # On initialise la variable

    if request.method == "POST":

        try:
            objet_document = Document.objects.get(id=request.POST.get('id'))
        except Document.DoesNotExist:
            messages.error(request, "Ce document n'existe pas.")
            return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))

        if objet_document:
            membre = request.POST.get("select_membre", None)
            typedocument = request.POST.get("select_typedocument", None)
            dateenre = request.POST.get("dateenre", None)

            if membre and typedocument:  # On vérifie si le champ a été renseigné
                if len(request.FILES) != 0:
                    photo = request.FILES["photo"]
                else:
                    photo = ""

                if not dateenre:
                    dateenre = None

                membre = Membre.objects.get(id=membre)
                typedocument = TypeDocument.objects.get(id=typedocument)
            else:
                messages.error(request, f"Veuillez renseigner les champs.")
                return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))

            # ----
            objet_document.membre = membre
            objet_document.typedocument = typedocument
            objet_document.dateenre = dateenre
            if len(photo) > 0:
                try:
                    if objet_document.photo.size > 0:
                        os.remove(objet_document.photo.path)
                except FileNotFoundError:
                    pass
                objet_document.photo = photo
            objet_document.save()

            messages.success(request, "Modification réussie.")

            return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))
    else:
        return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))


@login_required
@permission_required('vieprofessionnelle.delete_document', raise_exception=True)
def supprimer_document(request, id):
    global _active_onglet
    _active_onglet = "document"  # On initialise la variable

    try:
        objet_document = Document.objects.get(id=id)
    except Document.DoesNotExist:
        messages.error(request, "Ce document n'existe pas.")
        return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))

    if objet_document:
        try:
            if objet_document.photo.size > 0:
                os.remove(objet_document.photo.path)
                objet_document.delete()
        except FileNotFoundError:
            messages.error(request, "Le fichier à supprimer n'existe pas.")
            return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))

        messages.info(request, "Suppression réussie.")

    return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))
# Fin de la Gestion du document -------------------------------------

# Gestion de la Coopérative -----------------------------------------------
@login_required
@permission_required('vieprofessionnelle.add_secteuragricole', raise_exception=True)
def ajouter_cooperative(request):
    if request.method == 'POST':
        if request.POST.get('id_json', None):

            nom_cooperative = request.POST.get('nom_cooperative', None)
            presidente = request.POST.get('presidente', None)
            contact_presidente = request.POST.get('contact_presidente', None)
            speculation_agricole = request.POST.get('speculation_agricole', None)
            superficie_en_culture = request.POST.get('superficie_en_culture', None)
            superficie_en_production = request.POST.get('superficie_en_production', None)
            gps_longitude = request.POST.get('gps_longitude', None)
            gps_latitude = request.POST.get('gps_latitude', None)
            dateenre = request.POST.get('dateenre', None)


            if nom_cooperative: #On vérifie si la champ a été saisi

                nom_cooperative = nom_cooperative.capitalize() # On formate la variable

                # On vérifie si ce Secteur Agricole existe déjà
                try:
                    SecteurAgricole.objects.get(nom=nom_cooperative)
                    return JsonResponse({'data': 'Cette coopérative existe déjà.'}, status=400)
                except SecteurAgricole.DoesNotExist:
                    pass


                #On Ajoute un nouveau Secteur Agricole
                secteur_agricole = SecteurAgricole()

                secteur_agricole.nom = nom_cooperative
                secteur_agricole.presidente = presidente.title()
                secteur_agricole.contact = contact_presidente
                secteur_agricole.speculation_agricole = speculation_agricole
                secteur_agricole.superficie_en_culture = superficie_en_culture
                secteur_agricole.superficie_en_production = superficie_en_production
                secteur_agricole.gps_longitude = gps_longitude
                secteur_agricole.gps_latitude = gps_latitude
                secteur_agricole.dateenre = dateenre
                #secteur_agricole.date_adhesion = None

                secteur_agricole.save()

                data = {
                    'id': secteur_agricole.id,
                    'cooperative': secteur_agricole.nom,
                    'message': "Enregistrement réussi",
                }

                return JsonResponse({'data': data}, status=200)
            else:
                return JsonResponse({'data': 'non'}, status=404)

        else:
            return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))

    return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))

# Fin de la Gestion de la Coopérative -------------------------------------