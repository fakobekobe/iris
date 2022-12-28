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
from utilisateur.models import Parametre
from django.db.models import F

# Les constatntes et les variables globales
_active_onglet = ""  # Variable globale pour l'activation des onglets
_active_session = False  # Variable globale pour l'activation des onglets


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
        sexe = request.POST.get('sexe', None)
        nom = strip_tags(request.POST.get('nom', None)).strip().title() # On rétire les tag (<>) et on enleve les espaces au début et fin
        prenoms = strip_tags(request.POST.get('prenoms', None)).strip().title()
        nomjeunefille = strip_tags(request.POST.get('nomjeunefille', None)).strip().title()
        date_naissance = request.POST.get('date_naissance', None)
        lieu_naissance = request.POST.get('lieu_naissance', None)
        typepiece = request.POST.get('typepiece', None)
        numeropiece = strip_tags(request.POST.get('numeropiece', None)).strip()
        nationalite = request.POST.get('nationalite', None)
        contact = strip_tags(request.POST.get('contact', None)).strip()
        cooperative = request.POST.get('cooperative', None)
        dateadhesion = request.POST.get('dateadhesion', None)
        numero_carte = strip_tags(request.POST.get('numero_carte', None)).strip()
        chapeau = request.POST.get('chapeau', None)
        niveauscolaire = request.POST.get('niveauscolaire', None)
        situationmatrimoniale = request.POST.get('situationmatrimoniale', None)
        lieu_habitation = request.POST.get('lieu_habitation', None)

        if not date_naissance:
            date_naissance = None

        if not dateadhesion:
            dateadhesion = None

        if nom != 'None' and date_naissance and numeropiece != 'None' and contact != 'None' and\
                typepiece and cooperative and lieu_habitation and sexe and\
                nationalite and lieu_naissance and niveauscolaire and \
                situationmatrimoniale and lieu_habitation and chapeau:

            if not request.session.get('id_membre'): # On traite la modification
                # On vérifie si ce membre existe déjà car le numeropiece et le contact sont uniques
                try:
                    Membre.objects.get(numeropiece=numeropiece, contact=contact)
                    messages.error(request, "Ce membre existe déjà.")
                    il_existe = False
                except Membre.DoesNotExist:
                    # On vérifie si le numeropiece existe
                    try:
                        Membre.objects.get(numeropiece=numeropiece)
                        messages.error(request, "Ce numéro de pièce existe déjà.")
                        il_existe = False
                    except:
                        # On vérifie si le numéro de téléphone existe
                        try:
                            Membre.objects.get(contact=contact)
                            messages.error(request, "Ce contact existe déjà.")
                            il_existe = False
                        except:
                            objet_membre = Membre()
            else:
                # On vérifie si le membre à modifier existe
                try:
                    objet_membre = Membre.objects.get(id=request.session.get('id_membre'))
                except Membre.DoesNotExist:
                    messages.error(request, "Ce membre n'existe pas.")
                    il_existe = False

            if il_existe:  # Si la valeur est True on entre dans la condition
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
                    objet_membre.set_identifiant()
                    objet_membre.dateenre = datetime.date.today()

                objet_membre.actif = True  # On active l'utilisateur
                objet_membre.utilisateur = User.objects.get(id=request.user.id)

                # On sauvegarde les données
                objet_membre.save()

                if not request.session.get('id_membre'):

                    # On ajoute le secteur agricole en relation
                    MembreSecteurAgricole.objects.create(
                        membre=objet_membre,
                        secteuragricole=SecteurAgricole.objects.get(id=cooperative),
                        date_adhesion=dateadhesion,
                        numero_carte=numero_carte,
                        chapeau=Chapeau.objects.get(id=chapeau),
                    )

                    messages.success(request, "Enregistrement réussi")

                else:
                    try:
                        membresecteura = MembreSecteurAgricole.objects.get(membre=objet_membre)
                        membresecteura.secteuragricole = SecteurAgricole.objects.get(id=cooperative)
                        membresecteura.date_adhesion = dateadhesion
                        membresecteura.numero_carte = numero_carte
                        membresecteura.chapeau = Chapeau.objects.get(id=chapeau)
                        membresecteura.save()

                        messages.success(request, "Modification réussi")
                    except MembreSecteurAgricole.DoesNotExist:
                        pass

                    del request.session['id_membre']  # On détruit la variable

        else:
            messages.error(request, "Veuillez renseigner les champs.")


    # PARTIE DU GET -----------------------
    if not _active_session:
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
    membres = Membre.objects.filter(utilisateur_id=request.user.id, actif=True, secteuragricole=F('secteuragricole')).order_by('nom_prenoms')
    chapeaux = Chapeau.objects.order_by('-id')


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
        "chapeaux": chapeaux,

        "active_secteuragricole": active_secteuragricole,
        "active_liste": active_liste,
    }

    if request.session.get('id_membre'): # On affiche la page de modification
        # On récupère le membre
        context["membre_actif"] = Membre.objects.get(id=request.session.get('id_membre'))
        context["membre_secteuragricole"] = MembreSecteurAgricole.objects.get(membre_id=request.session.get('id_membre'))
        return render(request, "presentation/modifier_secteuragricole.html", context)

    return render(request, "presentation/secteuragricole.html", context)


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
    typedocuments = TypeDocument.objects.order_by('id')
    documents = Document.objects.filter(membre=membre).order_by('id')
    parents_membre = Parent.objects.filter(membre=membre).order_by('id')
    parents = Parent.objects.order_by('id')
    typeparents = TypeParent.objects.order_by('id')
    typeetatsantes = TypeEtatSante.objects.order_by('id')
    etatsantes = EtatSante.objects.filter(membre=membre).order_by('id')

    context = {
        'title': "Détials du membre",
        'membre': membre,
        'typesecteurs': typesecteurs,
        'secteurs': secteurs,
        'typedocuments': typedocuments,
        'documents': documents,
        'parents_membre': parents_membre,
        'parents': parents,
        'typeparents': typeparents,
        'typeetatsantes': typeetatsantes,
        'etatsantes': etatsantes,
        'id_retour': 1,  # Variable pour le lien de retour vers la liste des membres
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
def modifier_secteuragricole(request, id):
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
@permission_required('vieprofessionnelle.add_membre', raise_exception=True)
def ajouter_document_membre(request):
    if request.method == "POST":
        id_membre_document = request.POST.get('id_membre_document', None)
        typedocument = request.POST.get('select_typedocument', None)
        dateenre = request.POST.get('dateenre_d', None)
        if id_membre_document and typedocument:
            if not dateenre:
                dateenre = None

            if len(request.FILES) != 0:
                photo = request.FILES["photo"]
            else:
                photo = "profil.png" # image par défaut

            try:
                # On récupère le membre
                membre = Membre.objects.get(id=id_membre_document)
            except Membre.DoesNotExist:
                data = {"libelle": "Ce membre n'existe pas."}
                return JsonResponse({'data': data}, status=404)

            try:
                # On récupère le secteur
                typedocument = TypeDocument.objects.get(id=typedocument)
            except TypeDocument.DoesNotExist:
                data = {"libelle": "Ce type de document n'existe pas."}
                return JsonResponse({'data': data}, status=404)

            # Les données sont bonnes, on ajoute le document du membre
            objet_document = Document()
            objet_document.membre = membre
            objet_document.typedocument = typedocument
            objet_document.dateenre = dateenre
            objet_document.photo = photo
            objet_document.save()

            # On récupère tous les documents du membre
            documents = Document.objects.filter(membre=membre).order_by('id')

            if documents:
                data = [{'id': document.id, 'photo': document.photo.url, 'photo_name': document.photo.name,
                         'typedocument': document.typedocument.libelle, 'id_membre': id_membre_document,
                         'dateenre': document.dateenre.strftime('%d/%m/%Y')} for document in documents]

                return JsonResponse({'data': data}, status=200)

        else:
            data = {"libelle":"Veuillez renseigner les champs"}
            return JsonResponse({'data': data}, status=404)

    return HttpResponseRedirect(reverse('presentation:ajouter_secteuragricole'))


@login_required
@permission_required('vieprofessionnelle.delete_membre', raise_exception=True)
def supprimer_document_membre(request):
    if request.method == "GET":
        id_membre_document_s = request.GET.get('id_membre_document_s', None)
        supprimer_d = request.GET.get('supprimer_d', None)

        if id_membre_document_s and supprimer_d:

            try:
                # On récupère le membre
                membre = Membre.objects.get(id=id_membre_document_s)
            except Membre.DoesNotExist:
                data = {"libelle": "Ce membre n'existe pas."}
                return JsonResponse({'data': data}, status=404)

            try:
                # On récupère le secteur
                document = Document.objects.get(id=supprimer_d)
            except Document.DoesNotExist:
                data = {"libelle": "Ce document n'existe pas."}
                return JsonResponse({'data': data}, status=404)

            # Les données sont bonnes, on supprime le document du membre
            if document:
                try:
                    if document.photo.size > 0:
                        # On ne supprime pas l'image par défaut
                        if document.photo != "profil.png":
                            os.remove(document.photo.path)
                        document.delete()
                except FileNotFoundError:
                    data = {"libelle": "Ce document n'existe pas."}
                    return JsonResponse({'data': data}, status=404)

            # On récupère tous les documents du membre
            documents = Document.objects.filter(membre=membre).order_by('id')

            if documents:
                data = [{'id': document.id, 'photo': document.photo.url, 'photo_name': document.photo.name,
                        'typedocument': document.typedocument.libelle, 'id_membre': id_membre_document_s,
                        'dateenre': document.dateenre.strftime('%d/%m/%Y')} for document in documents]

                return JsonResponse({'data': data}, status=200)

        else:
            data = {"libelle": "Veuillez renseigner les champs"}
            return JsonResponse({'data': data}, status=404)

    return HttpResponseRedirect(reverse('presentation:ajouter_secteuragricole'))


@login_required
@permission_required('vieprofessionnelle.delete_membre', raise_exception=True)
def supprimer_parent_membre(request):
    if request.method == "GET":
        id_membre_parent_s = request.GET.get('id_membre_parent_s', None)
        supprimer_p = request.GET.get('supprimer_p', None)

        if id_membre_parent_s and supprimer_p:

            try:
                # On récupère le membre
                membre = Membre.objects.get(id=id_membre_parent_s)
            except Membre.DoesNotExist:
                data = {"libelle": "Ce membre n'existe pas."}
                return JsonResponse({'data': data}, status=404)

            try:
                # On récupère le secteur
                parent = Parent.objects.get(id=supprimer_p)
            except Parent.DoesNotExist:
                data = {"libelle": "Ce parent n'existe pas."}
                return JsonResponse({'data': data}, status=404)

            # Les données sont bonnes, on ajoute le secteur au membre
            if parent:
                membre.parents.remove(parent)

                # On récupère tous les documents du membre
                parents = Parent.objects.filter(membre=membre).order_by('id')

                if parents:
                    data = [{'id': parent.id, 'typeparent': parent.typeparent.libelle.upper(),
                             'id_membre': id_membre_parent_s, 'nomprenoms': parent.nomprenoms.title(),
                             'contact': parent.contact, 'adresse': parent.adresse,
                             'datenaissance': parent.datenaissance.strftime('%d/%m/%Y')} for parent in parents]

                    return JsonResponse({'data': data}, status=200)

        else:
            data = {"libelle": "Veuillez renseigner les champs"}
            return JsonResponse({'data': data}, status=404)

    return HttpResponseRedirect(reverse('presentation:ajouter_secteuragricole'))


@login_required
@permission_required('vieprofessionnelle.add_parent', raise_exception=True)
def ajouter_parent_membre(request):
    if request.method == "GET":
        # On initialise les variables
        id_membre_parent = request.GET.get("id_membre_parent", None)
        id_parent = request.GET.get("parent", None)

        if id_membre_parent and id_parent:  # On vérifie si les champs ont été renseignés

            try:
                # On récupère le membre
                membre = Membre.objects.get(id=id_membre_parent)
            except Membre.DoesNotExist:
                data = {"libelle": "Ce membre n'existe pas."}
                return JsonResponse({'data': data}, status=404)

            try:
                # On récupère le membre
                parent = Parent.objects.get(id=id_parent)
            except Parent.DoesNotExist:
                data = {"libelle": "Ce parent n'existe pas."}
                return JsonResponse({'data': data}, status=404)

            # On ajoute le parent au membre
            membre.parents.add(parent)

            # On récupère tous les documents du membre
            parents = Parent.objects.filter(membre=membre).order_by('id')

            if parents:
                data = [{'id': parent.id, 'typeparent': parent.typeparent.libelle.upper(),
                        'id_membre': id_membre_parent, 'nomprenoms': parent.nomprenoms.title(),
                        'contact': parent.contact, 'adresse': parent.adresse,
                        'datenaissance': parent.datenaissance.strftime('%d/%m/%Y')} for parent in parents]

                return JsonResponse({'data': data}, status=200)

        else:
            data = {"libelle": "Toutes les données n'ont pas été reçues"}
            return JsonResponse({'data': data}, status=404)
    else:
        return HttpResponseRedirect(reverse('vieprofessionnelle:vieprofessionnelle'))


@login_required
@permission_required('vieprofessionnelle.add_membre', raise_exception=True)
def retour_liste_membre(request, id):
    global _active_onglet
    _active_onglet = "active_liste"  # On initialise la variable

    if int(id) == 1:
        return HttpResponseRedirect(reverse('presentation:ajouter_secteuragricole'))
    elif int(id) == 2:
        return HttpResponseRedirect(reverse('presentation:ajouter_secteurfemmeactive'))


@login_required
@permission_required('vieprofessionnelle.add_membre', raise_exception=True)
def ajouter_etatsante_membre(request):
    if request.method == "POST":
        id_membre_etatsante = request.POST.get('id_membre_etatsante', None)
        typeetatsante = request.POST.get('select_typeetatsante', None)
        dateenre = request.POST.get('dateenre_e', None)
        if id_membre_etatsante and typeetatsante and dateenre:

            try:
                # On récupère le membre
                membre = Membre.objects.get(id=id_membre_etatsante)
            except Membre.DoesNotExist:
                data = {"libelle": "Ce membre n'existe pas."}
                return JsonResponse({'data': data}, status=404)

            try:
                # On récupère le secteur
                typeetatsante = TypeEtatSante.objects.get(id=typeetatsante)
            except TypeEtatSante.DoesNotExist:
                data = {"libelle": "Ce type d'état de santé n'existe pas."}
                return JsonResponse({'data': data}, status=404)

            # Les données sont bonnes, on ajoute l'état de santé du membre
            objet_etatsante = EtatSante()
            objet_etatsante.membre = membre
            objet_etatsante.parent = None
            objet_etatsante.typeetatsante = typeetatsante
            objet_etatsante.dateenre = dateenre
            objet_etatsante.save()

            # On récupère tous les états de santé du membre
            etatsantes = EtatSante.objects.filter(membre=membre).order_by('id')

            if etatsantes:
                data = [{'id': etatsante.id, 'typeetatsante': etatsante.typeetatsante.libelle.upper(),
                         'id_membre': id_membre_etatsante,
                         'dateenre': etatsante.dateenre.strftime('%d/%m/%Y')} for etatsante in etatsantes]

                return JsonResponse({'data': data}, status=200)

        else:
            data = {"libelle": "Veuillez renseigner les champs"}
            return JsonResponse({'data': data}, status=404)

    return HttpResponseRedirect(reverse('presentation:ajouter_secteuragricole'))


@login_required
@permission_required('vieprofessionnelle.delete_membre', raise_exception=True)
def supprimer_etatsante_membre(request):
    if request.method == "GET":
        id_membre_etatsante_s = request.GET.get('id_membre_etatsante_s', None)
        supprimer_e = request.GET.get('supprimer_e', None)

        if id_membre_etatsante_s and supprimer_e:

            try:
                # On récupère le membre
                membre = Membre.objects.get(id=id_membre_etatsante_s)
            except Membre.DoesNotExist:
                data = {"libelle": "Ce membre n'existe pas."}
                return JsonResponse({'data': data}, status=404)

            try:
                # On récupère le secteur
                etatsante = EtatSante.objects.get(id=supprimer_e)
            except EtatSante.DoesNotExist:
                data = {"libelle": "Cet état de santé n'existe pas."}
                return JsonResponse({'data': data}, status=404)

            # Les données sont bonnes, on supprime l'état de santé du membre
            etatsante.delete()

            # On récupère tous les états de santé du membre
            etatsantes = EtatSante.objects.filter(membre=membre).order_by('id')

            if etatsantes:
                data = [{'id': etatsante.id, 'typeetatsante': etatsante.typeetatsante.libelle.upper(),
                         'id_membre': id_membre_etatsante_s,
                         'dateenre': etatsante.dateenre.strftime('%d/%m/%Y')} for etatsante in etatsantes]

                return JsonResponse({'data': data}, status=200)

        else:
            data = {"libelle": "Veuillez renseigner les champs"}
            return JsonResponse({'data': data}, status=404)

    return HttpResponseRedirect(reverse('presentation:ajouter_secteuragricole'))


@login_required
@permission_required('vieprofessionnelle.add_membre', raise_exception=True)
def detail_parent_secteuragricole(request, id, id_retour):
    try:
        parent = Parent.objects.get(id=id)
    except Parent.DoesNotExist:
        messages.error(request, "Ce parent n'existe pas.")
        return HttpResponseRedirect(reverse('presentation:ajouter_secteuragricole'))

    typeetatsantes = TypeEtatSante.objects.order_by('id')
    etatsantes = EtatSante.objects.filter(parent=parent).order_by('id')

    context = {
        'title': "Détials état de santé du parent",
        'typeetatsantes': typeetatsantes,
        'etatsantes': etatsantes,
        'parent': parent,
        'id_retour': id_retour,
    }
    return render(request, 'presentation/detail_parent_secteuragricole.html', context)


@login_required
@permission_required('vieprofessionnelle.add_membre', raise_exception=True)
def ajouter_etatsante_parent(request):
    if request.method == "POST":
        id_parent_etatsante = request.POST.get('id_parent_etatsante', None)
        typeetatsante = request.POST.get('select_typeetatsante', None)
        dateenre = request.POST.get('dateenre_e', None)
        if id_parent_etatsante and typeetatsante and dateenre:

            try:
                # On récupère le membre
                parent = Parent.objects.get(id=id_parent_etatsante)
            except Parent.DoesNotExist:
                data = {"libelle": "Ce parent n'existe pas."}
                return JsonResponse({'data': data}, status=404)

            try:
                # On récupère le secteur
                typeetatsante = TypeEtatSante.objects.get(id=typeetatsante)
            except TypeEtatSante.DoesNotExist:
                data = {"libelle": "Ce type d'état de santé n'existe pas."}
                return JsonResponse({'data': data}, status=404)

            # Les données sont bonnes, on ajoute l'état de santé du parent
            objet_etatsante = EtatSante()
            objet_etatsante.membre = None
            objet_etatsante.parent = parent
            objet_etatsante.typeetatsante = typeetatsante
            objet_etatsante.dateenre = dateenre
            objet_etatsante.save()

            # On récupère tous les états de santé du parent
            etatsantes = EtatSante.objects.filter(parent=parent).order_by('id')

            if etatsantes:
                data = [{'id': etatsante.id, 'typeetatsante': etatsante.typeetatsante.libelle.upper(),
                         'id_parent': id_parent_etatsante,
                         'dateenre': etatsante.dateenre.strftime('%d/%m/%Y')} for etatsante in etatsantes]

                return JsonResponse({'data': data}, status=200)

        else:
            data = {"libelle": "Veuillez renseigner les champs"}
            return JsonResponse({'data': data}, status=404)

    return HttpResponseRedirect(reverse('presentation:ajouter_secteuragricole'))


@login_required
@permission_required('vieprofessionnelle.delete_membre', raise_exception=True)
def supprimer_etatsante_parent(request):
    if request.method == "GET":
        id_parent_etatsante_s = request.GET.get('id_parent_etatsante_s', None)
        supprimer_e = request.GET.get('supprimer_e', None)

        if id_parent_etatsante_s and supprimer_e:

            try:
                # On récupère le membre
                parent = Parent.objects.get(id=id_parent_etatsante_s)
            except Parent.DoesNotExist:
                data = {"libelle": "Ce parent n'existe pas."}
                return JsonResponse({'data': data}, status=404)

            try:
                # On récupère le secteur
                etatsante = EtatSante.objects.get(id=supprimer_e)
            except EtatSante.DoesNotExist:
                data = {"libelle": "Cet état de santé n'existe pas."}
                return JsonResponse({'data': data}, status=404)

            # Les données sont bonnes, on supprime l'état de santé du membre
            etatsante.delete()

            # On récupère tous les états de santé du membre
            etatsantes = EtatSante.objects.filter(parent=parent).order_by('id')

            if etatsantes:
                data = [{'id': etatsante.id, 'typeetatsante': etatsante.typeetatsante.libelle.upper(),
                         'id_membre': id_parent_etatsante_s,
                         'dateenre': etatsante.dateenre.strftime('%d/%m/%Y')} for etatsante in etatsantes]

                return JsonResponse({'data': data}, status=200)

        else:
            data = {"libelle": "Veuillez renseigner les champs"}
            return JsonResponse({'data': data}, status=404)

    return HttpResponseRedirect(reverse('presentation:ajouter_secteuragricole'))


@login_required
@permission_required('vieprofessionnelle.view_membre', raise_exception=True)
def imprimer_secteuragricole(request, id):
    if request.method == "GET":

        try:
            membre = Membre.objects.get(id=id)
        except Membre.DoesNotExist:
            messages.error(request, "Ce membre n'existe pas.")
            return HttpResponseRedirect(reverse('presentation:ajouter_secteuragricole'))

        # On lui ajoute la propriété
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
            membre.cooperative = MembreSecteurAgricole.objects.get(membre=membre, secteuragricole=membre.secteuragricole)
        except MembreSecteurAgricole.DoesNotExist:
            pass

        context = {
            'title': "Fiche d'identification Secteur Agricole",
            'membre': membre,
        }
        return render(request,'presentation/imprimer_secteuragricole.html', context)

    return HttpResponseRedirect(reverse('presentation:ajouter_secteuragricole'))

# Fin de la Gestion du secteur agricole ------------------------------------------------------------------------------


# Gestion du secteur femme active ------------------------------------------------------------------------------------
@login_required
@permission_required('vieprofessionnelle.add_membre', raise_exception=True)
def ajouter_secteurfemmeactive(request):

    # Les variables
    il_existe = True
    global _active_session

    if request.method == "POST":
        # On récupère les données
        sexe = request.POST.get('sexe', None)
        nom = strip_tags(request.POST.get('nom', None)).strip().title() # On rétire les tag (<>) et on enleve les espaces au début et fin
        prenoms = strip_tags(request.POST.get('prenoms', None)).strip().title()
        nomjeunefille = strip_tags(request.POST.get('nomjeunefille', None)).strip().title()
        date_naissance = request.POST.get('date_naissance', None)
        lieu_naissance = request.POST.get('lieu_naissance', None)
        typepiece = request.POST.get('typepiece', None)
        numeropiece = strip_tags(request.POST.get('numeropiece', None)).strip()
        nationalite = request.POST.get('nationalite', None)
        contact = strip_tags(request.POST.get('contact', None)).strip()
        groupement = request.POST.get('groupement', None)
        dateadhesion = request.POST.get('dateadhesion', None)
        numero_carte = strip_tags(request.POST.get('numero_carte', None)).strip()
        typeresponsabilite = request.POST.get('typeresponsabilite', None)
        montantfinancement = request.POST.get('montantfinancement', None)
        chapeau = request.POST.get('chapeau', None)
        personne_ressource = request.POST.get('personne_ressource', None)
        niveauscolaire = request.POST.get('niveauscolaire', None)
        situationmatrimoniale = request.POST.get('situationmatrimoniale', None)
        lieu_habitation = request.POST.get('lieu_habitation', None)

        print('sexe',sexe)
        print('nom',nom)
        print('prenoms',prenoms)
        print('nomjeunefille',nomjeunefille)
        print('date_naissance',date_naissance)
        print('lieu_naissance', lieu_naissance)
        print('typepiece',typepiece)
        print('numeropiece',numeropiece)
        print('nationalite',nationalite)
        print('contact',contact)
        print('groupement',groupement)
        print('dateadhesion',dateadhesion)
        print('numero_carte',numero_carte)
        print('typeresponsabilite',typeresponsabilite)
        print('montantfinancement',montantfinancement)
        print('chapeau',chapeau)
        print('personne_ressource',personne_ressource)
        print('niveauscolaire',niveauscolaire)
        print('situationmatrimoniale',situationmatrimoniale)
        print('lieu_habitation',lieu_habitation)

        if not date_naissance:
            date_naissance = None

        if not dateadhesion:
            dateadhesion = None

        if nom != 'None' and date_naissance and numeropiece != 'None' and contact != 'None' and\
                typepiece and groupement and lieu_habitation and sexe and\
                nationalite and lieu_naissance and niveauscolaire and \
                situationmatrimoniale and lieu_habitation and typeresponsabilite and montantfinancement and\
                chapeau and personne_ressource:

            if not request.session.get('id_membre'):  # On traite l'ajout
                # On vérifie si ce membre existe déjà car le numeropiece et le contact sont uniques
                try:
                    Membre.objects.get(numeropiece=numeropiece, contact=contact)
                    messages.error(request, "Ce membre existe déjà.")
                    il_existe = False
                except Membre.DoesNotExist:
                    # On vérifie si le numeropiece existe
                    try:
                        Membre.objects.get(numeropiece=numeropiece)
                        messages.error(request, "Ce numéro de pièce existe déjà.")
                        il_existe = False
                    except:
                        # On vérifie si le numéro de téléphone existe
                        try:
                            Membre.objects.get(contact=contact)
                            messages.error(request, "Ce contact existe déjà.")
                            il_existe = False
                        except:
                            objet_membre = Membre()
            else:  # On traite la modification
                # On vérifie si le membre à modifier existe
                try:
                    objet_membre = Membre.objects.get(id=request.session.get('id_membre'))
                except Membre.DoesNotExist:
                    messages.error(request, "Ce membre n'existe pas.")
                    il_existe = False

            if il_existe:  # Si la valeur est True on entre dans la condition
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
                    objet_membre.set_identifiant()
                    objet_membre.dateenre = datetime.date.today()

                objet_membre.actif = True  # On active l'utilisateur
                objet_membre.utilisateur = User.objects.get(id=request.user.id)

                # On sauvegarde les données
                objet_membre.save()

                if not request.session.get('id_membre'):

                    # On ajoute le secteur femme active en relation
                    MembreSecteurFemmeActive.objects.create(
                        membre=objet_membre,
                        secteurfemmeactive=SecteurFemmeActive.objects.get(id=groupement),
                        date_adhesion=dateadhesion,
                        numero_carte=numero_carte,
                        chapeau=Chapeau.objects.get(id=chapeau),
                        personneressource=PersonneRessource.objects.get(id=personne_ressource),
                        typeresponsabilite=TypeResponsabilite.objects.get(id=typeresponsabilite),
                        montantfinancement=MontantFinancement.objects.get(id=montantfinancement),

                    )

                    messages.success(request, "Enregistrement réussi")

                else:
                    try:
                        membresecteur = MembreSecteurFemmeActive.objects.get(membre=objet_membre)
                        membresecteur.secteurfemmeactive = SecteurFemmeActive.objects.get(id=groupement)
                        membresecteur.date_adhesion = dateadhesion
                        membresecteur.numero_carte = numero_carte
                        membresecteur.chapeau = Chapeau.objects.get(id=chapeau)
                        membresecteur.personneressource = PersonneRessource.objects.get(id=personne_ressource)
                        membresecteur.typeresponsabilite = TypeResponsabilite.objects.get(id=typeresponsabilite)
                        membresecteur.montantfinancement = MontantFinancement.objects.get(id=montantfinancement)
                        membresecteur.save()

                        messages.success(request, "Modification réussi")
                    except MembreSecteurFemmeActive.DoesNotExist:
                        pass
                    finally:
                        del request.session['id_membre']  # On détruit la variable

        else:
            messages.error(request, "Veuillez renseigner les champs.")


    # PARTIE DU GET -----------------------
    if not _active_session:
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
    secteuragricoles = SecteurFemmeActive.objects.order_by("nom")
    typeparents = TypeParent.objects.order_by("libelle")
    parents = Parent.objects.order_by("nomprenoms")
    membres = Membre.objects.filter(utilisateur_id=request.user.id, actif=True, secteurfemmeactive=F('secteurfemmeactive')).order_by('nom_prenoms')
    typeresponsabilites = TypeResponsabilite.objects.order_by('id')
    montantfinancements = MontantFinancement.objects.order_by('id')
    chapeaux = Chapeau.objects.order_by('-id')
    typepersonneressources = TypePersonneRessource.objects.order_by('id')
    quantitegroupements = QuantiteGroupement.objects.order_by('id')
    groupements = SecteurFemmeActive.objects.order_by('nom')

    # On détermine le nombre de places disponibles par groupement
    nombre_places = []
    nouveau_groupement = []

    for groupement in groupements:
        nbg = MembreSecteurFemmeActive.objects.filter(secteurfemmeactive=groupement).count()
        if groupement.quantitegroupement.quantite > nbg:
            # On ajoute le groupement dans la nouvelle liste
            nouveau_groupement.append(groupement)
            # On ajoute le nombre de places disponibles
            nombre_places.append(groupement.quantitegroupement.quantite - nbg)

    # On initialise le nouveau groupement
    groupements = nouveau_groupement


    # On initialise les données
    _parametre = Parametre.objects.first()
    chapeaux_liste = None
    membres_chapeau = None
    for typepersonneressource in typepersonneressources:
        if typepersonneressource.id == int(_parametre.id_chapeau):
            # On récupère la liste des personnes ressources de type chapeau
            chapeaux_liste = PersonneRessource.objects.filter(typepersonneressource=typepersonneressource)
        else:
            # On récupère la liste des personnes ressources de type membre
            membres_chapeau = PersonneRessource.objects.filter(typepersonneressource=typepersonneressource)

    # Initialisation de l'affichage de l'onglet active
    active_secteurfemmeactive = ['', 'false', '']
    active_liste = ['', 'false', '']

    if _active_onglet == "active_secteurfemmeactive":
        active_secteurfemmeactive = ['active', 'true', 'show active']
    elif _active_onglet == "active_liste":
        active_liste = ['active', 'true', 'show active']
    else:
        # Affichage par défaut
        active_secteurfemmeactive = ['active', 'true', 'show active']


    context = {
        'titre': "Identification - Secteur Femme Active",
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
        "typeresponsabilites": typeresponsabilites,
        "montantfinancements": montantfinancements,
        "chapeaux": chapeaux,
        "chapeaux_liste": chapeaux_liste,
        "typepersonneressources": typepersonneressources,
        "membres_chapeau": membres_chapeau,
        "id_chapeau": int(_parametre.id_chapeau),
        "quantitegroupements": quantitegroupements,
        "groupements": groupements,
        "nombre_places": nombre_places,

        "active_secteurfemmeactive": active_secteurfemmeactive,
        "active_liste": active_liste,
    }

    if request.session.get('id_membre'):  # On affiche la page de modification
        # On récupère le membre
        context["membre_actif"] = Membre.objects.get(id=request.session.get('id_membre'))
        context["membre_secteurfemmeactive"] = MembreSecteurFemmeActive.objects.get(membre_id=request.session.get('id_membre'))
        return render(request, "presentation/secteurfemmeactive/modifier_secteurfemmeactive.html", context)

    return render(request, "presentation/secteurfemmeactive/secteurfemmeactive.html", context)


@login_required
@permission_required('vieprofessionnelle.add_membre', raise_exception=True)
def detail_secteurfemmeactive(request, id):
    try:
        membre = Membre.objects.get(id=id)
    except Membre.DoesNotExist:
        messages.error(request, "Ce membre n'existe pas.")
        return HttpResponseRedirect(reverse('presentation:ajouter_secteurfemmeactive'))

    typesecteurs = TypeSecteur.objects.order_by('id')
    secteurs = Secteur.objects.filter(membre=membre).order_by('secteur')
    typedocuments = TypeDocument.objects.order_by('id')
    documents = Document.objects.filter(membre=membre).order_by('id')
    parents_membre = Parent.objects.filter(membre=membre).order_by('id')
    parents = Parent.objects.order_by('id')
    typeparents = TypeParent.objects.order_by('id')
    typeetatsantes = TypeEtatSante.objects.order_by('id')
    etatsantes = EtatSante.objects.filter(membre=membre).order_by('id')

    context = {
        'title': "Détials du membre",
        'membre': membre,
        'typesecteurs': typesecteurs,
        'secteurs': secteurs,
        'typedocuments': typedocuments,
        'documents': documents,
        'parents_membre': parents_membre,
        'parents': parents,
        'typeparents': typeparents,
        'typeetatsantes': typeetatsantes,
        'etatsantes': etatsantes,
        'id_retour': 2,  # Variable pour le lien de retour vers la liste des membres
    }
    return render(request, 'presentation/details_secteur_agricole.html', context)


@login_required
@permission_required('vieprofessionnelle.change_membre', raise_exception=True)
def modifier_secteurfemmeactive(request, id):
    global _active_onglet
    global _active_session

    _active_session = True
    _active_onglet = "active_secteurfemmeactive"  # On initialise la variable
    request.session['id_membre'] = id

    return HttpResponseRedirect(reverse('presentation:ajouter_secteurfemmeactive'))


@login_required
@permission_required('vieprofessionnelle.delete_membre', raise_exception=True)
def supprimer_secteurfemmeactive(request, id):
    global _active_onglet
    _active_onglet = "active_liste"  # On initialise la variable

    try:
        objet_membre = Membre.objects.get(id=id)
    except Membre.DoesNotExist:
        messages.error(request, "Ce membre n'existe pas.")
        return HttpResponseRedirect(reverse('presentation:ajouter_secteurfemmeactive'))

    if objet_membre:
        objet_membre.actif = False
        objet_membre.save()

        messages.info(request, "Suppression réussie.")

    return HttpResponseRedirect(reverse('presentation:ajouter_secteurfemmeactive'))


@login_required
@permission_required('vieprofessionnelle.view_membre', raise_exception=True)
def imprimer_secteurfemmeactive(request, id):
    if request.method == "GET":

        try:
            membre = Membre.objects.get(id=id)
        except Membre.DoesNotExist:
            messages.error(request, "Ce membre n'existe pas.")
            return HttpResponseRedirect(reverse('presentation:ajouter_secteurfemmeactive'))

        # On lui ajoute la propriété
        membre.get_region = membre.get_region()
        membre.groupement = membre.secteurfemmeactive_set.first()
        #membre.nombrefemme = membre.get_nombre_parent('Femme')
        membre.nombreenfant = membre.get_nombre_parent('Enfant')
        membre.lieu_habitation = membre.get_lieu_habitation()
        membre.secteuractivite = membre.secteurs.first()
        try:
            document = Document.objects.get(membre=membre)
            membre.photo = document.get_photo_membre()
        except Document.DoesNotExist:
            pass
        try:
            membre.secteurfemmeactive = MembreSecteurFemmeActive.objects.get(membre=membre, secteurfemmeactive=membre.groupement)
            membre.personneressource_contact = membre.secteurfemmeactive.personneressource.get_personneressource_contact()
        except MembreSecteurFemmeActive.DoesNotExist:
            pass

        context = {
            'title': "Fiche d'identification Secteur Femme Active",
            'membre': membre,
        }
        return render(request, 'presentation/secteurfemmeactive/imprimer_secteurfemmeactive.html', context)

    return HttpResponseRedirect(reverse('presentation:ajouter_secteurfemmeactive'))


# Fin de la Gestion du secteur agricole -------------------------------------
