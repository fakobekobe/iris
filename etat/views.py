from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from vieprofessionnelle.models import *
from django.contrib.auth.decorators import login_required, permission_required
from django.http import JsonResponse
from django.utils.html import strip_tags
from django.db.models import F, Q
from utilisateur.models import *

# Les constatntes et les variables globales
_active_onglet = ""  # Variable globale pour l'activation des onglets


@login_required
@permission_required('vieprofessionnelle.add_membre', raise_exception=True)
def etat(request):
    # Initialisation de l'affichage de l'onglet active
    active_membre = ['', 'false', '']
    active_cooperative = ['', 'false', '']
    active_statistique = ['', 'false', '']

    if _active_onglet == "active_membre":
        active_membre = ['active', 'true', 'show active']
    elif _active_onglet == "active_cooperative":
        active_cooperative = ['active', 'true', 'show active']
    elif _active_onglet == "active_statistique":
        active_statistique = ['active', 'true', 'show active']
    else:
        # Affichage par défaut
        active_membre = ['active', 'true', 'show active']

    typesecteurs = TypeSecteur.objects.order_by('id')
    districts = District.objects.order_by('id')
    nationalites = Nationalite.objects.order_by('id')
    niveaux = Niveau.objects.order_by('id')
    utilisateurs = User.objects.order_by('id')

    context = {
        'titre': 'Etats',
        'typesecteurs': typesecteurs,
        'districts': districts,
        'nationalites': nationalites,
        'niveaux': niveaux,
        'utilisateurs': utilisateurs,

        'active_membre': active_membre,
        'active_cooperative': active_cooperative,
        'active_statistique': active_statistique,
    }
    return render(request, 'etat/etat.html', context)


@login_required
@permission_required('vieprofessionnelle.add_membre', raise_exception=True)
def fiche_identification(request):
    if request.method == 'POST':
        typesecteur = request.POST.get('typesecteur', None)
        secteur = request.POST.get('secteur', None)
        activite = request.POST.get('activite', None)

        district = request.POST.get('select_district', None)
        region = request.POST.get('select_region', None)
        departement = request.POST.get('select_departement', None)
        ville = request.POST.get('select_ville', None)
        commune = request.POST.get('select_commune', None)
        quartier = request.POST.get('select_quartier', None)
        marche = request.POST.get('select_marche', None)

        identifiant = strip_tags(request.POST.get('identifiant', '')).strip()
        nomprenoms = strip_tags(request.POST.get('nomprenoms', '')).strip()
        nationalite = request.POST.get('nationalite', None)
        niveau = request.POST.get('niveau', None)
        niveauscolaire = request.POST.get('niveauscolaire', None)
        utilisateur = request.POST.get('utilisateur', None)

        # Les variables
        membres = []
        imembres = []
        _parametre = Parametre.objects.first()

        # On vérifie si au moins une donnée existe
        if typesecteur or secteur or activite or \
                district or region or departement or \
                ville or commune or quartier or marche or \
                nationalite or niveau or niveauscolaire or utilisateur:

            # On débute par les deux critaires
            if identifiant or nomprenoms:
                if identifiant:
                    membres = Membre.objects.filter(identifiant__iexact=identifiant)
                if nomprenoms and not membres:
                    membres = Membre.objects.filter(nom_prenoms__iexact=nomprenoms)
            else:
                # On traite d'abord le secteur d'activité ----------------
                if typesecteur:  # On traite le type de secteur
                    if int(typesecteur) == _parametre.id_secteuragricole:
                        # On vérifie si le typesecteur correspond au
                        # paramètre id secteur agricole puis on récupère
                        # tous les membres qui ont une valeur non nul pour le secteuragricole
                        membres = Membre.objects.filter(secteuragricole=F('secteuragricole'), actif=True)
                    elif int(
                            typesecteur) == _parametre.id_secteurfemmeactive:  # On vérifie si le typesecteur correspond au paramètre id secteur femme active puis on récupère tous les membres qui ont une valeur non nul pour le secteurfemmeactive
                        membres = Membre.objects.filter(secteurfemmeactive=F('secteurfemmeactive'), actif=True)
                    elif int(typesecteur) == _parametre.id_secteurinformel:
                        # On vérifie si le typesecteur correspond au paramètre
                        # id secteur informel puis on récupère tous les membres
                        # qui ont une valeur non nul pour le secteurinformel
                        membres = Membre.objects.filter(secteurinformel=F('secteurinformel'), actif=True)
                if secteur and membres:  # On traite le secteur
                    membres = membres.filter(secteurs=secteur)
                if activite and membres:  # On traite le nom des coopératives et groupements
                    if int(typesecteur) == _parametre.id_secteuragricole:
                        membres = membres.filter(secteuragricole=activite)
                    elif int(typesecteur) == _parametre.id_secteurfemmeactive:
                        membres = membres.filter(secteurfemmeactive=activite)
                    elif int(typesecteur) == _parametre.id_secteurinformel:
                        membres = membres.filter(secteurinformel=activite)

                # On traite ensuite la localisation ---------------------------------------
                if not membres:
                    # Si rien n'est sélectionné jusqu'ici,
                    # on débute avec tous les membres sinon
                    # on continue avec les membres existants
                    membres = Membre.objects.filter(actif=True)

                if district and membres:
                    membres = membres.filter(quartier__commune__ville__departement__region__district=district)
                if region and membres:
                    membres = membres.filter(quartier__commune__ville__departement__region=region)
                if departement and membres:
                    membres = membres.filter(quartier__commune__ville__departement=departement)
                if ville and membres:
                    membres = membres.filter(quartier__commune__ville=ville)
                if commune and membres:
                    membres = membres.filter(quartier__commune=commune)
                if quartier and membres:
                    membres = membres.filter(quartier=quartier)
                if marche and membres:
                    #  Le marché concerne le secteurfemmeactive
                    membres = membres.filter(
                        secteurfemmeactive=F('secteurfemmeactive'),
                        secteurfemmeactive__marche=marche)

                # On traite enfin les derniers critaires ------------------------------------------
                if not membres:
                    # Si rien n'est sélectionné jusqu'ici,
                    # on débute avec tous les membres sinon
                    # on continue avec les membres existants
                    membres = Membre.objects.filter(actif=True)

                if nationalite and membres:
                    membres = membres.filter(nationalite=nationalite)
                if niveau and membres:
                    membres = membres.filter(niveauscolaire__niveau=niveau)
                if niveauscolaire and membres:
                    membres = membres.filter(niveauscolaire=niveauscolaire)
                if utilisateur and membres:
                    membres = membres.filter(utilisateur=utilisateur)

        else:  # On récupère tous les membres actif
            membres = Membre.objects.filter(actif=True)

        # On parcourt la liste des membres pour leur ajouter
        # des propriétés pour l'impression selon le type de secteur

        for membre in membres:
            if membre.secteuragricole_set.first():

                membre.get_region = membre.get_region()
                membre.secteuragricole = membre.secteuragricole_set.first()
                membre.nombrefemme = membre.get_nombre_parent('Femme')
                membre.nombreenfant = membre.get_nombre_parent('Enfant')
                membre.lieu_habitation = membre.get_lieu_habitation()
                try:
                    document = Document.objects.get(membre=membre)
                    membre.photo = document.get_photo_membre()
                except Document.DoesNotExist:
                    pass
                try:
                    membre.cooperative = MembreSecteurAgricole.objects.get(membre=membre,
                                                                           secteuragricole=membre.secteuragricole)
                except MembreSecteurAgricole.DoesNotExist:
                    pass

                # On ajoute le membre dans la liste à imprimer
                imembres.append(membre)

            elif membre.secteurfemmeactive_set.first():

                membre.get_region = membre.get_region()
                membre.groupement = membre.secteurfemmeactive_set.first()
                membre.nombreenfant = membre.get_nombre_parent('Enfant')
                membre.lieu_habitation = membre.get_lieu_habitation()
                membre.secteuractivite = membre.secteurs.first()
                try:
                    document = Document.objects.get(membre=membre)
                    membre.photo = document.get_photo_membre()
                except Document.DoesNotExist:
                    pass
                try:
                    membre.secteurfemmeactive = MembreSecteurFemmeActive.objects.get(membre=membre,
                                                                                     secteurfemmeactive=membre.groupement)
                    membre.personneressource_contact = membre.secteurfemmeactive.personneressource.get_personneressource_contact()
                except MembreSecteurFemmeActive.DoesNotExist:
                    pass

                # On ajoute le membre dans la liste à imprimer
                imembres.append(membre)

            else:
                print('secteurinformel')

        context = {
            'title': "Fiche d'identification",
            'imembres': imembres,
        }

        return render(request, 'etat/membre/imprimer_fiche_identification.html', context)

    return HttpResponseRedirect(reverse('etat:etat'))


@login_required
@permission_required('vieprofessionnelle.add_membre', raise_exception=True)
def retour_etat(request, id):
    global _active_onglet

    if int(id) == 1:
        _active_onglet = "active_membre"  # On initialise la variable
        return HttpResponseRedirect(reverse('etat:etat'))
    elif int(id) == 2:
        _active_onglet = "active_cooperative"  # On initialise la variable
        return HttpResponseRedirect(reverse('etat:etat'))
    elif int(id) == 3:
        _active_onglet = "active_statistique"  # On initialise la variable
        return HttpResponseRedirect(reverse('etat:etat'))

@login_required
@permission_required('vieprofessionnelle.add_membre', raise_exception=True)
def liste_badge(request):
    if request.method == 'POST':
        typesecteur = request.POST.get('typesecteur', None)
        secteur = request.POST.get('secteur', None)
        activite = request.POST.get('activite', None)

        district = request.POST.get('select_district', None)
        region = request.POST.get('select_region', None)
        departement = request.POST.get('select_departement', None)
        ville = request.POST.get('select_ville', None)
        commune = request.POST.get('select_commune', None)
        quartier = request.POST.get('select_quartier', None)
        marche = request.POST.get('select_marche', None)

        identifiant = strip_tags(request.POST.get('identifiant', '')).strip()
        nomprenoms = strip_tags(request.POST.get('nomprenoms', '')).strip()
        nationalite = request.POST.get('nationalite', None)
        niveau = request.POST.get('niveau', None)
        niveauscolaire = request.POST.get('niveauscolaire', None)
        utilisateur = request.POST.get('utilisateur', None)

        # Les variables
        membres = []
        _parametre = Parametre.objects.first()

        # On vérifie si au moins une donnée existe
        if typesecteur or secteur or activite or \
                district or region or departement or \
                ville or commune or quartier or marche or \
                nationalite or niveau or niveauscolaire or utilisateur:

            # On débute par les deux critaires
            if identifiant or nomprenoms:
                if identifiant:
                    membres = Membre.objects.filter(identifiant__iexact=identifiant)
                if nomprenoms and not membres:
                    membres = Membre.objects.filter(nom_prenoms__iexact=nomprenoms)
            else:
                # On traite d'abord le secteur d'activité ----------------
                if typesecteur:  # On traite le type de secteur
                    if int(typesecteur) == _parametre.id_secteuragricole:
                        # On vérifie si le typesecteur correspond au
                        # paramètre id secteur agricole puis on récupère
                        # tous les membres qui ont une valeur non nul pour le secteuragricole
                        membres = Membre.objects.filter(secteuragricole=F('secteuragricole'), actif=True)
                    elif int(
                            typesecteur) == _parametre.id_secteurfemmeactive:  # On vérifie si le typesecteur correspond au paramètre id secteur femme active puis on récupère tous les membres qui ont une valeur non nul pour le secteurfemmeactive
                        membres = Membre.objects.filter(secteurfemmeactive=F('secteurfemmeactive'), actif=True)
                    elif int(typesecteur) == _parametre.id_secteurinformel:
                        # On vérifie si le typesecteur correspond au paramètre
                        # id secteur informel puis on récupère tous les membres
                        # qui ont une valeur non nul pour le secteurinformel
                        membres = Membre.objects.filter(secteurinformel=F('secteurinformel'), actif=True)
                if secteur and membres:  # On traite le secteur
                    membres = membres.filter(secteurs=secteur)
                if activite and membres:  # On traite le nom des coopératives et groupements
                    if int(typesecteur) == _parametre.id_secteuragricole:
                        membres = membres.filter(secteuragricole=activite)
                    elif int(typesecteur) == _parametre.id_secteurfemmeactive:
                        membres = membres.filter(secteurfemmeactive=activite)
                    elif int(typesecteur) == _parametre.id_secteurinformel:
                        membres = membres.filter(secteurinformel=activite)

                # On traite ensuite la localisation ---------------------------------------
                if not membres:
                    # Si rien n'est sélectionné jusqu'ici,
                    # on débute avec tous les membres sinon
                    # on continue avec les membres existants
                    membres = Membre.objects.filter(actif=True)

                if district and membres:
                    membres = membres.filter(quartier__commune__ville__departement__region__district=district)
                if region and membres:
                    membres = membres.filter(quartier__commune__ville__departement__region=region)
                if departement and membres:
                    membres = membres.filter(quartier__commune__ville__departement=departement)
                if ville and membres:
                    membres = membres.filter(quartier__commune__ville=ville)
                if commune and membres:
                    membres = membres.filter(quartier__commune=commune)
                if quartier and membres:
                    membres = membres.filter(quartier=quartier)
                if marche and membres:
                    #  Le marché concerne le secteurfemmeactive
                    membres = membres.filter(
                        secteurfemmeactive=F('secteurfemmeactive'),
                        secteurfemmeactive__marche=marche)

                # On traite enfin les derniers critaires ------------------------------------------
                if not membres:
                    # Si rien n'est sélectionné jusqu'ici,
                    # on débute avec tous les membres sinon
                    # on continue avec les membres existants
                    membres = Membre.objects.filter(actif=True)

                if nationalite and membres:
                    membres = membres.filter(nationalite=nationalite)
                if niveau and membres:
                    membres = membres.filter(niveauscolaire__niveau=niveau)
                if niveauscolaire and membres:
                    membres = membres.filter(niveauscolaire=niveauscolaire)
                if utilisateur and membres:
                    membres = membres.filter(utilisateur=utilisateur)

        else:  # On récupère tous les membres actif
            membres = Membre.objects.filter(actif=True)

        # On parcourt la liste des membres pour leur ajouter
        # des propriétés pour l'impression selon le type de secteur

        context = {
            'title': "Liste n°badges",
            'membres': membres,
        }

        return render(request, 'etat/membre/liste_badge.html', context)

    return HttpResponseRedirect(reverse('etat:etat'))