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
    typesecteurs = TypeSecteur.objects.order_by("type")
    secteurs = Secteur.objects.order_by("secteur")
    typeparents = TypeParent.objects.order_by("libelle")
    parents = Parent.objects.order_by("nomprenoms")

    # Initialisation de l'affichage de l'onglet active
    active_typesecteur = ['', 'false', '']
    active_secteur = ['', 'false', '']
    active_typeparent = ['', 'false', '']
    active_parent = ['', 'false', '']

    if _active_onglet == "typesecteur":
        active_typesecteur = ['active', 'true', 'show active']
    elif _active_onglet == "secteur":
        active_secteur = ['active', 'true', 'show active']
    elif _active_onglet == "typeparent":
        active_typeparent = ['active', 'true', 'show active']
    elif _active_onglet == "parent":
        active_parent = ['active', 'true', 'show active']
    else:
        # Affichage par défaut
        active_typesecteur = ['active', 'true', 'show active']

    context = {
        "titre": "Vie professionnelle",
        "typesecteurs": typesecteurs,
        "secteurs": secteurs,
        "typeparents": typeparents,
        "parents": parents,


        "active_typesecteur": active_typesecteur,
        "active_secteur": active_secteur,
        "active_typeparent": active_typeparent,
        "active_parent": active_parent,

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
            objet_parent.typeparent = TypeParent.objects.get(id=typeparent)
            objet_parent.save()

            messages.success(request, "Enregistrement réussi.")

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

            typeparent = request.POST.get("select_typeparent", None)

            # On effectue la modification
            objet_parent.nomprenoms = parent_nouveau
            objet_parent.datenaissance = date_nouveau
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
@permission_required('vieprofessionnelle.change_typeetatsante', raise_exception=True)
def modifier_typeetatsante(request):
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
@permission_required('vieprofessionnelle.delete_typeetatsante', raise_exception=True)
def supprimer_typeetatsante(request, id):
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
# Fin de la Gestion du type d'etat de santé -------------------------------------
