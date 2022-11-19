from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from .models import *
from vieprofessionnelle.models import *
from django.contrib.auth.decorators import login_required, permission_required
from etatcivil.models import TypePiece, Nationalite, Niveau, NiveauScolaire, SituationMatrimoniale
from localisation.models import *
from django.http import JsonResponse
from django.utils.html import strip_tags
import datetime
import os

# Les constatntes et les variables globales
_active_onglet = "" # Variable globale pour l'activation des onglets
_active_session = False # Variable globale pour l'activation des onglets


# Gestion du secteur agricole-----------------------------------------------
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

    # Les variables
    il_existe = True
    global _active_session

    if request.method == "POST":
        # On récupère les données
        sexe = strip_tags(request.POST.get('sexe', None))# On rétire les tag (<>)
        nom = strip_tags(request.POST.get('nom', None)).strip().title() # On rétire les tag (<>) et on enleve les espaces au début et fin
        prenoms = strip_tags(request.POST.get('prenoms', None)).strip().title()
        nomjeunefille = strip_tags(request.POST.get('nomjeunefille', None)).strip().title()
        date_naissance = strip_tags(request.POST.get('date_naissance', None))
        lieu_naissance = strip_tags(request.POST.get('lieu_naissance', None))
        typepiece = strip_tags(request.POST.get('typepiece', None))
        numeropiece = strip_tags(request.POST.get('numeropiece', None)).strip()
        nationalite = strip_tags(request.POST.get('nationalite', None))
        contact = strip_tags(request.POST.get('contact', None)).strip()
        cooperative = strip_tags(request.POST.get('cooperative', None))
        dateadhesion = strip_tags(request.POST.get('dateadhesion', None))
        numero_carte = strip_tags(request.POST.get('numero_carte', None)).strip()
        niveauscolaire = strip_tags(request.POST.get('niveauscolaire', None))
        situationmatrimoniale = strip_tags(request.POST.get('situationmatrimoniale', None))
        lieu_habitation = strip_tags(request.POST.get('lieu_habitation', None))

        if not date_naissance:
            date_naissance = None

        if not dateadhesion:
            dateadhesion = None

        if nom and date_naissance and numeropiece and contact and cooperative and lieu_habitation:
            if not request.session.get('id_membre'): # On traite la modification
                # On vérifie si ce membre existe déjà car le numeropiece et le contact sont uniques
                try:
                    Membre.objects.get(numeropiece=numeropiece, contact=contact)
                    messages.error(request, "Ce membre existe déjà.")
                    il_existe = False
                except Membre.DoesNotExist:
                    objet_membre = Membre()
            else:
                # On vérifie si le membre à modifier existe
                try:
                    objet_membre = Membre.objects.get(id=request.session.get('id_membre'))
                except Membre.DoesNotExist:
                    messages.error(request, "Ce membre n'existe pas.")
                    il_existe = False

            if il_existe: # Si la valeur est True on entre dans la condition
                objet_membre.nom = nom
                objet_membre.prenoms = prenoms
                objet_membre.set_nomprenoms()
                objet_membre.nomjeunefille = nomjeunefille
                objet_membre.sexe = Sexe.objects.get(code=sexe)
                objet_membre.lieunaissance = Commune.objects.get(id=lieu_naissance)
                objet_membre.date_naissance = date_naissance
                objet_membre.typepiece = TypePiece.objects.get(id=typepiece)
                objet_membre.numeropiece = numeropiece
                objet_membre.nationalite = Nationalite.objects.get(id=nationalite)
                objet_membre.contact = contact
                objet_membre.numerobadge = None
                objet_membre.niveauscolaire = NiveauScolaire.objects.get(id=niveauscolaire)
                objet_membre.situationmatrimoniale = SituationMatrimoniale.objects.get(id=situationmatrimoniale)
                objet_membre.quartier = Quartier.objects.get(id=lieu_habitation)

                if not request.session.get('id_membre'):
                    objet_membre.dateenre = datetime.date.today()

                objet_membre.actif = True # On active l'utilisateur
                objet_membre.utilisateur = User.objects.get(id=request.user.id)

                # On sauvegarde les données
                objet_membre.save()

                if not request.session.get('id_membre'):
                    # On ajoute le champ après la sauvegarde pour utiliser l'id
                    objet_membre.set_identifiant()
                    objet_membre.save()

                    # On ajoute le secteur agricole en relation
                    MembreSecteurAgricole.objects.create(
                        membre=objet_membre,
                        secteuragricole=SecteurAgricole.objects.get(id=cooperative),
                        date_adhesion=dateadhesion,
                        numero_carte=numero_carte,
                    )

                    messages.success(request, "Enregistrement réussi")

                else:
                    try:
                        membresecteura = MembreSecteurAgricole.objects.get(membre = objet_membre)
                        membresecteura.secteuragricole = SecteurAgricole.objects.get(id=cooperative)
                        membresecteura.date_adhesion = dateadhesion
                        membresecteura.numero_carte = numero_carte
                        membresecteura.save()

                        messages.success(request, "Modification réussi")
                    except MembreSecteurAgricole.DoesNotExist:
                        pass

                    del request.session['id_membre'] # On détruit la variable

        else:
            messages.error(request, "Veuillez renseigner les champs.")


    # PARTIE DU GET -----------------------
    if not _active_session :
        if request.session.get('id_membre'):
            del request.session['id_membre']

    if _active_session and request.session.get('id_membre'):
        _active_session = False

    typepieces = TypePiece.objects.order_by('id')
    nationalites = Nationalite.objects.order_by('id')
    niveaux = Niveau.objects.order_by('id')
    niveauscolaires = NiveauScolaire.objects.order_by('id')
    situationmatrimoniales = SituationMatrimoniale.objects.order_by('id')
    districts = District.objects.order_by("libelle")
    regions = Region.objects.order_by("libelle")
    departements = Departement.objects.order_by("libelle")
    villes = Ville.objects.order_by("libelle")
    communes = Commune.objects.order_by("libelle")
    secteuragricoles = SecteurAgricole.objects.order_by("nom")
    typeparents = TypeParent.objects.order_by("libelle")
    parents = Parent.objects.order_by("nomprenoms")
    membres = Membre.objects.filter(utilisateur_id=request.user.id, actif=True).order_by('nom_prenoms')

    # Initialisation de l'affichage de l'onglet active
    active_secteuragricole = ['', 'false', '']
    active_liste = ['', 'false', '']

    if _active_onglet == "active_secteuragricole":
        active_secteuragricole = ['active', 'true', 'show active']
    elif _active_onglet == "active_liste":
        active_liste = ['active', 'true', 'show active']
    else:
        # Affichage par défaut
        active_secteuragricole = ['active', 'true', 'show active']


    context = {
        'titre': "Identification - Secteur Agricole",
        'typepieces': typepieces,
        'nationalites': nationalites,
        'niveaux': niveaux,
        'niveauscolaires': niveauscolaires,
        'situationmatrimoniales': situationmatrimoniales,
        "districts": districts,
        "regions": regions,
        "departements": departements,
        "villes": villes,
        "communes": communes,
        "secteuragricoles": secteuragricoles,
        "typeparents": typeparents,
        "parents": parents,
        "membres": membres,

        "active_secteuragricole": active_secteuragricole,
        "active_liste": active_liste,
    }

    if request.session.get('id_membre'): # On affiche la page de modification
        # On récupère le membre
        context["membre_actif"] = Membre.objects.get(id=request.session.get('id_membre'))
        context["membre_secteuragricole"] = MembreSecteurAgricole.objects.get(membre_id=request.session.get('id_membre'))
        return render(request, "presentation/modifier_secteuragricole.html", context)

    return render(request,"presentation/secteuragricole.html", context)


@login_required
@permission_required('vieprofessionnelle.add_membre', raise_exception=True)
def detail_secteuragricole(request, id):
    try:
        membre = Membre.objects.get(id=id)
    except Membre.DoesNotExist:
        messages.error(request, "Ce membre n'existe pas.")
        return HttpResponseRedirect(reverse('presentation:ajouter_secteuragricole'))

    typesecteurs = TypeSecteur.objects.order_by('id')
    secteurs = Secteur.objects.filter(membre=membre).order_by('secteur')

    context = {
        'title': "Détials du membre",
        'membre': membre,
        'typesecteurs': typesecteurs,
        'secteurs': secteurs,
    }
    return render(request, 'presentation/details_secteur_agricole.html', context)


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
@permission_required('vieprofessionnelle.change_membre', raise_exception=True)
def modifier_secteuragricole(request,id):
    global _active_onglet
    global _active_session

    _active_session = True
    _active_onglet = "active_secteuragricole"  # On initialise la variable
    request.session['id_membre'] = id

    return HttpResponseRedirect(reverse('presentation:ajouter_secteuragricole'))

@login_required
@permission_required('vieprofessionnelle.delete_membre', raise_exception=True)
def supprimer_secteuragricole(request, id):
    global _active_onglet
    _active_onglet = "active_liste"  # On initialise la variable

    try:
        objet_membre = Membre.objects.get(id=id)
    except Membre.DoesNotExist:
        messages.error(request, "Ce membre n'existe pas.")
        return HttpResponseRedirect(reverse('presentation:ajouter_secteuragricole'))

    if objet_membre:
        objet_membre.actif = False
        objet_membre.save()

        messages.info(request, "Suppression réussie.")

    return HttpResponseRedirect(reverse('presentation:ajouter_secteuragricole'))

@login_required
@permission_required('vieprofessionnelle.add_membre', raise_exception=True)
def ajouter_secteur_membre(request):
    if request.method == "GET":
        id_membre_secteur = request.GET.get('id_membre_secteur', None)
        select_secteur = request.GET.get('select_secteur', None)

        if id_membre_secteur and select_secteur:
            try:
                # On récupère le membre
                membre = Membre.objects.get(id=id_membre_secteur)
            except Membre.DoesNotExist:
                data = {"libelle": "Ce membre n'existe pas."}
                return JsonResponse({'data': data}, status=404)

            try:
                # On récupère le secteur
                secteur = Secteur.objects.get(id=select_secteur)
            except Secteur.DoesNotExist:
                data = {"libelle": "Ce secteur d'activité n'existe pas."}
                return JsonResponse({'data': data}, status=404)

            # Les données sont bonnes, on ajoute le secteur au membre
            membre.secteurs.add(secteur)

            # On récupère tous les secteurs du membre
            secteurs = Secteur.objects.filter(membre=id_membre_secteur).order_by('secteur')

            if secteurs:
                data = [{'id': secteur.id, 'secteur': secteur.secteur, 'typesecteur': secteur.typesecteur.type, 'id_membre': id_membre_secteur} for secteur in secteurs]

                return JsonResponse({'data': data}, status=200)

        else:
            data = {"libelle":"Veuillez renseigner les champs"}
            return JsonResponse({'data': data}, status=404)

    return HttpResponseRedirect(reverse('presentation:ajouter_secteuragricole'))

@login_required
@permission_required('vieprofessionnelle.delete_membre', raise_exception=True)
def supprimer_secteur_membre(request):
    if request.method == "GET":
        id_membre_secteur_s = request.GET.get('id_membre_secteur_s', None)
        supprimer_s = request.GET.get('supprimer_s', None)

        if id_membre_secteur_s and supprimer_s:
            try:
                # On récupère le membre
                membre = Membre.objects.get(id=id_membre_secteur_s)
            except Membre.DoesNotExist:
                data = {"libelle": "Ce membre n'existe pas."}
                return JsonResponse({'data': data}, status=404)

            try:
                # On récupère le secteur
                secteur = Secteur.objects.get(id=supprimer_s)
            except Secteur.DoesNotExist:
                data = {"libelle": "Ce secteur d'activité n'existe pas."}
                return JsonResponse({'data': data}, status=404)

            # Les données sont bonnes, on ajoute le secteur au membre
            membre.secteurs.remove(secteur)

            # On récupère tous les secteurs du membre
            secteurs = Secteur.objects.filter(membre=id_membre_secteur_s).order_by('secteur')

            if secteurs:
                data = [{'id': secteur.id, 'secteur': secteur.secteur, 'typesecteur': secteur.typesecteur.type, 'id_membre' : id_membre_secteur_s} for secteur in secteurs]

                return JsonResponse({'data': data}, status=200)

        else:
            data = {"libelle": "Veuillez renseigner les champs"}
            return JsonResponse({'data': data}, status=404)

    return HttpResponseRedirect(reverse('presentation:ajouter_secteuragricole'))

@login_required
@permission_required('vieprofessionnelle.delete_membre', raise_exception=True)
def supprimer_membre(request, id):
    pass


# Fin de la Gestion du secteur agricole -------------------------------------
