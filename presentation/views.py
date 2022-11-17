from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
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

        if nom and date_naissance and numeropiece and contact and cooperative and lieu_habitation:
            # On véruifie si ce membre existe déjà car le numeropiece et le contact sont uniques
            try:
                Membre.objects.get(numeropiece=numeropiece, contact=contact)
                messages.error(request, "Ce membre existe déjà.")
            except Membre.DoesNotExist:
                objet_membre = Membre()

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
                objet_membre.dateenre = datetime.date.today()
                objet_membre.actif = True # On active l'utilisateur
                objet_membre.utilisateur = User.objects.get(id=request.user.id)

                # On sauvegarde les données
                objet_membre.save()

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

                messages.success(request,"Enregistrement réussi")
        else:
            messages.error(request, "Veuillez renseigner les champs.")


    # PARTIE DU GET -----------------------
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
    membres = Membre.objects.filter(utilisateur_id=request.user.id).order_by('nom_prenoms')

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
        "membres": membres,

        "active_sercteuragricole": active_sercteuragricole,
        "active_liste": active_liste,
    }


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

@login_required
@permission_required('presentation.delete_membre', raise_exception=True)
def supprimer_membre(request, id):
  pass


# Fin de la Gestion du secteur -------------------------------------
