from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required, permission_required
from django.http import JsonResponse
import os
from datetime import datetime
from django.utils.html import strip_tags
from utilisateur.models import Parametre


# Les constatntes et les variables globales
_active_onglet = ""  # Variable globale pour l'activation des onglets

@login_required
@permission_required('vieprofessionnelle.view_membre', raise_exception=True)
def vieprofessionnelle(request):
    typesecteurs = TypeSecteur.objects.order_by("type")
    secteurs = Secteur.objects.order_by("secteur")
    typeparents = TypeParent.objects.order_by("libelle")
    parents = Parent.objects.order_by("nomprenoms")
    typeetatsantes = TypeEtatSante.objects.order_by("libelle")
    typedocuments = TypeDocument.objects.order_by("libelle")
    documents = Document.objects.order_by("-id")
    chapeaux = Chapeau.objects.order_by("-id")
    typepersonneressources = TypePersonneRessource.objects.order_by("-id")
    personneressources = PersonneRessource.objects.order_by("-id")
    membres = Membre.objects.filter(actif=True).order_by("nom_prenoms")
    typeresponsabilites = TypeResponsabilite.objects.order_by("-id")
    montantfinancements = MontantFinancement.objects.order_by("montant")
    quantitegroupements = QuantiteGroupement.objects.order_by("quantite")

    # Initialisation de l'affichage de l'onglet active
    active_typesecteur = ['', 'false', '']
    active_secteur = ['', 'false', '']
    active_typeparent = ['', 'false', '']
    active_parent = ['', 'false', '']
    active_typeetatsante = ['', 'false', '']
    active_typedocument = ['', 'false', '']
    active_document = ['', 'false', '']
    active_chapeau = ['', 'false', '']
    active_typepersonneressource = ['', 'false', '']
    active_personneressource = ['', 'false', '']
    active_typeresponsabilite = ['', 'false', '']
    active_montantfinancement = ['', 'false', '']
    active_quantitegroupement = ['', 'false', '']

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
    elif _active_onglet == "chapeau":
        active_chapeau = ['active', 'true', 'show active']
    elif _active_onglet == "typepersonneressource":
        active_typepersonneressource = ['active', 'true', 'show active']
    elif _active_onglet == "personneressource":
        active_personneressource = ['active', 'true', 'show active']
    elif _active_onglet == "typeresponsabilite":
        active_typeresponsabilite = ['active', 'true', 'show active']
    elif _active_onglet == "montantfinancement":
        active_montantfinancement = ['active', 'true', 'show active']
    elif _active_onglet == "quantitegroupement":
        active_quantitegroupement = ['active', 'true', 'show active']
    else:
        # Affichage par d??faut
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
        "chapeaux": chapeaux,
        "typepersonneressources": typepersonneressources,
        "personneressources": personneressources,
        "id_chapeau": int(Parametre.objects.first().id_chapeau),
        "monnaie": Parametre.objects.first().monnaie,
        "typeresponsabilites": typeresponsabilites,
        "montantfinancements": montantfinancements,
        "quantitegroupements": quantitegroupements,

        "active_typesecteur": active_typesecteur,
        "active_secteur": active_secteur,
        "active_typeparent": active_typeparent,
        "active_parent": active_parent,
        "active_typeetatsante": active_typeetatsante,
        "active_typedocument": active_typedocument,
        "active_document": active_document,
        "active_chapeau": active_chapeau,
        "active_typepersonneressource": active_typepersonneressource,
        "active_personneressource": active_personneressource,
        "active_typeresponsabilite": active_typeresponsabilite,
        "active_montantfinancement": active_montantfinancement,
        "active_quantitegroupement": active_quantitegroupement,

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

        if type:  # On v??rifie si les champs ont ??t?? renseign??s

            # On format les chaines
            type = type.upper()

            try:
                objet_typesecteur = TypeSecteur.objects.get(type=type)
                messages.error(request, f"Ce type :[{type}] existe d??j??.")
                return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))

            except TypeSecteur.DoesNotExist:
                pass

            # ----
            objet_typesecteur = TypeSecteur()
            objet_typesecteur.type = type
            objet_typesecteur.save()

            messages.success(request, "Enregistrement r??ussi.")

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

            # On r??cup??re l'ancienne valeur
            type_ancien = objet_typesecteur.type

            # On v??rifie si la valeur a chang??
            if type_nouveau != type_ancien:
                # On v??rifie si le valeur modifi?? existe d??j??
                try:
                    TypeSecteur.objects.get(type=type_nouveau)
                    messages.error(request, f"Ce type de secteur [{type_nouveau}] existe d??j??.")
                    return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))

                except TypeSecteur.DoesNotExist:
                    pass

            # On effectue la modification
            objet_typesecteur.type = type_nouveau
            objet_typesecteur.save()

            messages.success(request, "Modification r??ussie.")

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
        messages.info(request, "Suppression r??ussie.")

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

        if secteur and typesecteur:  # On v??rifie si les champs ont ??t?? renseign??s

            # On format les chaines
            secteur = secteur.capitalize()

            try:
                objet_secteur = Secteur.objects.get(secteur=secteur)
                messages.error(request, f"Ce secteur :[{secteur}] existe d??j??.")
                return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))

            except Secteur.DoesNotExist:
                pass

            # ----
            objet_secteur = Secteur()
            objet_secteur.secteur = secteur
            objet_secteur.typesecteur = TypeSecteur.objects.get(id=typesecteur)
            objet_secteur.save()

            messages.success(request, "Enregistrement r??ussi.")

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

            # On r??cup??re l'ancienne valeur
            secteur_ancien = objet_secteur.secteur

            # On v??rifie si la valeur a chang??
            if secteur_nouveau != secteur_ancien:
                # On v??rifie si le valeur modifi?? existe d??j??
                try:
                    Secteur.objects.get(secteur=secteur_nouveau)
                    messages.error(request, f"Ce secteur [{secteur_nouveau}] existe d??j??.")
                    return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))

                except Secteur.DoesNotExist:
                    pass

            # On effectue la modification
            objet_secteur.secteur = secteur_nouveau
            objet_secteur.typesecteur = TypeSecteur.objects.get(id=typesecteur)
            objet_secteur.save()

            messages.success(request, "Modification r??ussie.")

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
        messages.info(request, "Suppression r??ussie.")

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

@login_required
@permission_required('vieprofessionnelle.add_secteur', raise_exception=True)
def details_activite(request):

    if request.method == "GET":
        id = request.GET.get('id', None)
        ajax_activite = []

        if id:
            _parametre = Parametre.objects.first()

            if int(id) == _parametre.id_secteuragricole:
                ajax_activite = SecteurAgricole.objects.order_by('nom')
            elif int(id) == _parametre.id_secteurfemmeactive:
                ajax_activite = SecteurFemmeActive.objects.order_by('nom')
            else:
                ajax_activite = SecteurInformel.objects.order_by('nom')

            if ajax_activite:
                data = [{'id': activite.id, 'nom': activite.nom} for activite in ajax_activite]

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

        if libelle:  # On v??rifie si le champ a ??t?? renseign??

            # On format les chaines
            libelle = libelle.capitalize()

            try:
                objet_typeparent = TypeParent.objects.get(libelle=libelle)
                messages.error(request, f"Ce type de parent :[{libelle}] existe d??j??.")
                return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))

            except TypeParent.DoesNotExist:
                pass

            # ----
            objet_typeparent = TypeParent()
            objet_typeparent.libelle = libelle
            objet_typeparent.save()

            messages.success(request, "Enregistrement r??ussi.")

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

            # On r??cup??re l'ancienne valeur
            libelle_ancien = objet_typeparent.libelle

            # On v??rifie si la valeur a chang??
            if libelle_nouveau != libelle_ancien:
                # On v??rifie si le valeur modifi?? existe d??j??
                try:
                    TypeParent.objects.get(libelle=libelle_nouveau)
                    messages.error(request, f"Ce type de parent [{libelle_nouveau}] existe d??j??.")
                    return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))

                except TypeParent.DoesNotExist:
                    pass

            # On effectue la modification
            objet_typeparent.libelle = libelle_nouveau
            objet_typeparent.save()

            messages.success(request, "Modification r??ussie.")

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
        messages.info(request, "Suppression r??ussie.")

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

        if nomprenoms and typeparent:  # On v??rifie si les champs ont ??t?? renseign??s

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
                id_membre_parent = request.POST.get("id_membre_parent", None)
                # On ajoute le parent au membre
                try:
                    # On r??cup??re le membre
                    membre = Membre.objects.get(id=id_membre_parent)
                except Membre.DoesNotExist:
                    data = {"libelle": "Ce membre n'existe pas."}
                    return JsonResponse({'data': data}, status=404)

                # On ajoute le parent au membre
                membre.parents.add(objet_parent)

                # On r??cup??re tous les documents du membre
                parents = Parent.objects.filter(membre=membre).order_by('id')

                if parents:
                    data = [{'id': parent.id, 'typeparent': parent.typeparent.libelle.upper(),
                             'id_membre': id_membre_parent, 'nomprenoms': parent.nomprenoms.title(),
                             'contact': parent.contact, 'adresse': parent.adresse,
                             'datenaissance': parent.datenaissance.strftime('%d/%m/%Y')} for parent in parents]

                    return JsonResponse({'data': data}, status=200)
            #------------------------------------------------------

            messages.success(request, "Enregistrement r??ussi.")
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

            messages.success(request, "Modification r??ussie.")

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
        messages.info(request, "Suppression r??ussie.")

    return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))
# Fin de la Gestion du parent -------------------------------------

# Gestion du type d'etat de sant?? -----------------------------------------------
@login_required
@permission_required('vieprofessionnelle.add_typeetatsante', raise_exception=True)
def ajouter_typeetatsante(request):
    global _active_onglet
    _active_onglet = "typeetatsante"  # On initialise la variable

    if request.method == "POST":
        # On initialise les variables
        libelle = request.POST.get("libelle", None)

        if libelle:  # On v??rifie si le champ a ??t?? renseign??

            # On format les chaines
            libelle = libelle.capitalize()

            try:
                objet_typeetatsante = TypeEtatSante.objects.get(libelle=libelle)
                messages.error(request, f"Ce type d'??tat de sant?? :[{libelle}] existe d??j??.")
                return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))

            except TypeEtatSante.DoesNotExist:
                pass

            # ----
            objet_typeetatsante = TypeEtatSante()
            objet_typeetatsante.libelle = libelle
            objet_typeetatsante.save()

            messages.success(request, "Enregistrement r??ussi.")

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
            messages.error(request, "Ce type d'??tat de sant?? n'existe pas.")
            return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))

        if objet_typeetatsante:
            # On format les chaine
            libelle_nouveau = request.POST.get("libelle", None)
            libelle_nouveau = libelle_nouveau.capitalize()

            # On r??cup??re l'ancienne valeur
            libelle_ancien = objet_typeetatsante.libelle

            # On v??rifie si la valeur a chang??
            if libelle_nouveau != libelle_ancien:
                # On v??rifie si le valeur modifi?? existe d??j??
                try:
                    TypeEtatSante.objects.get(libelle=libelle_nouveau)
                    messages.error(request, f"Ce type d'??tat de sant?? [{libelle_nouveau}] existe d??j??.")
                    return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))

                except TypeEtatSante.DoesNotExist:
                    pass

            # On effectue la modification
            objet_typeetatsante.libelle = libelle_nouveau
            objet_typeetatsante.save()

            messages.success(request, "Modification r??ussie.")

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
        messages.error(request, "Ce type d'??ta de sant?? n'existe pas.")
        return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))

    if objet_typeetatsante:
        objet_typeetatsante.delete()
        messages.info(request, "Suppression r??ussie.")

    return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))
# Fin de la Gestion du type d'etat de sant?? -------------------------------------

# Gestion du type de document -----------------------------------------------
@login_required
@permission_required('vieprofessionnelle.add_typedocument', raise_exception=True)
def ajouter_typedocument(request):
    global _active_onglet
    _active_onglet = "typedocument"  # On initialise la variable

    if request.method == "POST":
        # On initialise les variables
        libelle = request.POST.get("libelle", None)

        if libelle:  # On v??rifie si le champ a ??t?? renseign??

            # On format les chaines
            libelle = libelle.capitalize()

            try:
                objet_typedocument = TypeDocument.objects.get(libelle=libelle)
                messages.error(request, f"Ce type de document :[{libelle}] existe d??j??.")
                return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))

            except TypeDocument.DoesNotExist:
                pass

            # ----
            objet_typedocument = TypeDocument()
            objet_typedocument.libelle = libelle
            objet_typedocument.save()

            messages.success(request, "Enregistrement r??ussi.")

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

            # On r??cup??re l'ancienne valeur
            libelle_ancien = objet_typedocument.libelle

            # On v??rifie si la valeur a chang??
            if libelle_nouveau != libelle_ancien:
                # On v??rifie si le valeur modifi?? existe d??j??
                try:
                    TypeDocument.objects.get(libelle=libelle_nouveau)
                    messages.error(request, f"Ce type de document[{libelle_nouveau}] existe d??j??.")
                    return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))

                except TypeDocument.DoesNotExist:
                    pass

            # On effectue la modification
            objet_typedocument.libelle = libelle_nouveau
            objet_typedocument.save()

            messages.success(request, "Modification r??ussie.")

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
        messages.info(request, "Suppression r??ussie.")

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

        if membre and typedocument:  # On v??rifie si le champ a ??t?? renseign??
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

        messages.success(request, "Enregistrement r??ussi.")

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

            if membre and typedocument:  # On v??rifie si le champ a ??t?? renseign??
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

            messages.success(request, "Modification r??ussie.")

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
            messages.error(request, "Le fichier ?? supprimer n'existe pas.")
            return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))

        messages.info(request, "Suppression r??ussie.")

    return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))
# Fin de la Gestion du document -------------------------------------

# Gestion de la Coop??rative -----------------------------------------------
@login_required
@permission_required('vieprofessionnelle.add_secteuragricole', raise_exception=True)
def ajouter_cooperative(request):
    if request.method == 'POST':
        if request.POST.get('id_json', None):

            nom_cooperative = request.POST.get('nom_cooperative', None)
            presidente = request.POST.get('presidente', None)
            contact_presidente = request.POST.get('contact_presidente', None)
            ville = request.POST.get('ville', None)
            dateenre = request.POST.get('dateenre', None)


            if nom_cooperative and ville: #On v??rifie si la champ a ??t?? saisi

                nom_cooperative = nom_cooperative.title() # On formate la variable

                # On v??rifie si ce Secteur Agricole existe d??j??
                try:
                    SecteurAgricole.objects.get(nom=nom_cooperative)
                    return JsonResponse({'data': 'Cette coop??rative existe d??j??.'}, status=400)
                except SecteurAgricole.DoesNotExist:
                    pass


                #On Ajoute un nouveau Secteur Agricole
                secteur_agricole = SecteurAgricole()

                secteur_agricole.nom = nom_cooperative
                secteur_agricole.presidente = presidente.title()
                secteur_agricole.contact = contact_presidente
                secteur_agricole.ville = Ville.objects.get(id=ville)
                secteur_agricole.dateenre = dateenre

                secteur_agricole.save()

                data = {
                    'id': secteur_agricole.id,
                    'cooperative': secteur_agricole.nom,
                    'message': "Enregistrement r??ussi",
                }

                return JsonResponse({'data': data}, status=200)
            else:
                return JsonResponse({'data': 'non'}, status=404)

        else:
            return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))

    return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))

# Fin de la Gestion de la Coop??rative -------------------------------------

# Gestion du Groupement -----------------------------------------------
@login_required
@permission_required('vieprofessionnelle.add_secteurfemmeactive', raise_exception=True)
def ajouter_groupement(request):
    if request.method == 'POST':
        if request.POST.get('id_json', None):

            nom_groupement = strip_tags(request.POST.get('nom_groupement', None)).strip()
            ville = request.POST.get('ville', None)
            marche = request.POST.get('marche', None)
            quantitegroupement = request.POST.get('quantitegroupement', None)
            dateenre = request.POST.get('dateenre', None)


            if nom_groupement and ville and quantitegroupement: #On v??rifie si la champ a ??t?? saisi

                nom_groupement = nom_groupement.title()  # On formate la variable

                # On v??rifie si ce Secteur femme active existe d??j??
                try:
                    quantitegroupement = QuantiteGroupement.objects.get(id=quantitegroupement)
                    SecteurFemmeActive.objects.get(nom=nom_groupement, quantitegroupement=quantitegroupement)
                    return JsonResponse({'data': 'Ce groupement existe d??j??.'}, status=400)
                except SecteurFemmeActive.DoesNotExist:
                    pass

                # On r??cup??re le march?? s'il existe
                if marche:
                    try:
                        marche = Marche.objects.get(id=marche)
                    except Marche.DoesNotExist:
                        marche = None
                else:
                    marche = None

                if not dateenre:
                    dateenre = None

                # On Ajoute un nouveau Secteur Femme active
                secteur_femmeactive = SecteurFemmeActive()

                secteur_femmeactive.nom = nom_groupement
                secteur_femmeactive.presidente = None
                secteur_femmeactive.contact = None
                secteur_femmeactive.ville = Ville.objects.get(id=ville)
                secteur_femmeactive.marche = marche
                secteur_femmeactive.quantitegroupement = quantitegroupement
                secteur_femmeactive.dateenre = dateenre
                secteur_femmeactive.set_identifiant()

                secteur_femmeactive.save()

                data = {
                    'id': secteur_femmeactive.id,
                    'groupement': secteur_femmeactive.nom,
                    'message': "Enregistrement r??ussi",
                }

                return JsonResponse({'data': data}, status=200)
            else:
                return JsonResponse({'data': 'non'}, status=404)

        else:
            return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))

    return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))

# Fin de la Gestion du Groupement -------------------------------------

# Gestion du type de document -----------------------------------------------
@login_required
@permission_required('vieprofessionnelle.add_chapeau', raise_exception=True)
def ajouter_chapeau(request):
    global _active_onglet
    _active_onglet = "chapeau"  # On initialise la variable

    if request.method == "POST":
        # On initialise les variables
        chapeau = strip_tags(request.POST.get("chapeau", "")).strip()
        nom = strip_tags(request.POST.get("nom", "")).strip()
        contact = strip_tags(request.POST.get("contact", "")).strip()

        if chapeau and nom and contact:  # On v??rifie si le champ a ??t?? renseign??

            # On format les chaines
            chapeau = chapeau.title()
            nom = nom.title()

            try:
                objet_chapeau = Chapeau.objects.get(chapeau=chapeau)
                messages.error(request, f"Ce chapeau :[{chapeau}] existe d??j??.")
                return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))

            except Chapeau.DoesNotExist:
                pass

            # ----
            objet_chapeau = Chapeau()
            objet_chapeau.chapeau = chapeau
            objet_chapeau.nom = nom
            objet_chapeau.contact = contact
            objet_chapeau.save()

            messages.success(request, "Enregistrement r??ussi.")

            return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))
    else:
        return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))


@login_required
@permission_required('vieprofessionnelle.change_chapeau', raise_exception=True)
def modifier_chapeau(request):
    global _active_onglet
    _active_onglet = "chapeau"  # On initialise la variable

    if request.method == "POST":

        try:
            objet_chapeau = Chapeau.objects.get(id=request.POST.get('id'))
        except Chapeau.DoesNotExist:
            messages.error(request, "Ce chapeau n'existe pas.")
            return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))

        if objet_chapeau:
            # On formate les chaines
            chapeau_nouveau = strip_tags(request.POST.get("chapeau", "")).strip()
            chapeau_nouveau = chapeau_nouveau.title()

            nom = strip_tags(request.POST.get("nom", "")).strip()
            nom = nom.title()

            contact = strip_tags(request.POST.get("contact", "")).strip()

            # On r??cup??re l'ancienne valeur
            chapeau_ancien = objet_chapeau.chapeau

            # On v??rifie si la valeur a chang??
            if chapeau_nouveau != chapeau_ancien:
                # On v??rifie si la valeur modifi??e existe d??j??
                try:
                    Chapeau.objects.get(chapeau=chapeau_nouveau)
                    messages.error(request, f"Ce chapeau [{chapeau_nouveau}] existe d??j??.")
                    return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))

                except Chapeau.DoesNotExist:
                    pass

            # On effectue la modification
            objet_chapeau.chapeau = chapeau_nouveau
            objet_chapeau.nom = nom
            objet_chapeau.contact = contact
            objet_chapeau.save()

            messages.success(request, "Modification r??ussie.")

            return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))
    else:
        return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))


@login_required
@permission_required('vieprofessionnelle.delete_chapeau', raise_exception=True)
def supprimer_chapeau(request, id):
    global _active_onglet
    _active_onglet = "chapeau"  # On initialise la variable

    try:
        objet_chapeau = Chapeau.objects.get(id=id)
    except Chapeau.DoesNotExist:
        messages.error(request, "Ce chapeau n'existe pas.")
        return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))

    if objet_chapeau:
        objet_chapeau.delete()
        messages.info(request, "Suppression r??ussie.")

    return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))
# Fin de la Gestion du type de document -------------------------------------

# Gestion du type de personne ressource -----------------------------------------------
@login_required
@permission_required('vieprofessionnelle.add_typepersonneressource', raise_exception=True)
def ajouter_typepersonneressource(request):
    global _active_onglet
    _active_onglet = "typepersonneressource"  # On initialise la variable

    if request.method == "POST":
        # On initialise les variables
        type = strip_tags(request.POST.get("type", "")).strip()

        if type:  # On v??rifie si le champ a ??t?? renseign??

            # On formate les chaines
            type = type.capitalize()

            try:
                TypePersonneRessource.objects.get(type=type)
                messages.error(request, f"Ce type de presonne ressource :[{type}] existe d??j??.")
                return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))

            except TypePersonneRessource.DoesNotExist:
                pass

            # ----
            objet_typepersonneressource = TypePersonneRessource()
            objet_typepersonneressource.type = type
            objet_typepersonneressource.save()

            messages.success(request, "Enregistrement r??ussi.")

            return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))
    else:
        return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))


@login_required
@permission_required('vieprofessionnelle.change_typepersonneressource', raise_exception=True)
def modifier_typepersonneressource(request):
    global _active_onglet
    _active_onglet = "typepersonneressource"  # On initialise la variable

    if request.method == "POST":

        try:
            objet_typepersonneressource = TypePersonneRessource.objects.get(id=request.POST.get('id'))
        except TypePersonneRessource.DoesNotExist:
            messages.error(request, "Ce type de personne ressource n'existe pas.")
            return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))

        if objet_typepersonneressource:
            # On formate les chaines
            type_nouveau = strip_tags(request.POST.get("type", "")).strip()
            type_nouveau = type_nouveau.capitalize()

            # On r??cup??re l'ancienne valeur
            type_ancien = objet_typepersonneressource.type

            # On v??rifie si la valeur a chang??
            if type_nouveau != type_ancien:
                # On v??rifie si la valeur modifi??e existe d??j??
                try:
                    TypePersonneRessource.objects.get(type=type_nouveau)
                    messages.error(request, f"Ce type de personne ressource [{type_nouveau}] existe d??j??.")
                    return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))

                except TypePersonneRessource.DoesNotExist:
                    pass

            # On effectue la modification
            objet_typepersonneressource.type = type_nouveau
            objet_typepersonneressource.save()

            messages.success(request, "Modification r??ussie.")

            return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))
    else:
        return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))


@login_required
@permission_required('vieprofessionnelle.delete_typepersonneressource', raise_exception=True)
def supprimer_typepersonneressource(request, id):
    global _active_onglet
    _active_onglet = "typepersonneressource"  # On initialise la variable

    try:
        objet_typepersonneressource = TypePersonneRessource.objects.get(id=id)
    except TypePersonneRessource.DoesNotExist:
        messages.error(request, "Ce type de personne ressource n'existe pas.")
        return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))

    if objet_typepersonneressource:
        objet_typepersonneressource.delete()
        messages.info(request, "Suppression r??ussie.")

    return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))
# Fin de la Gestion du type de personne ressource -------------------------------------


# Gestion de personne ressource -----------------------------------------------
@login_required
@permission_required('vieprofessionnelle.add_personneressource', raise_exception=True)
def ajouter_personneressource(request):
    if request.method == "GET":
        # On initialise les variables
        typepersonneressource = request.GET.get("typepersonneressource", None)
        id = request.GET.get("id", None)
        _parametre = Parametre.objects.first()

        if typepersonneressource and id:  # On v??rifie si les champs ont ??t?? renseign??s

            try:
                # On r??cup??re le type de personne ressource
                object_typepersonneressource = TypePersonneRessource.objects.get(id=typepersonneressource)
            except TypePersonneRessource.DoesNotExist:
                data = {"libelle": "Ce type de personne ressource n'existe pas."}
                return JsonResponse({'data': data}, status=404)

            if int(_parametre.id_chapeau) == int(typepersonneressource):

                try:
                    # On r??cup??re le membre
                    objet_chapeau = Chapeau.objects.get(id=id)
                    # On v??rifie si ce chapeau existe d??j?? en tant que personne ressource
                    try:
                        PersonneRessource.objects.get(chapeau=objet_chapeau.id)
                        data = {"libelle": "Ce Chapeau existe d??j??."}
                        return JsonResponse({'data': data}, status=403)
                    except PersonneRessource.DoesNotExist:
                        pass
                    objet_membre = None
                except Chapeau.DoesNotExist:
                    data = {"libelle": "Ce Chapeau n'existe pas."}
                    return JsonResponse({'data': data}, status=404)
            else:
                try:
                    # On r??cup??re le membre
                    objet_membre = Membre.objects.get(id=id)
                    try:
                        PersonneRessource.objects.get(membre=objet_membre.id)
                        data = {"libelle": "Ce Membre existe d??j??."}
                        return JsonResponse({'data': data}, status=403)
                    except PersonneRessource.DoesNotExist:
                        pass
                    objet_chapeau = None
                except Membre.DoesNotExist:
                    data = {"libelle": "Ce Membre n'existe pas."}
                    return JsonResponse({'data': data}, status=404)
            # On ajoute les donn??es
            objet_personneressource = PersonneRessource()
            objet_personneressource.typepersonneressource = object_typepersonneressource
            objet_personneressource.membre = objet_membre
            objet_personneressource.chapeau = objet_chapeau
            objet_personneressource.save()

            # On r??cup??re toutes les personnes ressources
            personneressources = PersonneRessource.objects.order_by('-id')

            if personneressources:
                data = []
                for personne in personneressources:
                    if personne.chapeau:
                        data.append(
                            {
                                'id': personne.id,
                                'type': personne.typepersonneressource.type,
                                'nom': personne.chapeau.chapeau,
                                'contact': personne.chapeau.contact,
                            }

                        )
                    else:
                        data.append(
                            {
                                'id': personne.id,
                                'type': personne.typepersonneressource.type,
                                'nom': personne.membre.nom_prenoms,
                                'contact': personne.membre.contact,
                            }

                        )

                return JsonResponse({'data': data}, status=200)

        else:
            data = {"libelle": "Toutes les donn??es n'ont pas ??t?? re??ues"}
            return JsonResponse({'data': data}, status=404)
    else:
        return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))


@login_required
@permission_required('vieprofessionnelle.delete_personneressource', raise_exception=True)
def supprimer_personneressource(request):
    if request.method == "GET":
        supprimer_p = request.GET.get('supprimer_p', None)

        if supprimer_p:

            try:
                # On r??cup??re la personne ressource
                personneressource = PersonneRessource.objects.get(id=supprimer_p)
            except PersonneRessource.DoesNotExist:
                data = {"libelle": "Cette personne ressource n'existe pas."}
                return JsonResponse({'data': data}, status=404)

            # Les donn??es sont bonnes, on ajoute le secteur au membre
            if personneressource:
                personneressource.delete()

                # On r??cup??re toutes les personnes ressources
                personneressources = PersonneRessource.objects.order_by('-id')

                if personneressources:
                    data = []
                    for personne in personneressources:
                        if personne.chapeau:
                            data.append(
                                {
                                    'id': personne.id,
                                    'type': personne.typepersonneressource.type,
                                    'nom': personne.chapeau.chapeau,
                                    'contact': personne.chapeau.contact,
                                }

                            )
                        else:
                            data.append(
                                {
                                    'id': personne.id,
                                    'type': personne.typepersonneressource.type,
                                    'nom': personne.membre.nom_prenoms,
                                    'contact': personne.membre.contact,
                                }

                            )

                    return JsonResponse({'data': data}, status=200)

        else:
            data = {"libelle": "Veuillez renseigner les champs"}
            return JsonResponse({'data': data}, status=404)

    return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))


@login_required
@permission_required('vieprofessionnelle.add_personneressource', raise_exception=True)
def details_personneressource(request):
    if request.method == "GET":
        id = request.GET.get('id', None)
        _parametre = Parametre.objects.first()

        if id:
            if id == _parametre.id_chapeau:
                ajax_chapeau = Chapeau.objects.order_by('-id')
                if ajax_chapeau:
                    data = [{'id': chapeau.id, 'nom': chapeau.chapeau, 'contact': chapeau.contact} for chapeau in
                            ajax_chapeau]

                    return JsonResponse({'data': data}, status=200)
            else:
                ajax_membre = Membre.objects.order_by('-id')
                if ajax_membre:
                    data = [{'id': membre.id, 'nom': membre.nom_prenoms, 'contact': membre.contact} for membre in
                            ajax_membre]

                    return JsonResponse({'data': data}, status=200)

    return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))

# Fin de la Gestion de personne ressource -------------------------------------

# Gestion du type de responsabilit?? -----------------------------------------------
@login_required
@permission_required('vieprofessionnelle.add_typeresponsabilite', raise_exception=True)
def ajouter_typeresponsabilite(request):
    global _active_onglet
    _active_onglet = "typeresponsabilite"  # On initialise la variable

    if request.method == "POST":
        # On initialise les variables
        type = strip_tags(request.POST.get("type", "")).strip()

        if type:  # On v??rifie si le champ a ??t?? renseign??

            # On formate les chaines
            type = type.capitalize()

            try:
                TypeResponsabilite.objects.get(type=type)
                messages.error(request, f"Ce type de responsabilit?? :[{type}] existe d??j??.")
                return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))

            except TypeResponsabilite.DoesNotExist:
                pass

            # ----
            objet_typeresponsabilite = TypeResponsabilite()
            objet_typeresponsabilite.type = type
            objet_typeresponsabilite.save()

            messages.success(request, "Enregistrement r??ussi.")

            return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))
    else:
        return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))


@login_required
@permission_required('vieprofessionnelle.change_typeresponsabilite', raise_exception=True)
def modifier_typeresponsabilite(request):
    global _active_onglet
    _active_onglet = "typeresponsabilite"  # On initialise la variable

    if request.method == "POST":

        try:
            objet_typeresponsabilite = TypeResponsabilite.objects.get(id=request.POST.get('id'))
        except TypeResponsabilite.DoesNotExist:
            messages.error(request, "Ce type de responsabilit?? n'existe pas.")
            return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))

        if objet_typeresponsabilite:
            # On formate les chaines
            type_nouveau = strip_tags(request.POST.get("type", "")).strip()
            type_nouveau = type_nouveau.capitalize()

            # On r??cup??re l'ancienne valeur
            type_ancien = objet_typeresponsabilite.type

            # On v??rifie si la valeur a chang??
            if type_nouveau != type_ancien:
                # On v??rifie si la valeur modifi??e existe d??j??
                try:
                    TypeResponsabilite.objects.get(type=type_nouveau)
                    messages.error(request, f"Ce type de responsabilit?? [{type_nouveau}] existe d??j??.")
                    return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))

                except TypeResponsabilite.DoesNotExist:
                    pass

            # On effectue la modification
            objet_typeresponsabilite.type = type_nouveau
            objet_typeresponsabilite.save()

            messages.success(request, "Modification r??ussie.")

            return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))
    else:
        return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))


@login_required
@permission_required('vieprofessionnelle.delete_typeresponsabilite', raise_exception=True)
def supprimer_typeresponsabilite(request, id):
    global _active_onglet
    _active_onglet = "typeresponsabilite"  # On initialise la variable

    try:
        objet_typeresponsabilite = TypeResponsabilite.objects.get(id=id)
    except TypeResponsabilite.DoesNotExist:
        messages.error(request, "Ce type de responsabilit?? n'existe pas.")
        return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))

    if objet_typeresponsabilite:
        objet_typeresponsabilite.delete()
        messages.info(request, "Suppression r??ussie.")

    return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))
# Fin de la Gestion du type de responsabilit?? -------------------------------------

# Gestion du montant du financement -----------------------------------------------
@login_required
@permission_required('vieprofessionnelle.add_montantfinancement', raise_exception=True)
def ajouter_montantfinancement(request):
    global _active_onglet
    _active_onglet = "montantfinancement"  # On initialise la variable

    if request.method == "POST":
        # On initialise les variables
        montant = strip_tags(request.POST.get("montant", 0)).strip()

        if montant != '0':  # On v??rifie si le champ a ??t?? renseign??

            try:
                MontantFinancement.objects.get(montant=montant)
                messages.error(request, f"Ce montant :[{montant}] existe d??j??.")
                return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))

            except MontantFinancement.DoesNotExist:
                pass

            # ----
            objet_montantfinancement = MontantFinancement()
            objet_montantfinancement.montant = montant
            objet_montantfinancement.save()

            messages.success(request, "Enregistrement r??ussi.")

            return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))
        else:
            messages.error(request, f"Entrer un montant sup??rieur ?? {montant}.")

            return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))
    else:
        return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))


@login_required
@permission_required('vieprofessionnelle.change_montantfinancement', raise_exception=True)
def modifier_montantfinancement(request):
    global _active_onglet
    _active_onglet = "montantfinancement"  # On initialise la variable

    if request.method == "POST":

        try:
            objet_montantfinancement = MontantFinancement.objects.get(id=request.POST.get('id'))
        except MontantFinancement.DoesNotExist:
            messages.error(request, "Ce montant n'existe pas.")
            return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))

        if objet_montantfinancement:
            # On formate les chaines
            montant_nouveau = strip_tags(request.POST.get("montant", 0)).strip()

            # On r??cup??re l'ancienne valeur
            montant_ancien = objet_montantfinancement.montant

            # On v??rifie si la valeur a chang??
            if montant_nouveau != montant_ancien:
                # On v??rifie si la valeur modifi??e existe d??j??
                try:
                    MontantFinancement.objects.get(montant=montant_nouveau)
                    messages.error(request, f"Ce montant [{montant_nouveau}] existe d??j??.")
                    return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))

                except MontantFinancement.DoesNotExist:
                    pass

            # On effectue la modification
            objet_montantfinancement.montant = montant_nouveau
            objet_montantfinancement.save()

            messages.success(request, "Modification r??ussie.")

            return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))
    else:
        return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))


@login_required
@permission_required('vieprofessionnelle.delete_montantfinancement', raise_exception=True)
def supprimer_montantfinancement(request, id):
    global _active_onglet
    _active_onglet = "montantfinancement"  # On initialise la variable

    try:
        objet_montantfinancement = MontantFinancement.objects.get(id=id)
    except MontantFinancement.DoesNotExist:
        messages.error(request, "Ce montant n'existe pas.")
        return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))

    if objet_montantfinancement:
        objet_montantfinancement.delete()
        messages.info(request, "Suppression r??ussie.")

    return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))
# Fin de la Gestion du montant du financement -------------------------------------

# Gestion de la quantit?? du groupement -----------------------------------------------
@login_required
@permission_required('vieprofessionnelle.add_quantitegroupement', raise_exception=True)
def ajouter_quantitegroupement(request):
    global _active_onglet
    _active_onglet = "quantitegroupement"  # On initialise la variable

    if request.method == "POST":
        # On initialise les variables
        quantite = strip_tags(request.POST.get("quantite", 0)).strip()

        if quantite != '0':  # On v??rifie si le champ a ??t?? renseign??

            try:
                QuantiteGroupement.objects.get(quantite=quantite)
                messages.error(request, f"Cette quantit?? :[{quantite}] existe d??j??.")
                return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))

            except QuantiteGroupement.DoesNotExist:
                pass

            # ----
            objet_quantitegroupement = QuantiteGroupement()
            objet_quantitegroupement.quantite = quantite
            objet_quantitegroupement.save()

            messages.success(request, "Enregistrement r??ussi.")

            return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))
        else:
            messages.error(request, f"Entrer une quantit?? sup??rieur ?? {quantite}.")

            return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))
    else:
        return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))


@login_required
@permission_required('vieprofessionnelle.change_quantitegroupement', raise_exception=True)
def modifier_quantitegroupement(request):
    global _active_onglet
    _active_onglet = "quantitegroupement"  # On initialise la variable

    if request.method == "POST":

        try:
            objet_quantitegroupement = QuantiteGroupement.objects.get(id=request.POST.get('id'))
        except QuantiteGroupement.DoesNotExist:
            messages.error(request, "Cette quantit?? n'existe pas.")
            return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))

        if objet_quantitegroupement:
            # On formate les chaines
            quantite_nouveau = strip_tags(request.POST.get("quantite", 0)).strip()

            # On r??cup??re l'ancienne valeur
            quantite_ancien = objet_quantitegroupement.quantite

            # On v??rifie si la valeur a chang??
            if quantite_nouveau != quantite_ancien:
                # On v??rifie si la valeur modifi??e existe d??j??
                try:
                    QuantiteGroupement.objects.get(quantite=quantite_nouveau)
                    messages.error(request, f"Cette quantit?? [{quantite_nouveau}] existe d??j??.")
                    return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))

                except QuantiteGroupement.DoesNotExist:
                    pass

            # On effectue la modification
            objet_quantitegroupement.quantite = quantite_nouveau
            objet_quantitegroupement.save()

            messages.success(request, "Modification r??ussie.")

            return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))
    else:
        return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))


@login_required
@permission_required('vieprofessionnelle.delete_quantitegroupement', raise_exception=True)
def supprimer_quantitegroupement(request, id):
    global _active_onglet
    _active_onglet = "quantitegroupement"  # On initialise la variable

    try:
        objet_quantitegroupement = QuantiteGroupement.objects.get(id=id)
    except QuantiteGroupement.DoesNotExist:
        messages.error(request, "Cette quantit?? n'existe pas.")
        return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))

    if objet_quantitegroupement:
        objet_quantitegroupement.delete()
        messages.info(request, "Suppression r??ussie.")

    return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))
# Fin de la Gestion de la quantit?? du groupement -------------------------------------
