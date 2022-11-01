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
    typesecteurs = TypeSecteur.objects.all().order_by("type")
    secteurs = Secteur.objects.all().order_by("secteur")

    # Initialisation de l'affichage de l'onglet active
    active_typesecteur = ['', 'false', '']
    active_secteur = ['', 'false', '']

    if _active_onglet == "typesecteur":
        active_typesecteur = ['active', 'true', 'show active']
    elif _active_onglet == "secteur":
        active_secteur = ['active', 'true', 'show active']
    else:
        # Affichage par défaut
        active_typesecteur = ['active', 'true', 'show active']

    context = {
        "titre": "Vie professionnelle",
        "typesecteurs": typesecteurs,
        "secteurs": secteurs,


        "active_typesecteur": active_typesecteur,
        "active_secteur": active_secteur,

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
