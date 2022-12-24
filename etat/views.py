from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from vieprofessionnelle.models import *
from django.contrib.auth.decorators import login_required, permission_required
from django.http import JsonResponse
from django.utils.html import strip_tags
from django.db.models import F, Q
from utilisateur.models import *
import datetime
from django.core.exceptions import FieldDoesNotExist

# Les constatntes et les variables globales
_active_onglet = ""  # Variable globale pour l'activation des onglets
_nouvellenaissance = 1  # Variable globale pour la date de la nouvelle naissance (1 an)


@login_required
@permission_required('vieprofessionnelle.add_membre', raise_exception=True)
def etat(request):

    # Les variables
    parametre = Parametre.objects.first()

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
    quantitegroupements = QuantiteGroupement.objects.order_by('id')

    context = {
        'titre': 'Etats',
        'typesecteurs': typesecteurs,
        'districts': districts,
        'nationalites': nationalites,
        'niveaux': niveaux,
        'utilisateurs': utilisateurs,
        'quantitegroupements': quantitegroupements,

        'active_membre': active_membre,
        'active_cooperative': active_cooperative,
        'active_statistique': active_statistique,

        'parametre': parametre,
    }
    return render(request, 'etat/etat.html', context)


# Liste des fonction de l'onglet Membre -------------------------------------
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
        date_debut = request.POST.get('date_debut', None)
        date_fin = request.POST.get('date_fin', None)
        utilisateur = request.POST.get('utilisateur', None)

        # Les variables
        membres = []
        imembres = []
        _parametre = Parametre.objects.first()

        # On vérifie si au moins une donnée existe
        if typesecteur or secteur or activite or \
                district or region or departement or \
                ville or commune or quartier or marche or \
                identifiant or nomprenoms or nationalite or \
                 niveau or niveauscolaire or date_fin or utilisateur:

            # on initialise la liste des membres
            membres = Membre.objects.filter(actif=True)

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
                if nationalite and membres:
                    membres = membres.filter(nationalite=nationalite)
                if niveau and membres:
                    membres = membres.filter(niveauscolaire__niveau=niveau)
                if niveauscolaire and membres:
                    membres = membres.filter(niveauscolaire=niveauscolaire)
                if date_fin and membres:
                    membres = membres.filter(dateenre__range=(date_debut, date_fin))
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
        date_debut = request.POST.get('date_debut', None)
        date_fin = request.POST.get('date_fin', None)
        utilisateur = request.POST.get('utilisateur', None)

        # Les variables
        membres = []
        _parametre = Parametre.objects.first()

        # On vérifie si au moins une donnée existe
        if typesecteur or secteur or activite or \
                district or region or departement or \
                ville or commune or quartier or marche or \
                identifiant or nomprenoms or nationalite or \
                niveau or niveauscolaire or date_fin or utilisateur:

            # on initialise la liste des membres
            membres = Membre.objects.filter(actif=True)

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
                if nationalite and membres:
                    membres = membres.filter(nationalite=nationalite)
                if niveau and membres:
                    membres = membres.filter(niveauscolaire__niveau=niveau)
                if niveauscolaire and membres:
                    membres = membres.filter(niveauscolaire=niveauscolaire)
                if date_fin and membres:
                    membres = membres.filter(dateenre__range=(date_debut, date_fin))
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


@login_required
@permission_required('vieprofessionnelle.add_membre', raise_exception=True)
def total_enfants(request):
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
        date_debut = request.POST.get('date_debut', None)
        date_fin = request.POST.get('date_fin', None)
        utilisateur = request.POST.get('utilisateur', None)

        # Les variables
        membres = []
        imembres = []
        total_enfants = 0
        _parametre = Parametre.objects.first()

        # On vérifie si au moins une donnée existe
        if typesecteur or secteur or activite or \
                district or region or departement or \
                ville or commune or quartier or marche or \
                identifiant or nomprenoms or nationalite or \
                niveau or niveauscolaire or date_fin or utilisateur:

            # on initialise la liste des membres
            membres = Membre.objects.filter(actif=True)

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
                if nationalite and membres:
                    membres = membres.filter(nationalite=nationalite)
                if niveau and membres:
                    membres = membres.filter(niveauscolaire__niveau=niveau)
                if niveauscolaire and membres:
                    membres = membres.filter(niveauscolaire=niveauscolaire)
                if date_fin and membres:
                    membres = membres.filter(dateenre__range=(date_debut, date_fin))
                if utilisateur and membres:
                    membres = membres.filter(utilisateur=utilisateur)

        else:  # On récupère tous les membres actif
            membres = Membre.objects.filter(actif=True)

        # On parcourt la liste des membres pour leur ajouter
        # des propriétés
        for membre in membres:
            membre.nombreenfant = membre.get_nombre_parent('Enfant')
            total_enfants += membre.nombreenfant
            imembres.append(membre)

        context = {
            'title': "Nombre Total d'enfants",
            'imembres': membres,
            'total_enfants': total_enfants,
        }

        return render(request, 'etat/membre/total_enfants.html', context)

    return HttpResponseRedirect(reverse('etat:etat'))


@login_required
@permission_required('vieprofessionnelle.add_membre', raise_exception=True)
def nouvelle_naissance(request):
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
        date_debut = request.POST.get('date_debut', None)
        date_fin = request.POST.get('date_fin', None)
        utilisateur = request.POST.get('utilisateur', None)

        # Les variables
        membres = []
        imembres = []
        total_enfants = 0
        _parametre = Parametre.objects.first()

        # On vérifie si au moins une donnée existe
        if typesecteur or secteur or activite or \
                district or region or departement or \
                ville or commune or quartier or marche or \
                identifiant or nomprenoms or nationalite or \
                niveau or niveauscolaire or date_fin or utilisateur:

            # on initialise la liste des membres
            membres = Membre.objects.filter(actif=True)

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
                if nationalite and membres:
                    membres = membres.filter(nationalite=nationalite)
                if niveau and membres:
                    membres = membres.filter(niveauscolaire__niveau=niveau)
                if niveauscolaire and membres:
                    membres = membres.filter(niveauscolaire=niveauscolaire)
                if date_fin and membres:
                    membres = membres.filter(dateenre__range=(date_debut, date_fin))
                if utilisateur and membres:
                    membres = membres.filter(utilisateur=utilisateur)

        else:  # On récupère tous les membres actif
            membres = Membre.objects.filter(actif=True)

        # On parcourt la liste des membres pour leur ajouter
        # des propriétés
        annee_limite = datetime.date.today().year - _nouvellenaissance  # On récupère l'année en cours moins la variable (1)

        for membre in membres:
            membre.nouvellenaissance = membre.get_nouvelle_naissance('Enfant', annee_limite)
            total_enfants += membre.nouvellenaissance
            imembres.append(membre)

        context = {
            'title': "Total Nouvelles naissances",
            'imembres': membres,
            'total_enfants': total_enfants,
        }

        return render(request, 'etat/membre/nouvelle_naissance.html', context)

    return HttpResponseRedirect(reverse('etat:etat'))


@login_required
@permission_required('vieprofessionnelle.add_membre', raise_exception=True)
def total_deces(request):
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
        date_debut = request.POST.get('date_debut', None)
        date_fin = request.POST.get('date_fin', None)
        utilisateur = request.POST.get('utilisateur', None)

        # Les variables
        membres = []
        imembres = []
        total_deces = 0
        _parametre = Parametre.objects.first()

        # On vérifie si au moins une donnée existe
        if typesecteur or secteur or activite or \
                district or region or departement or \
                ville or commune or quartier or marche or \
                identifiant or nomprenoms or nationalite or \
                niveau or niveauscolaire or date_fin or utilisateur:

            # on initialise la liste des membres
            membres = Membre.objects.filter(actif=True)

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
                if nationalite and membres:
                    membres = membres.filter(nationalite=nationalite)
                if niveau and membres:
                    membres = membres.filter(niveauscolaire__niveau=niveau)
                if niveauscolaire and membres:
                    membres = membres.filter(niveauscolaire=niveauscolaire)
                if date_fin and membres:
                    membres = membres.filter(dateenre__range=(date_debut, date_fin))
                if utilisateur and membres:
                    membres = membres.filter(utilisateur=utilisateur)

        else:  # On récupère tous les membres actif
            membres = Membre.objects.filter(actif=True)

        # On parcourt la liste des membres pour leur ajouter
        # des propriétés
        for membre in membres:
            membre.deces = membre.get_etat_sante(_parametre.id_deces)
            total_deces += membre.deces
            imembres.append(membre)

        context = {
            'title': "Nombre Total de décès",
            'imembres': membres,
            'total': total_deces,
        }

        return render(request, 'etat/membre/total_deces.html', context)

    return HttpResponseRedirect(reverse('etat:etat'))


@login_required
@permission_required('vieprofessionnelle.add_membre', raise_exception=True)
def total_deces_enfant(request):
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
        date_debut = request.POST.get('date_debut', None)
        date_fin = request.POST.get('date_fin', None)
        utilisateur = request.POST.get('utilisateur', None)

        # Les variables
        membres = []
        imembres = []
        total_deces = 0
        _parametre = Parametre.objects.first()

        # On vérifie si au moins une donnée existe
        if typesecteur or secteur or activite or \
                district or region or departement or \
                ville or commune or quartier or marche or \
                identifiant or nomprenoms or nationalite or \
                niveau or niveauscolaire or date_fin or utilisateur:

            # on initialise la liste des membres
            membres = Membre.objects.filter(actif=True)

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
                if nationalite and membres:
                    membres = membres.filter(nationalite=nationalite)
                if niveau and membres:
                    membres = membres.filter(niveauscolaire__niveau=niveau)
                if niveauscolaire and membres:
                    membres = membres.filter(niveauscolaire=niveauscolaire)
                if date_fin and membres:
                    membres = membres.filter(dateenre__range=(date_debut, date_fin))
                if utilisateur and membres:
                    membres = membres.filter(utilisateur=utilisateur)

        else:  # On récupère tous les membres actif
            membres = Membre.objects.filter(actif=True)

        # On parcourt la liste des membres pour leur ajouter
        # des propriétés
        for membre in membres:
            membre.deces = membre.get_nombre_etat_parent('Enfant', _parametre.id_deces)
            total_deces += membre.deces
            imembres.append(membre)

        context = {
            'title': "Nombre Total de décès enfants",
            'imembres': membres,
            'total': total_deces,
        }

        return render(request, 'etat/membre/total_deces_enfant.html', context)

    return HttpResponseRedirect(reverse('etat:etat'))


@login_required
@permission_required('vieprofessionnelle.add_membre', raise_exception=True)
def total_accident(request):
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
        date_debut = request.POST.get('date_debut', None)
        date_fin = request.POST.get('date_fin', None)
        utilisateur = request.POST.get('utilisateur', None)

        # Les variables
        membres = []
        imembres = []
        total_accident = 0
        _parametre = Parametre.objects.first()

        # On vérifie si au moins une donnée existe
        if typesecteur or secteur or activite or \
                district or region or departement or \
                ville or commune or quartier or marche or \
                identifiant or nomprenoms or nationalite or \
                niveau or niveauscolaire or date_fin or utilisateur:

            # on initialise la liste des membres
            membres = Membre.objects.filter(actif=True)

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

                if nationalite and membres:
                    membres = membres.filter(nationalite=nationalite)
                if niveau and membres:
                    membres = membres.filter(niveauscolaire__niveau=niveau)
                if niveauscolaire and membres:
                    membres = membres.filter(niveauscolaire=niveauscolaire)
                if date_fin and membres:
                    membres = membres.filter(dateenre__range=(date_debut, date_fin))
                if utilisateur and membres:
                    membres = membres.filter(utilisateur=utilisateur)

        else:  # On récupère tous les membres actif
            membres = Membre.objects.filter(actif=True)

        # On parcourt la liste des membres pour leur ajouter
        # des propriétés
        for membre in membres:
            membre.accident = membre.get_etat_sante(_parametre.id_accident)
            total_accident += membre.accident
            imembres.append(membre)

        context = {
            'title': "Nombre Total de décès",
            'imembres': membres,
            'total': total_accident,
        }

        return render(request, 'etat/membre/total_accident.html', context)

    return HttpResponseRedirect(reverse('etat:etat'))


@login_required
@permission_required('vieprofessionnelle.add_membre', raise_exception=True)
def total_accident_enfant(request):
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
        date_debut = request.POST.get('date_debut', None)
        date_fin = request.POST.get('date_fin', None)
        utilisateur = request.POST.get('utilisateur', None)

        # Les variables
        membres = []
        imembres = []
        total_accident = 0
        _parametre = Parametre.objects.first()

        # On vérifie si au moins une donnée existe
        if typesecteur or secteur or activite or \
                district or region or departement or \
                ville or commune or quartier or marche or \
                identifiant or nomprenoms or nationalite or \
                niveau or niveauscolaire or date_fin or utilisateur:

            # on initialise la liste des membres
            membres = Membre.objects.filter(actif=True)

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
                    elif int(typesecteur) == _parametre.id_secteurfemmeactive:
                        # On vérifie si le typesecteur correspond au paramètre
                        # id secteur femme active puis on récupère tous les membres
                        # qui ont une valeur non nul pour le secteurfemmeactive
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
                if nationalite and membres:
                    membres = membres.filter(nationalite=nationalite)
                if niveau and membres:
                    membres = membres.filter(niveauscolaire__niveau=niveau)
                if niveauscolaire and membres:
                    membres = membres.filter(niveauscolaire=niveauscolaire)
                if date_fin and membres:
                    membres = membres.filter(dateenre__range=(date_debut, date_fin))
                if utilisateur and membres:
                    membres = membres.filter(utilisateur=utilisateur)

        else:  # On récupère tous les membres actif
            membres = Membre.objects.filter(actif=True)

        # On parcourt la liste des membres pour leur ajouter
        # des propriétés
        for membre in membres:
            membre.accident = membre.get_nombre_etat_parent('Enfant', _parametre.id_accident)
            total_accident += membre.accident
            imembres.append(membre)

        context = {
            'title': "Nombre Total d'accidents enfants",
            'imembres': membres,
            'total': total_accident,
        }

        return render(request, 'etat/membre/total_accident_enfant.html', context)

    return HttpResponseRedirect(reverse('etat:etat'))
# Fin de la gestion de Membre -------------------------------------


# Liste des fonction de l'onglet Coopérative et groupement--------
@login_required
@permission_required('vieprofessionnelle.add_membre', raise_exception=True)
def liste_secteur_activite(request):

    # On initialise la variable
    _active_onglet = "active_cooperative"

    if request.method == 'POST':
        typesecteur = request.POST.get('typesecteur_c', None)
        activite = request.POST.get('activite_c', None)
        quantitegroupement = request.POST.get('quantitegroupement', None)
        speculation_debut = request.POST.get('speculation_debut', None)
        speculation_fin = request.POST.get('speculation_fin', None)

        district = request.POST.get('select_district_c', None)
        region = request.POST.get('select_region_c', None)
        departement = request.POST.get('select_departement_c', None)
        ville = request.POST.get('select_ville_c', None)

        identifiant = strip_tags(request.POST.get('identifiant', '')).strip()
        cooperative = strip_tags(request.POST.get('cooperative', '')).strip()

        # Les variables
        secteurs = []
        isecteurs = []
        _parametre = Parametre.objects.first()

        # On vérifie si au moins une donnée existe
        if typesecteur or activite or quantitegroupement or speculation_fin or \
                district or region or departement or \
                ville or identifiant or cooperative:

            if typesecteur:  # On vérifie si le typesecteur existe car on a besoin de lui pour commencer

                # On débute par les deux critaires
                if identifiant or cooperative:
                    if identifiant:
                        # On récupère le secteur selon le typesecteur
                        if int(typesecteur) == _parametre.id_secteurfemmeactive:
                            secteurs = SecteurFemmeActive.objects.filter(identifiant__iexact=identifiant)

                    if cooperative and not secteurs:
                        # On récupère le secteur selon le typesecteur
                        if int(typesecteur) == _parametre.id_secteuragricole:
                            secteurs = SecteurAgricole.objects.filter(nom__iexact=cooperative)
                        elif int(typesecteur) == _parametre.id_secteurfemmeactive:
                            secteurs = SecteurFemmeActive.objects.filter(nom__iexact=cooperative)
                        elif int(typesecteur) == _parametre.id_secteurinformel:
                            secteurs = SecteurInformel.objects.filter(nom__iexact=cooperative)
                else:
                    # On traitre ensuite les secteurs d'activités -----------------------------------
                    # On débute par le typesecteur
                    if int(typesecteur) == _parametre.id_secteuragricole:
                        secteurs = SecteurAgricole.objects.order_by('nom')
                    elif int(typesecteur) == _parametre.id_secteurfemmeactive:
                        secteurs = SecteurFemmeActive.objects.order_by('nom')
                    elif int(typesecteur) == _parametre.id_secteurinformel:
                        secteurs = SecteurInformel.objects.order_by('nom')

                    if activite and secteurs:  # On traite l'activite
                        secteurs = secteurs.filter(id=activite)

                    if speculation_fin != '0' and secteurs:  # On traite la specification agricole
                        try:
                            # On exécute l'instruction dans le bloc car l'utilisateur
                            # peut reseigner le mauvais champs et cela lèvera une erreur du type FieldError
                            secteurs = secteurs.filter(speculation_agricole__range=(speculation_debut, speculation_fin))
                        except:
                            pass

                    if quantitegroupement and secteurs:  # On traite la quantité de groupement
                        try:
                            # On exécute l'instruction dans le bloc car l'utilisateur
                            # peut reseigner le mauvais champs et cela lèvera une erreur du type FieldError
                            secteurs = secteurs.filter(quantitegroupement=quantitegroupement)
                        except:
                            pass

                    # On traite enfin la localisation ------------------------------------
                    if district and secteurs:
                        secteurs = secteurs.filter(ville__departement__region__district=district)
                    if region and secteurs:
                        secteurs = secteurs.filter(ville__departement__region=region)
                    if departement and secteurs:
                        secteurs = secteurs.filter(ville__departement=departement)
                    if ville and secteurs:
                        secteurs = secteurs.filter(ville=ville)
            else:
                return HttpResponseRedirect(reverse('etat:etat'))
        else:
            return HttpResponseRedirect(reverse('etat:etat'))

        # On parcourt la liste des secteurs pour leur ajouter
        # des propriétés

        for secteur in secteurs:
            print(secteur.nom)

        context = {
            'title': "Liste secteur d'activité",
            'isecteurs': isecteurs,
        }

        return render(request, 'etat/cooperative/liste_secteur_activite.html', context)

    return HttpResponseRedirect(reverse('etat:etat'))


@login_required
@permission_required('vieprofessionnelle.add_membre', raise_exception=True)
def liste_membre(request):

    # On initialise la variable
    _active_onglet = "active_cooperative"

    if request.method == 'POST':
        typesecteur = request.POST.get('typesecteur_c', None)
        activite = request.POST.get('activite_c', None)
        quantitegroupement = request.POST.get('quantitegroupement', None)
        speculation_debut = request.POST.get('speculation_debut', None)
        speculation_fin = request.POST.get('speculation_fin', None)

        district = request.POST.get('select_district_c', None)
        region = request.POST.get('select_region_c', None)
        departement = request.POST.get('select_departement_c', None)
        ville = request.POST.get('select_ville_c', None)

        identifiant = strip_tags(request.POST.get('identifiant', '')).strip()
        cooperative = strip_tags(request.POST.get('cooperative', '')).strip()

        # Les variables
        secteurs = []
        isecteurs = []
        _parametre = Parametre.objects.first()

        # On vérifie si au moins une donnée existe
        if typesecteur or activite or quantitegroupement or speculation_fin or \
                district or region or departement or \
                ville or identifiant or cooperative:

            if typesecteur:  # On vérifie si le typesecteur existe car on a besoin de lui pour commencer

                # On débute par les deux critaires
                if identifiant or cooperative:
                    if identifiant:
                        # On récupère le secteur selon le typesecteur
                        if int(typesecteur) == _parametre.id_secteurfemmeactive:
                            secteurs = SecteurFemmeActive.objects.filter(identifiant__iexact=identifiant)

                    if cooperative and not secteurs:
                        # On récupère le secteur selon le typesecteur
                        if int(typesecteur) == _parametre.id_secteuragricole:
                            secteurs = SecteurAgricole.objects.filter(nom__iexact=cooperative)
                        elif int(typesecteur) == _parametre.id_secteurfemmeactive:
                            secteurs = SecteurFemmeActive.objects.filter(nom__iexact=cooperative)
                        elif int(typesecteur) == _parametre.id_secteurinformel:
                            secteurs = SecteurInformel.objects.filter(nom__iexact=cooperative)
                else:
                    # On traitre ensuite les secteurs d'activités -----------------------------------
                    # On débute par le typesecteur
                    if int(typesecteur) == _parametre.id_secteuragricole:
                        secteurs = SecteurAgricole.objects.order_by('nom')
                    elif int(typesecteur) == _parametre.id_secteurfemmeactive:
                        secteurs = SecteurFemmeActive.objects.order_by('nom')
                    elif int(typesecteur) == _parametre.id_secteurinformel:
                        secteurs = SecteurInformel.objects.order_by('nom')

                    if activite and secteurs:  # On traite l'activite
                        secteurs = secteurs.filter(id=activite)

                    if speculation_fin != '0' and secteurs:  # On traite la specification agricole
                        try:
                            # On exécute l'instruction dans le bloc car l'utilisateur
                            # peut reseigner le mauvais champs et cela lèvera une erreur du type FieldError
                            secteurs = secteurs.filter(speculation_agricole__range=(speculation_debut, speculation_fin))
                        except:
                            pass

                    if quantitegroupement and secteurs:  # On traite la quantité de groupement
                        try:
                            # On exécute l'instruction dans le bloc car l'utilisateur
                            # peut reseigner le mauvais champs et cela lèvera une erreur du type FieldError
                            secteurs = secteurs.filter(quantitegroupement=quantitegroupement)
                        except:
                            pass

                    # On traite enfin la localisation ------------------------------------
                    if district and secteurs:
                        secteurs = secteurs.filter(ville__departement__region__district=district)
                    if region and secteurs:
                        secteurs = secteurs.filter(ville__departement__region=region)
                    if departement and secteurs:
                        secteurs = secteurs.filter(ville__departement=departement)
                    if ville and secteurs:
                        secteurs = secteurs.filter(ville=ville)
            else:
                return HttpResponseRedirect(reverse('etat:etat'))
        else:
            return HttpResponseRedirect(reverse('etat:etat'))

        # On parcourt la liste des secteurs pour leur ajouter
        # des propriétés
        # On détermine le typesecteur
        isecteur = {}
        mon_secteur = None
        liste_membre = []

        if int(typesecteur) == _parametre.id_secteuragricole:
            for secteur in secteurs:
                # On récupère la liste des membres du secteur
                mon_secteur = MembreSecteurAgricole.objects.filter(secteuragricole=secteur.id)

                # On récupère tous les membres du secteur
                for secteur_simple in mon_secteur:
                    liste_membre.append(secteur_simple.membre)

                isecteur['secteur'] = secteur
                isecteur['membres'] = liste_membre

                # On ajoute le secteur et ses membres dans la liste
                isecteurs.append(isecteur)

                # On reinitialise les variables
                isecteur = {}
                liste_membre = []

        elif int(typesecteur) == _parametre.id_secteurfemmeactive:
            for secteur in secteurs:
                # On récupère la liste des membres du secteur
                mon_secteur = MembreSecteurFemmeActive.objects.filter(secteurfemmeactive=secteur.id)

                # On récupère tous les membres du secteur
                for secteur_simple in mon_secteur:
                    liste_membre.append(secteur_simple.membre)

                isecteur['secteur'] = secteur
                isecteur['membres'] = liste_membre

                # On ajoute le secteur et ses membres dans la liste
                isecteurs.append(isecteur)

                # On reinitialise les variables
                isecteur = {}
                liste_membre = []

        elif int(typesecteur) == _parametre.id_secteurinformel:
            pass

        # test
        for secteur in isecteurs:
            print(secteur['secteur'].nom)
            print(secteur['membres'])

        context = {
            'title': "Liste secteur d'activité",
            'isecteurs': isecteurs,
        }

        return render(request, 'etat/cooperative/liste_membre.html', context)

    return HttpResponseRedirect(reverse('etat:etat'))

# Fin de la gestion de l'onglet Coopérative et groupement--------