from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User, Permission, Group
from django.contrib.contenttypes.models import ContentType
from .forms import InscriptionForm, ConnexionForm, ModifierUtilisateurForm, GroupeForm
from .models import LISTE_MODELS
from django.core.paginator import Paginator
from django.utils.html import strip_tags

# Les Constantes
_PAS = 10  # pas de la pagination

# Les Views---------------------------------------------------


def inscription(request, ajouter_utilisateur=0):

    # On crée un formulaire vide
    form = InscriptionForm()

    context = {
        'titre': "S'inscrire",
        'form': form,
        'ajouter_utilisateur': ajouter_utilisateur
    }

    if request.method == "POST":

        # On crée un formulaire avec les données de l'utilisateur
        form = InscriptionForm(request.POST)

        # On vérifie si le formulaire est valide
        if form.is_valid():

            # On crée un nouvel utilisateur
            user = User.objects.create_user(username=form.cleaned_data['username'], password=form.cleaned_data['password1'], email=form.cleaned_data['email'])
            #user = User.objects.create_superuser(username = form.cleaned_data['username'],password = form.cleaned_data['password1'], email= form.cleaned_data['email'])

            # On effectue une redirection en fonction du paramètre.
            if ajouter_utilisateur:
                # On effectue une redirection vers la vue utilisateur
                return HttpResponseRedirect(reverse('utilisateur:utilisateur'))

            # On effectue une redirection
            return HttpResponseRedirect(reverse('utilisateur:connexion'))
        else:
            context['form'] = form


    return render(request,'utilisateur/inscription.html',context)

def connexion(request):

    default = {}  # On crée la variable d'initialisation
    checked = ""  # On crée la variable pour la case à cocher se souvenir de moi
    utilisateur = None

    # On récupère l'id utilisateur stocké dans le cookie
    if request.COOKIES.get('id_utilisateur'):
        # On récupère les données de l'utilisateur
        try:
            utilisateur = User.objects.get(id=request.COOKIES['id_utilisateur'])
        except User.DoesNotExist:
            pass

        if utilisateur is not None:
            default = {'username': utilisateur.username, 'password1': utilisateur.password}
            checked = "checked"

    # On crée un formulaire et on l'initialise selon l'existence du cookie
    form = ConnexionForm(initial=default)

    context = {
        'titre': "Se connecter",
        'form': form,
        'checked': checked
    }

    if request.method == "POST":

        # On authentifie l'utilisateur
        user = authenticate(request, username=strip_tags(request.POST['username']).strip(), password=strip_tags(request.POST['password1']))

        # On crée un formulaire avec les données du formulaire
        form = ConnexionForm(request.POST)

        # on initialise user = utilisateur pour connecter directement l'utilisateur au cas ou
        # le cookie id utilisateur existe
        if utilisateur is not None and user is None:
            user = utilisateur

        # On vérifie si l'utilisateur existe
        if user is not None:
            # On connecte l'utilisateur
            login(request, user)

            # On vérifie si la case se souvenir de moi est coché et on ajoute l'id utilisateur
            # dans la variable session pour créer un cookie pour sauvegarder l'id de l'utilisateur
            # sans la vue index de l'application presentation

            if request.POST.get('se_souvenir', ''):
                request.session['user_id'] = user.id

            # On effectue une redirection vers le tableau de bord
            return HttpResponseRedirect(reverse('presentation:index'))
        else:
            context['message'] = "L'identifiant n'est pas valide."
            context['form'] = form

    return render(request, 'utilisateur/connexion.html', context)

def deconnexion(request):
    logout(request)
    # On le redirige vers la page de connexion
    return HttpResponseRedirect(reverse('utilisateur:connexion'))


@login_required
@permission_required('auth.view_user', raise_exception=True)
def utilisateur(request):
    # On récupère la liste des 10 derniers utilisateurs
    Liste_utilisateurs = User.objects.all().order_by('-id')
    pagination = Paginator(Liste_utilisateurs, _PAS) # On crée l'objet pagination avec la liste des utilisateurs

    numero_page = request.GET.get('page', 1) # On récupère le numéro de la page sélectionnée
    page_obj = pagination.get_page(numero_page)

    total_pages = pagination.count

    context = {
        'titre': "Liste des utilisateurs",
        'page_obj': page_obj,
        'total_pages': total_pages
    }
    return render(request, 'utilisateur/utilisateur.html', context)

@login_required
@permission_required('auth.view_user', raise_exception=True)
def detail_utilisateur(request, id):
    # Les variables
    # on vérifie si l'utilisateur existe et on le récupère
    try:
        utilisateur = User.objects.get(id=id)
    except User.DoesNotExist:
        # On effectue une redirection
        # On gère le message d'erreur
        return HttpResponseRedirect(reverse('utilisateur:utilisateur'))

    # On récupère la liste des derniers groupes de l'utilisateur
    Liste_groupe = utilisateur.groups.all().order_by('name')
    pagination = Paginator(Liste_groupe, _PAS)  # On créé l'objet pagination avec la liste des utilisateurs

    numero_page = request.GET.get('page', 1)  # On récupère le numéro de la page sélectionnée
    page_obj = pagination.get_page(numero_page)

    total_pages = pagination.count

    # Gestion des permissions
    data = {}
    for app, donnees in LISTE_MODELS.items():  # On parcourt les apps
        models = {}
        for key, model in donnees.items():  # On parcourt les models
            # On récupère la liste des permissions du modèle
            content_type = ContentType.objects.get_for_model(model)
            mes_permissions = Permission.objects.filter(content_type=content_type)

            # On ajoute les permissions au groupe
            if request.method == 'POST':
                if request.POST.get('permissions_utilisateur',None) is not None:
                   for permission in mes_permissions:
                       if request.POST.get(permission.codename, None) is not None:
                           utilisateur.user_permissions.add(permission)  # On ajoute la permission
                       else:
                            utilisateur.user_permissions.remove(permission)  # On supprime la permission

            # On créé un tableau de tableau en ajoutant le name et le codename. on remplace Can, add, change, delete, view
            # par les mots en français

            # On récupère la liste des permissions de l'utilisateur
            liste_permissions = utilisateur.user_permissions.all()
            checked = ""  #  Variable pour l'activation ou la désactivation de la case à cocher de la permission dans le gabarit

            permissions = []  # On initialise la variable

            for permission in mes_permissions:
                name = permission.name.replace("Can", "Peut").\
                    replace("add", "Ajouter").\
                    replace("view", "Afficher").\
                    replace("change", "Modifier").\
                    replace("delete", "Supprimer")

                code = permission.codename
                if permission in liste_permissions:
                    checked = "checked"
                else:
                    checked = ""

                permissions.append([name, checked, code])

            # On ajoute la liste de droit de chaque modèle
            models[key] = permissions

        # On ajoute chaque dictionnaire de modèle dans son application
        data[app] = models

    context = {
        'titre': "Détail de l'utilisateur",
        'utilisateur': utilisateur,
        'page_obj': page_obj,
        'total_pages': total_pages,
        'data': data,
    }

    return render(request, 'utilisateur/detail_utilisateur.html', context)

@login_required
@permission_required('auth.delete_user', raise_exception=True)
def supprimer_groupe_utilisateur(request, id):
    # On récupère l'utilisateur à supprimer
    if request.method == 'POST':
        # On récupère l'id du groupe
        id_groupe = request.POST.get("id_groupe", 0)
        if not id_groupe:
            # On effectue une redirection
            # On gère le message d'erreur
            return HttpResponseRedirect(reverse('presentation:index'))

        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            # On effectue une redirection
            # On gère le message d'erreur
            return HttpResponseRedirect(reverse('utilisateur:detail_utilisateur', args={id}))


        # on vérifie si le groupe existe et on le récupère
        try:
            groupe = Group.objects.get(id=int(id_groupe))
        except Group.DoesNotExist:
            # On effectue une redirection
            # On gère le message d'erreur
            return HttpResponseRedirect(reverse('utilisateur:utilisateur'))

        # On supprime l'utilisateur du groupe
        groupe.user_set.remove(user)
        # On effectue une redirection
        return HttpResponseRedirect(reverse('utilisateur:detail_utilisateur', args={id}))

    # On effectue une redirection
    return HttpResponseRedirect(reverse('utilisateur:connexion'))

@login_required
@permission_required('auth.delete_user', raise_exception=True)
def supprimer_utilisateur(request, id):
    # on vérifie si l'utilisateur à supprimer existe et on le supprime
    try:
        utilisateur = User.objects.get(id=id)
        utilisateur.is_actif = False  # On désactive l'utilisateur au lieu de le supprimer avec utilisateur.delete()
        utilisateur.save()

    except User.DoesNotExist:
        # Gerer le message d'erreur
        pass

    # Gerer l'affichage du message de suppression réussie

    # On effectue une redirection
    return HttpResponseRedirect(reverse('utilisateur:utilisateur'))

@login_required
@permission_required('auth.change_user', raise_exception=True)
def modifier_utilisateur(request, id):

    context = {
        'titre': "Modifier les données de l'utilisateur"
    }

    # On récupère l'utilisateur à modifier
    try:
        utilisateur = User.objects.get(id=id)
    except User.DoesNotExist:
        # On effectue une redirection pour indiquer que l'utilisateur n'existe pas
        # Gerer le message d'erreur
        return HttpResponseRedirect(reverse('utilisateur:utilisateur'))

    context['utilisateur'] = utilisateur

    if request.method == 'GET':

        # On crée un formulaire avec les données de l'utilisateur
        form = ModifierUtilisateurForm()
        form.username = utilisateur.username
        form.first_name = utilisateur.first_name
        form.last_name = utilisateur.last_name
        form.email = utilisateur.email
        form.id = utilisateur.id

        context['form'] = form

        return render(request, 'utilisateur/modifier_utilisateur.html', context)
    else:
        # On crée un formulaire avec les données de l'utilisateur
        form = ModifierUtilisateurForm(request.POST)

        # On vérifie si le nom d'utilisateur a changer
        nom_utilisateur = request.POST.get('username', '')

        if utilisateur.username == nom_utilisateur:

            # On modifie les données de l'utilisateur
            utilisateur.first_name = request.POST.get('first_name', '')
            utilisateur.last_name = request.POST.get('last_name', '')
            utilisateur.email = request.POST.get('email', '')

            utilisateur.save()

            # On effectue une redirection
            return HttpResponseRedirect(reverse('utilisateur:utilisateur'))
        else:
            if nom_utilisateur:

                # On vérifie si le nom d'utilisateur existe déjà
                try:
                    # On essaie de voir si l'utilisateur existe
                    User.objects.get(username=nom_utilisateur)

                    # l'utilisateur existe déjà
                    context['message'] = "Ce nom d'utilisateur : {0} existe déjà.".format(nom_utilisateur)
                    context['form'] = form
                    return render(request, 'utilisateur/modifier_utilisateur.html', context)

                except User.DoesNotExist:
                    # On modifie les données de l'utilisateur
                    utilisateur.username = nom_utilisateur
                    utilisateur.first_name = request.POST.get('first_name', '')
                    utilisateur.last_name = request.POST.get('last_name', '')
                    utilisateur.email = request.POST.get('email', '')

                    utilisateur.save()

                    # On effectue une redirection
                    return HttpResponseRedirect(reverse('utilisateur:utilisateur'))

            else:

                context['message'] = "Veuillez saisir le nom d'utilisateur."
                context['form'] = form
                return render(request, 'utilisateur/modifier_utilisateur.html', context)

@login_required
@permission_required('auth.view_group', raise_exception=True)
def groupe(request):
    # On récupère la liste des 10 derniers groupes
    Liste_groupes = Group.objects.all().order_by('-id')

    pagination = Paginator(Liste_groupes, _PAS)  # On créé l'objet pagination avec la liste des groupes

    numero_page = request.GET.get('page', 1)  # On récupère le numéro de la page sélectionnée
    page_obj = pagination.get_page(numero_page)

    total_pages = pagination.count

    context = {
        'titre': "Liste des groupes",
        'page_obj': page_obj,
        'total_pages': total_pages
    }
    return render(request, 'utilisateur/groupe.html', context)

@login_required
@permission_required('auth.add_group', raise_exception=True)
def ajouter_groupe(request):
    # On créé un formulaire vide
    form = GroupeForm()

    context = {
        'titre': "Ajouter un nouveau groupe",
        'form': form
    }

    if request.method == "POST":

        # On créé un formulaire avec les données de l'utilisateur
        form = GroupeForm(request.POST)

        # On vérifie si le formulaire est valide
        if form.is_valid():
            # on récupère le nom du groupe
            groupe_name = form.cleaned_data['name'].upper()

            # on vérifie si le groupe existe déjà
            try:
                groupe = Group.objects.get(name=groupe_name)
            except Group.DoesNotExist:
                groupe = None

            if groupe is None:
                # On créé un nouveau groupe
                Group.objects.create(name=groupe_name)

                # On effectue une redirection
                return HttpResponseRedirect(reverse('utilisateur:groupe'))
            else:
                context['message'] = 'Ce nom : {0} existe déjà.'.format(groupe_name)
                context['form'] = form

        else:
            name = request.POST['name']
            context['message'] = 'Ce nom : {0} existe déjà.'.format(name)
            context['form'] = form

    return render(request, 'utilisateur/ajouter_groupe.html', context)

@login_required
@permission_required('auth.delete_group', raise_exception=True)
def supprimer_groupe(request, id):
    # on vérifie si le groupe à supprimer existe et on le supprime
    try:
        groupe = Group.objects.get(id=id)
        groupe.delete()

    except Group.DoesNotExist:
        # On gere les erreurs
        pass

    # On effectue une redirection
    return HttpResponseRedirect(reverse('utilisateur:groupe'))

@login_required
@permission_required('auth.view_group', raise_exception=True)
def detail_groupe(request, id):
    # Les variables
    recherche_utilisateur = ""

    # on vérifie si le groupe existe et on le récupère
    try:
        groupe = Group.objects.get(id=id)
    except Group.DoesNotExist:
        # On effectue une redirection
        # On gère le message
        return HttpResponseRedirect(reverse('utilisateur:groupe'))

    # On récupère la liste des derniers utilisateurs
    Liste_utilisateurs = User.objects.all().order_by('-id')
    pagination = Paginator(Liste_utilisateurs, _PAS)  # On créé l'objet pagination avec la liste des utilisateurs

    numero_page = request.GET.get('page', 1)  # On récupère le numéro de la page sélectionnée
    page_obj = pagination.get_page(numero_page) # On récupère la liste des objets selon le numéro de la page

    total_pages = pagination.count

    # On récupère chaque utilisateur sélectionné
    if request.method == 'POST':

        # on récupère les utilisateurs selon la recherche
        recherche_utilisateur = request.POST.get('recherche_utilisateur', '')
        if recherche_utilisateur:
            Liste_utilisateurs = User.objects.filter(username__icontains = recherche_utilisateur).order_by('username')
            pagination = Paginator(Liste_utilisateurs, _PAS)  # On créé l'objet pagination avec la liste des utilisateurs

            numero_page = request.GET.get('page', 1)  # On récupère le numéro de la page sélectionnée
            page_obj = pagination.get_page(numero_page)

            total_pages = pagination.count

        user = None
        for i in range(1, len(page_obj) + 1):
            try:
                user = User.objects.get(id=request.POST.get(str(i), 0))

                # On ajoute l'utilisateur dans le groupe
                groupe.user_set.add(user)

            except User.DoesNotExist:
                pass



    # On récupère la liste des utilisateurs du groupe
    gpage_obj = {}
    total_gpages = 0

    liste_utilisateur_groupe = groupe.user_set.all().order_by('username')
    if liste_utilisateur_groupe.count():
        pagination = Paginator(liste_utilisateur_groupe, _PAS)  # On créé l'objet pagination avec la liste des utilisateurs

        numero_page = request.GET.get('gpage', 1)  # On récupère le numéro de la page sélectionnée
        gpage_obj = pagination.get_page(numero_page)

        total_gpages = pagination.count

    # Gestion des permissions
    data = {}
    for app, donnees in LISTE_MODELS.items():  # On parcours les apps
        models = {}
        for key, model in donnees.items():  # On parcours les models
            # On récupère la liste des permissions du modèle
            content_type = ContentType.objects.get_for_model(model)
            mes_permissions = Permission.objects.filter(content_type=content_type)

            # On ajoute les permissions au groupe
            if request.method == 'POST':
                if request.POST.get('permissions_groupe',None) is not None:
                   for permission in mes_permissions:
                       if request.POST.get(permission.codename, None) is not None:
                           groupe.permissions.add(permission) # On ajoute la permission
                       else:
                            groupe.permissions.remove(permission) # On supprime la permission

            # On créé un tableau de tableau en ajoutant le name et le codename. on remplace Can, add, change, delete, view poar les mots en français
            #permissions = [[permission.name.replace("Can", "Peut").replace("add", "Ajouter").replace("view","Afficher").replace("change", "Modifier").replace("delete", "Supprimer"), permission.codename] for permission in mes_permissions]

            # On récupère la liste des permission du groupe
            liste_permissions = groupe.permissions.all()
            checked = "" # Variable pour l'activation ou la désactivation de la case à cocher de la permission dans le gabarit

            permissions = [] # On initialise la variable

            for permission in mes_permissions:
                name = permission.name.replace("Can", "Peut").replace("add", "Ajouter").replace("view","Afficher").replace("change", "Modifier").replace("delete", "Supprimer")
                code = permission.codename
                if permission in liste_permissions:
                    checked = "checked"
                else:
                    checked = ""

                permissions.append([name,checked,code])

            # On ajoute la liste de droit de chaque modèle
            models[key] = permissions

        # On ajoute chaque dictionnaire de modèle dans son application
        data[app] = models

    context = {
        'titre': "Détail du groupe",
        'groupe': groupe,
        'gpage_obj': gpage_obj,
        'total_gpages': total_gpages,
        'page_obj': page_obj,
        'total_pages': total_pages,
        'recherche_utilisateur': recherche_utilisateur,
        'data':data
    }

    return render(request, 'utilisateur/detail_groupe.html', context)

@login_required
@permission_required('auth.delete_group', raise_exception=True)
def supprimer_utilisateur_groupe(request, id):
    # On récupère l'utilisateur à supprimer
    if request.method == 'POST':
        # On récupère l'id du groupe
        id_groupe = request.POST.get("id_groupe", 0)
        if not id_groupe:
            # On effectue une redirection
            # On gère le message d'erreur
            return HttpResponseRedirect(reverse('presentation:index'))

        try:
            user = User.objects.get(id = id)
        except User.DoesNotExist:
            # On effectue une redirection
            # On gère le message d'erreur
            return HttpResponseRedirect(reverse('utilisateur:detail_groupe', args={id_groupe}))


        # on vérifie si le groupe existe et on le récupère
        try:
            groupe = Group.objects.get(id=id_groupe)
        except Group.DoesNotExist:
            # On effectue une redirection
            # On gère le message d'erreur
            return HttpResponseRedirect(reverse('utilisateur:groupe'))

        # On supprime l'utilisateur du groupe
        groupe.user_set.remove(user)
        # On effectue une redirection
        return HttpResponseRedirect(reverse('utilisateur:detail_groupe', args={id_groupe}))

    # On effectue une redirection
    return HttpResponseRedirect(reverse('utilisateur:connexion'))

@login_required
@permission_required('auth.change_group', raise_exception=True)
def modifier_groupe(request, id):

    context = {
        'titre': "Modifier les données du groupe"
    }

    # On récupère le groupe à modifier
    try:
        groupe = Group.objects.get(id=id)
    except Group.DoesNotExist:
        # On effectue une redirection pour indiquer que le groupe n'existe pas
        # On gere les erreurs
        return HttpResponseRedirect(reverse('utilisateur:groupe'))

    context['groupe'] = groupe

    if request.method == 'GET':

        # On créé un formulaire avec les données du groupe
        form = GroupeForm()
        form.name = groupe.name
        form.id = groupe.id

        context['form'] = form

        return render(request,'utilisateur/modifier_groupe.html', context)
    else:
        # On crée un formulaire avec les données du groupe
        form = GroupeForm(request.POST)

        # On vérifie si le nom du groupe a changer
        nom_groupe = request.POST.get('name', '').upper()

        if groupe.name == nom_groupe:

            # On ne fait rien, on effectue une redirection
            # On gere le message d'erreur
            return HttpResponseRedirect(reverse('utilisateur:groupe'))
        else:
            if nom_groupe:

                # On vérifie si le nom du groupe existe déjà
                try:
                    Group.objects.get(name = nom_groupe)
                except Group.DoesNotExist:
                    # On modifie les données du groupe
                    groupe.name = nom_groupe

                    groupe.save()

                    # On effectue une redirection
                    # On gere le message de confirmation
                    return HttpResponseRedirect(reverse('utilisateur:groupe'))

                # l'utilisateur existe déjà
                context['message'] = "Ce nom du groupe : {0} existe déjà.".format(nom_groupe)
                context['form'] = form
                return render(request, 'utilisateur/modifier_groupe.html', context)

            else:

                context['message'] = "Veuillez saisir le nom du groupe."
                context['form'] = form
                return render(request, 'utilisateur/modifier_groupe.html', context)

@login_required
@permission_required('auth.change_user', raise_exception=True)
def motdepasse(request, id):

    utilisateur_identique = False
    # On vérifie si l'utilisateur en cours est le même utilisateur qui veut modifier le mot de passe
    if int(request.user.id) == int(id):
        utilisateur_identique = True

    context = {
        'titre': "Changer de mot de passe",
        'utilisateur_identique': utilisateur_identique
    }

    # On récupère l'utilisateur
    try:
        utilisateur = User.objects.get(id=id)
    except User.DoesNotExist:
        # On effectue une redirection pour indiquer que l'utilisateur n'existe pas
        # On gère l'erreur
        return HttpResponseRedirect(reverse('utilisateur:utilisateur'))

    context['utilisateur'] = utilisateur

    if request.method == 'POST':
        # On vérifie si les mots de passes ont été saisies
        motdepasse_actuel = ""
        nouveau_motdepasse = ""
        confirmation_motdepasse = ""

        motdepasse_actuel = request.POST.get('passwordactuel', '')
        nouveau_motdepasse = request.POST.get('password1', '')
        confirmation_motdepasse = request.POST.get('password2', '')

        # On vérifie si le mot de passe actuel existe
        if utilisateur_identique:
            if not motdepasse_actuel:
                context['message'] = "Veuillez saisir le mot de passe actuel"
                return render(request, 'utilisateur/motdepasse.html', context)
            else:
                # On vérifie si le mot de passe actuel saisie est correcte
                user = authenticate(request, username=request.POST.get('username', ''), password=motdepasse_actuel)

                if user is not None:
                    # On vérifie si les deux mots de passes sont correctes
                    if not nouveau_motdepasse:
                        context['message'] = "Veuillez saisir le nouveau mot de passe"
                        return render(request, 'utilisateur/motdepasse.html', context)
                    else:
                        if nouveau_motdepasse == confirmation_motdepasse:
                            # On change le mot de passe
                            utilisateur.set_password(nouveau_motdepasse)
                            utilisateur.save()

                            request.session['success'] = "Mot de passe modifié avec succès. Veuillez vous identifier"  # Pour l'affichage du toast dans connexion
                            # On effectue une redirection vers le tableau de bord
                            return HttpResponseRedirect(reverse('utilisateur:deconnexion'))
                        else:
                            context['message'] = "Le mot de passe de confirmation est incorrecte"
                            return render(request, 'utilisateur/motdepasse.html', context)

                else:
                    context['message'] = "Le mot de passe actuel est incorrecte"
                    return render(request, 'utilisateur/motdepasse.html', context)
        else:
            if nouveau_motdepasse == confirmation_motdepasse:
                # On change le mot de passe
                utilisateur.set_password(nouveau_motdepasse)
                utilisateur.save()

                request.session['success'] = "Mot de passe modifié avec succès"  # Pour l'affichage du toast dans l'index
                # On effectue une redirection vers le tableau de bord
                return HttpResponseRedirect(reverse('utilisateur:utilisateur'))
            else:
                context['message'] = "Le mot de passe de confirmation est incorrecte"
                return render(request, 'utilisateur/motdepasse.html', context)

    return render(request, 'utilisateur/motdepasse.html', context)


# ---- Gestion des erreurs --------------------------
def handler404(request, exception):

    context = {
        'titre': 'ERREUR 404',
        'message': "La page que vous désirez n'existe pas",
    }

    return render(request, 'erreur/erreur.html', status=404, context=context)

def handler500(request):

    context = {
        'titre': 'ERREUR 500',
        'message': "Le serveur ne parvient pas à traiter votre requête",
    }

    return render(request, 'erreur/erreur.html', status=500, context=context)

def handler400(request, exception):

    context = {
        'titre': 'ERREUR 400',
        'message': "Votre requête est erronée",
    }

    return render(request,'erreur/erreur.html', status=400, context=context)

def handler403(request, exception):

    context = {
        'titre': 'ERREUR 403',
        'message': "Vous n'avez pas accès à cette ressource",
    }

    return render(request, 'erreur/erreur.html', status=403, context=context)

# ---- Fin de la Gestion des erreurs ----------------
