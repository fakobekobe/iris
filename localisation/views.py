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
def localisation(request):

    districts = District.objects.all().order_by("libelle")
    regions = Region.objects.all().order_by("libelle")
    departements = Departement.objects.all().order_by("libelle")
    villes = Ville.objects.all().order_by("libelle")
    communes = Commune.objects.all().order_by("libelle")
    quartiers = Quartier.objects.all().order_by("libelle")
    marches = Marche.objects.all().order_by("libelle")

    # Initialisation de l'affichage de l'onglet active
    active_district = ['','false','']
    active_region = ['','false','']
    active_departement = ['','false','']
    active_ville = ['','false','']
    active_commune = ['','false','']
    active_quartier = ['','false','']
    active_marche = ['','false','']

    if _active_onglet == "district":
        active_district =  ['active', 'true', 'show active']
    elif _active_onglet == "region":
        active_region = ['active', 'true', 'show active']
    elif _active_onglet == "departement":
        active_departement = ['active', 'true', 'show active']
    elif _active_onglet == "ville":
        active_ville = ['active', 'true', 'show active']
    elif _active_onglet == "commune":
        active_commune = ['active', 'true', 'show active']
    elif _active_onglet == "quartier":
        active_quartier = ['active', 'true', 'show active']
    elif _active_onglet == "marche":
        active_marche = ['active', 'true', 'show active']
    else:
        # Affichage par défaut
        active_district =  ['active', 'true', 'show active']


    context = {
        "titre" : "Localisation",
        "districts" : districts,
        "regions" : regions,
        "departements" : departements,
        "villes": villes,
        "communes": communes,
        "quartiers": quartiers,
        "marches": marches,

        "active_district": active_district,
        "active_region": active_region,
        "active_departement": active_departement,
        "active_ville": active_ville,
        "active_commune": active_commune,
        "active_quartier": active_quartier,
        "active_marche": active_marche,

    }

    return render(request, "localisation/localisation.html", context)

# Gestion du district -----------------------------------------------

@login_required
@permission_required('localisation.add_district', raise_exception=True)
def ajouter_district(request):

    global _active_onglet
    _active_onglet = "district"  # On initialise la variable

    if request.method == "POST":
        # On initialise les variables
        code = request.POST.get("code", None)
        libelle = request.POST.get("libelle", None)

        if code and libelle:
            # On vérifie si le code et le libelle existe
            # On format les chaine
            libelle = libelle.capitalize()

            try:
                district = District.objects.get(code = code)
                messages.error(request, f"Ce code :[{code}] existe déjà.")
                return HttpResponseRedirect(reverse('localisation:localisation'))

            except District.DoesNotExist:
                try:
                    district = District.objects.get(libelle = libelle)
                    messages.error(request, f"Ce libellé :[{libelle}] existe déjà.")
                    return HttpResponseRedirect(reverse('localisation:localisation'))
                except District.DoesNotExist:
                    pass
            #----
            district = District()
            district.code = code
            district.libelle = libelle
            district.save()

            messages.success(request,"Enregistrement réussi.")

            return HttpResponseRedirect(reverse('localisation:localisation'))
    else:
        return HttpResponseRedirect(reverse('localisation:localisation'))

@login_required
@permission_required('localisation.change_district', raise_exception=True)
def modifier_district(request):

    global _active_onglet
    _active_onglet = "district"  # On initialise la variable

    if request.method == "POST":

        try:
            district = District.objects.get(id=request.POST.get('id'))
        except District.DoesNotExist:
            messages.error(request, "Ce district n'existe pas.")
            return HttpResponseRedirect(reverse('localisation:localisation'))


        if district:
            # On format les chaine
            code = request.POST.get("code")
            libelle = request.POST.get("libelle")
            libelle = libelle.capitalize()

            district.code = code
            district.libelle = libelle
            district.save()

            messages.success(request, "Modification réussie.")

            return HttpResponseRedirect(reverse('localisation:localisation'))
    else:
        return HttpResponseRedirect(reverse('localisation:localisation'))

@login_required
@permission_required('localisation.delete_district', raise_exception=True)
def supprimer_district(request, id):

    global _active_onglet
    _active_onglet = "district"  # On initialise la variable

    try:
        district = District.objects.get(id=id)
    except District.DoesNotExist:
        messages.error(request, "Ce district n'existe pas.")
        return HttpResponseRedirect(reverse('localisation:localisation'))

    if district:
        district.delete()
        messages.info(request, "Suppression réussie.")

    return HttpResponseRedirect(reverse('localisation:localisation'))

# Fin de la Gestion du district -------------------------------------

# Gestion de la région -----------------------------------------------

@login_required
@permission_required('localisation.add_region', raise_exception=True)
def ajouter_region(request):

    global _active_onglet
    _active_onglet = "region"  # On initialise la variable

    if request.method == "POST":
        # On initialise les variables
        code = request.POST.get("code", None)
        libelle = request.POST.get("libelle", None)
        district = request.POST.get("select_district", None)

        if code and libelle and district:
            # On vérifie si le code et le libelle existe
            # On format les chaine
            libelle = libelle.capitalize()

            try:
                region = Region.objects.get(code = code)
                messages.error(request, f"Ce code :[{code}] existe déjà.")
                return HttpResponseRedirect(reverse('localisation:localisation'))

            except Region.DoesNotExist:
                try:
                    region = Region.objects.get(libelle = libelle)
                    messages.error(request, f"Ce libellé :[{libelle}] existe déjà.")
                    return HttpResponseRedirect(reverse('localisation:localisation'))
                except Region.DoesNotExist:
                    pass
            #----
            region = Region()
            region.code = code
            region.libelle = libelle
            region.district = District.objects.get(id = district)
            region.save()

            messages.success(request,"Enregistrement réussi.")

            return HttpResponseRedirect(reverse('localisation:localisation'))
        else:
            messages.error(request, "Veuillez renseigner les champs.")
            return HttpResponseRedirect(reverse('localisation:localisation'))
    else:
        return HttpResponseRedirect(reverse('localisation:localisation'))

@login_required
@permission_required('localisation.change_region', raise_exception=True)
def modifier_region(request):

    global _active_onglet
    _active_onglet = "region"  # On initialise la variable

    if request.method == "POST":

        try:
            region = Region.objects.get(id=request.POST.get('id'))
        except Region.DoesNotExist:
            messages.error(request, "Cette région n'existe pas.")
            return HttpResponseRedirect(reverse('localisation:localisation'))


        if region:
            # On format les chaine
            code = request.POST.get("code")
            libelle = request.POST.get("libelle")
            district = request.POST.get("select_district")
            libelle = libelle.capitalize()

            region.code = code
            region.libelle = libelle
            region.district = District.objects.get(id = district)
            region.save()

            messages.success(request, "Modification réussie.")

            return HttpResponseRedirect(reverse('localisation:localisation'))
    else:
        return HttpResponseRedirect(reverse('localisation:localisation'))

@login_required
@permission_required('localisation.delete_region', raise_exception=True)
def supprimer_region(request, id):

    global _active_onglet
    _active_onglet = "region"  # On initialise la variable

    try:
        region = Region.objects.get(id=id)
    except District.DoesNotExist:
        messages.error(request, "Cette région n'existe pas.")
        return HttpResponseRedirect(reverse('localisation:localisation'))

    if region:
        region.delete()
        messages.info(request, "Suppression réussie.")

    return HttpResponseRedirect(reverse('localisation:localisation'))

@login_required
@permission_required('localisation.view_region', raise_exception=True)
def details_region(request):

    if request.method == "GET":
        id = request.GET.get('id', None)
        if id:
            ajax_regions = Region.objects.filter(district=id).order_by('libelle')

            if ajax_regions:
                data = [{'id': region.id, 'libelle': region.libelle} for region in ajax_regions]

                return JsonResponse({'data': data}, status=200)

    return HttpResponseRedirect(reverse('localisation:localisation'))

# Fin de la Gestion de la région -------------------------------------


# Gestion du département -----------------------------------------------

@login_required
@permission_required('localisation.add_departement', raise_exception=True)
def ajouter_departement(request):

    global _active_onglet
    _active_onglet = "departement"  # On initialise la variable

    if request.method == "POST":
        # On initialise les variables
        code = request.POST.get("code", None)
        libelle = request.POST.get("libelle", None)
        region = request.POST.get("select_region", None)

        if code and libelle and region:
            # On vérifie si le code et le libelle existe
            # On format les chaine
            libelle = libelle.capitalize()

            try:
                departement = Departement.objects.get(code = code)
                messages.error(request, f"Ce code :[{code}] existe déjà.")
                return HttpResponseRedirect(reverse('localisation:localisation'))

            except Departement.DoesNotExist:
                try:
                    departement = Departement.objects.get(libelle = libelle)
                    messages.error(request, f"Ce libellé :[{libelle}] existe déjà.")
                    return HttpResponseRedirect(reverse('localisation:localisation'))
                except Departement.DoesNotExist:
                    pass
            #----
            departement = Departement()
            departement.code = code
            departement.libelle = libelle
            departement.region = Region.objects.get(id = region)
            departement.save()

            messages.success(request,"Enregistrement réussi.")

            return HttpResponseRedirect(reverse('localisation:localisation'))
        else:
            messages.error(request, "Veuillez renseigner les champs.")
            return HttpResponseRedirect(reverse('localisation:localisation'))
    else:
        return HttpResponseRedirect(reverse('localisation:localisation'))

@login_required
@permission_required('localisation.change_departement', raise_exception=True)
def modifier_departement(request):

    global _active_onglet
    _active_onglet = "departement"  # On initialise la variable

    if request.method == "POST":
        # On initialise les variables
        code = request.POST.get("code", None)
        libelle = request.POST.get("libelle", None)
        region = request.POST.get("select_region", None)

        if code and libelle and region:
            try:
                departement = Departement.objects.get(id=request.POST.get('id'))
            except Departement.DoesNotExist:
                messages.error(request, "Ce département n'existe pas.")
                return HttpResponseRedirect(reverse('localisation:localisation'))

            if departement:
                # On format les chaine
                code = request.POST.get("code")
                libelle = request.POST.get("libelle")
                region = request.POST.get("select_region")
                libelle = libelle.capitalize()

                departement.code = code
                departement.libelle = libelle
                departement.region = Region.objects.get(id=region)
                departement.save()

                messages.success(request, "Modification réussie.")

                return HttpResponseRedirect(reverse('localisation:localisation'))
        else:
            messages.error(request, "Veuillez renseigner les champs.")
            return HttpResponseRedirect(reverse('localisation:localisation'))

    else:
        return HttpResponseRedirect(reverse('localisation:localisation'))

@login_required
@permission_required('localisation.delete_departement', raise_exception=True)
def supprimer_departement(request, id):

    global _active_onglet
    _active_onglet = "departement"  # On initialise la variable

    try:
        departement = Departement.objects.get(id=id)
    except Departement.DoesNotExist:
        messages.error(request, "Ce département n'existe pas.")
        return HttpResponseRedirect(reverse('localisation:localisation'))

    if departement:
        departement.delete()
        messages.info(request, "Suppression réussie.")

    return HttpResponseRedirect(reverse('localisation:localisation'))

# Fin de la Gestion du département -------------------------------------

# Gestion de la ville -----------------------------------------------

@login_required
@permission_required('localisation.add_ville', raise_exception=True)
def ajouter_ville(request):

    global _active_onglet
    _active_onglet = "ville"  # On initialise la variable

    if request.method == "POST":
        # On initialise les variables
        code = request.POST.get("code", None)
        libelle = request.POST.get("libelle", None)
        departement = request.POST.get("select_departement", None)

        if code and libelle and departement:
            # On vérifie si le code et le libelle existe
            # On format les chaine
            libelle = libelle.capitalize()

            try:
                ville = Ville.objects.get(code = code)
                messages.error(request, f"Ce code :[{code}] existe déjà.")
                return HttpResponseRedirect(reverse('localisation:localisation'))

            except Ville.DoesNotExist:
                try:
                    ville = Ville.objects.get(libelle = libelle)
                    messages.error(request, f"Ce libellé :[{libelle}] existe déjà.")
                    return HttpResponseRedirect(reverse('localisation:localisation'))
                except Ville.DoesNotExist:
                    pass
            #----
            ville = Ville()
            ville.code = code
            ville.libelle = libelle
            ville.departement = Departement.objects.get(id = departement)
            ville.save()

            messages.success(request,"Enregistrement réussi.")

            return HttpResponseRedirect(reverse('localisation:localisation'))
        else:
            messages.error(request, "Veuillez renseigner les champs.")
            return HttpResponseRedirect(reverse('localisation:localisation'))
    else:
        return HttpResponseRedirect(reverse('localisation:localisation'))

@login_required
@permission_required('localisation.change_ville', raise_exception=True)
def modifier_ville(request):

    global _active_onglet
    _active_onglet = "ville"  # On initialise la variable

    if request.method == "POST":
        # On initialise les variables
        code = request.POST.get("code", None)
        libelle = request.POST.get("libelle", None)
        departement = request.POST.get("select_departement", None)

        if code and libelle and departement:
            try:
                ville = Ville.objects.get(id=request.POST.get('id'))
            except Ville.DoesNotExist:
                messages.error(request, "Cette ville n'existe pas.")
                return HttpResponseRedirect(reverse('localisation:localisation'))

            if ville:
                # On format les chaine
                code = request.POST.get("code")
                libelle = request.POST.get("libelle")
                departement = request.POST.get("select_departement")
                libelle = libelle.capitalize()

                ville.code = code
                ville.libelle = libelle
                ville.departement = Departement.objects.get(id=departement)
                ville.save()

                messages.success(request, "Modification réussie.")

                return HttpResponseRedirect(reverse('localisation:localisation'))
        else:
            messages.error(request, "Veuillez renseigner les champs.")
            return HttpResponseRedirect(reverse('localisation:localisation'))

    else:
        return HttpResponseRedirect(reverse('localisation:localisation'))

@login_required
@permission_required('localisation.delete_ville', raise_exception=True)
def supprimer_ville(request, id):

    global _active_onglet
    _active_onglet = "ville"  # On initialise la variable

    try:
        ville = Ville.objects.get(id=id)
    except Ville.DoesNotExist:
        messages.error(request, "Cette ville n'existe pas.")
        return HttpResponseRedirect(reverse('localisation:localisation'))

    if ville:
        ville.delete()
        messages.info(request, "Suppression réussie.")

    return HttpResponseRedirect(reverse('localisation:localisation'))

@login_required
@permission_required('localisation.view_ville', raise_exception=True)
def details_departement(request):

    if request.method == "GET":
        id = request.GET.get('id', None)
        if id:
            ajax_departement = Departement.objects.filter(region=id).order_by('libelle')

            if ajax_departement:
                data = [{'id': departement.id, 'libelle': departement.libelle} for departement in ajax_departement]

                return JsonResponse({'data': data}, status=200)

    return HttpResponseRedirect(reverse('localisation:localisation'))

# Fin de la Gestion de la ville -------------------------------------

# Gestion de la commune -----------------------------------------------

@login_required
@permission_required('localisation.add_commune', raise_exception=True)
def ajouter_commune(request):

    global _active_onglet
    _active_onglet = "commune"  # On initialise la variable

    if request.method == "POST":
        # On initialise les variables
        code = request.POST.get("code", None)
        libelle = request.POST.get("libelle", None)
        ville = request.POST.get("select_ville", None)

        if code and libelle and ville:
            # On vérifie si le code et le libelle existe
            # On format les chaine
            libelle = libelle.capitalize()

            try:
                commune = Commune.objects.get(code = code)
                messages.error(request, f"Ce code :[{code}] existe déjà.")
                return HttpResponseRedirect(reverse('localisation:localisation'))

            except Commune.DoesNotExist:
                try:
                    commune = Commune.objects.get(libelle = libelle)
                    messages.error(request, f"Ce libellé :[{libelle}] existe déjà.")
                    return HttpResponseRedirect(reverse('localisation:localisation'))
                except Commune.DoesNotExist:
                    pass
            #----
            commune = Commune()
            commune.code = code
            commune.libelle = libelle
            commune.ville = Ville.objects.get(id = ville)
            commune.save()

            messages.success(request,"Enregistrement réussi.")

            return HttpResponseRedirect(reverse('localisation:localisation'))
        else:
            messages.error(request, "Veuillez renseigner les champs.")
            return HttpResponseRedirect(reverse('localisation:localisation'))
    else:
        return HttpResponseRedirect(reverse('localisation:localisation'))

@login_required
@permission_required('localisation.change_commune', raise_exception=True)
def modifier_commune(request):

    global _active_onglet
    _active_onglet = "commune"  # On initialise la variable

    if request.method == "POST":
        # On initialise les variables
        code = request.POST.get("code", None)
        libelle = request.POST.get("libelle", None)
        ville = request.POST.get("select_ville", None)

        if code and libelle and ville:
            try:
                commune = Commune.objects.get(id=request.POST.get('id'))
            except Commune.DoesNotExist:
                messages.error(request, "Cette commune n'existe pas.")
                return HttpResponseRedirect(reverse('localisation:localisation'))

            if commune:
                # On format les chaine
                code = request.POST.get("code")
                libelle = request.POST.get("libelle")
                ville = request.POST.get("select_ville")
                libelle = libelle.capitalize()

                commune.code = code
                commune.libelle = libelle
                commune.ville = Ville.objects.get(id=ville)
                commune.save()

                messages.success(request, "Modification réussie.")

                return HttpResponseRedirect(reverse('localisation:localisation'))
        else:
            messages.error(request, "Veuillez renseigner les champs.")
            return HttpResponseRedirect(reverse('localisation:localisation'))

    else:
        return HttpResponseRedirect(reverse('localisation:localisation'))

@login_required
@permission_required('localisation.delete_commune', raise_exception=True)
def supprimer_commune(request, id):

    global _active_onglet
    _active_onglet = "commune"  # On initialise la variable

    try:
        commune = Commune.objects.get(id=id)
    except Commune.DoesNotExist:
        messages.error(request, "Cette commune n'existe pas.")
        return HttpResponseRedirect(reverse('localisation:localisation'))

    if commune:
        commune.delete()
        messages.info(request, "Suppression réussie.")

    return HttpResponseRedirect(reverse('localisation:localisation'))

@login_required
@permission_required('localisation.view_commune', raise_exception=True)
def details_ville(request):

    if request.method == "GET":
        id = request.GET.get('id', None)
        if id:
            ajax_ville = Ville.objects.filter(departement=id).order_by('libelle')

            if ajax_ville:
                data = [{'id': ville.id, 'libelle': ville.libelle} for ville in ajax_ville]

                return JsonResponse({'data': data}, status=200)

    return HttpResponseRedirect(reverse('localisation:localisation'))

# Fin de la Gestion de la commune -------------------------------------

# Gestion du quartier -----------------------------------------------

@login_required
@permission_required('localisation.add_quartier', raise_exception=True)
def ajouter_quartier(request):

    global _active_onglet
    _active_onglet = "quartier"  # On initialise la variable

    if request.method == "POST":
        # On initialise les variables
        code = request.POST.get("code", None)
        libelle = request.POST.get("libelle", None)
        commune = request.POST.get("select_commune", None)

        if code and libelle and commune:
            # On vérifie si le code et le libelle existe
            # On format les chaine
            libelle = libelle.capitalize()

            try:
                quartier = Quartier.objects.get(code = code)
                messages.error(request, f"Ce code :[{code}] existe déjà.")
                return HttpResponseRedirect(reverse('localisation:localisation'))

            except Quartier.DoesNotExist:
                try:
                    quartier = Quartier.objects.get(libelle = libelle)
                    messages.error(request, f"Ce libellé :[{libelle}] existe déjà.")
                    return HttpResponseRedirect(reverse('localisation:localisation'))
                except Quartier.DoesNotExist:
                    pass
            #----
            quartier = Quartier()
            quartier.code = code
            quartier.libelle = libelle
            quartier.commune = Commune.objects.get(id = commune)
            quartier.save()

            messages.success(request,"Enregistrement réussi.")

            return HttpResponseRedirect(reverse('localisation:localisation'))
        else:
            messages.error(request, "Veuillez renseigner les champs.")
            return HttpResponseRedirect(reverse('localisation:localisation'))
    else:
        return HttpResponseRedirect(reverse('localisation:localisation'))

@login_required
@permission_required('localisation.change_quartier', raise_exception=True)
def modifier_quartier(request):

    global _active_onglet
    _active_onglet = "quartier"  # On initialise la variable

    if request.method == "POST":
        # On initialise les variables
        code = request.POST.get("code", None)
        libelle = request.POST.get("libelle", None)
        commune = request.POST.get("select_commune", None)

        if code and libelle and commune:
            try:
                quartier = Quartier.objects.get(id=request.POST.get('id'))
            except Quartier.DoesNotExist:
                messages.error(request, "Ce quartier n'existe pas.")
                return HttpResponseRedirect(reverse('localisation:localisation'))

            if quartier:
                # On format les chaine
                code = request.POST.get("code")
                libelle = request.POST.get("libelle")
                commune = request.POST.get("select_commune")
                libelle = libelle.capitalize()

                quartier.code = code
                quartier.libelle = libelle
                quartier.commune = Commune.objects.get(id=commune)
                quartier.save()

                messages.success(request, "Modification réussie.")

                return HttpResponseRedirect(reverse('localisation:localisation'))
        else:
            messages.error(request, "Veuillez renseigner les champs.")
            return HttpResponseRedirect(reverse('localisation:localisation'))

    else:
        return HttpResponseRedirect(reverse('localisation:localisation'))

@login_required
@permission_required('localisation.delete_quartier', raise_exception=True)
def supprimer_quartier(request, id):

    global _active_onglet
    _active_onglet = "quartier"  # On initialise la variable

    try:
        quartier = Quartier.objects.get(id=id)
    except Quartier.DoesNotExist:
        messages.error(request, "Ce quartier n'existe pas.")
        return HttpResponseRedirect(reverse('localisation:localisation'))

    if quartier:
        quartier.delete()
        messages.info(request, "Suppression réussie.")

    return HttpResponseRedirect(reverse('localisation:localisation'))

@login_required
@permission_required('localisation.view_quartier', raise_exception=True)
def details_commune(request):

    if request.method == "GET":
        id = request.GET.get('id', None)
        if id:
            ajax_commune = Commune.objects.filter(ville=id).order_by('libelle')

            if ajax_commune:
                data = [{'id': commune.id, 'libelle': commune.libelle} for commune in ajax_commune]

                return JsonResponse({'data': data}, status=200)

    return HttpResponseRedirect(reverse('localisation:localisation'))

# Fin de la Gestion du quartier -------------------------------------

# Gestion du marché -----------------------------------------------

@login_required
@permission_required('localisation.add_marche', raise_exception=True)
def ajouter_marche(request):

    global _active_onglet
    _active_onglet = "marche"  # On initialise la variable

    if request.method == "POST":
        # On initialise les variables
        code = request.POST.get("code", None)
        libelle = request.POST.get("libelle", None)
        quartier = request.POST.get("select_quartier", None)

        if code and libelle and quartier:
            # On vérifie si le code et le libelle existe
            # On format les chaine
            libelle = libelle.capitalize()

            try:
                marche = Marche.objects.get(code = code)
                messages.error(request, f"Ce code :[{code}] existe déjà.")
                return HttpResponseRedirect(reverse('localisation:localisation'))

            except Marche.DoesNotExist:
                try:
                    marche = Marche.objects.get(libelle = libelle)
                    messages.error(request, f"Ce libellé :[{libelle}] existe déjà.")
                    return HttpResponseRedirect(reverse('localisation:localisation'))
                except Marche.DoesNotExist:
                    pass
            #----
            marche = Marche()
            marche.code = code
            marche.libelle = libelle
            marche.quartier = Quartier.objects.get(id = quartier)
            marche.save()

            messages.success(request,"Enregistrement réussi.")

            return HttpResponseRedirect(reverse('localisation:localisation'))
        else:
            messages.error(request, "Veuillez renseigner les champs.")
            return HttpResponseRedirect(reverse('localisation:localisation'))
    else:
        return HttpResponseRedirect(reverse('localisation:localisation'))

@login_required
@permission_required('localisation.change_marche', raise_exception=True)
def modifier_marche(request):

    global _active_onglet
    _active_onglet = "marche"  # On initialise la variable

    if request.method == "POST":
        # On initialise les variables
        code = request.POST.get("code", None)
        libelle = request.POST.get("libelle", None)
        quartier = request.POST.get("select_quartier", None)

        if code and libelle and quartier:
            try:
                marche = Marche.objects.get(id=request.POST.get('id'))
            except Marche.DoesNotExist:
                messages.error(request, "Ce marché n'existe pas.")
                return HttpResponseRedirect(reverse('localisation:localisation'))

            if marche:
                # On format les chaine
                code = request.POST.get("code")
                libelle = request.POST.get("libelle")
                quartier = request.POST.get("select_quartier")
                libelle = libelle.capitalize()

                marche.code = code
                marche.libelle = libelle
                marche.quartier = Quartier.objects.get(id=quartier)
                marche.save()

                messages.success(request, "Modification réussie.")

                return HttpResponseRedirect(reverse('localisation:localisation'))
        else:
            messages.error(request, "Veuillez renseigner les champs.")
            return HttpResponseRedirect(reverse('localisation:localisation'))

    else:
        return HttpResponseRedirect(reverse('localisation:localisation'))

@login_required
@permission_required('localisation.delete_marche', raise_exception=True)
def supprimer_marche(request, id):

    global _active_onglet
    _active_onglet = "marche"  # On initialise la variable

    try:
        marche = Marche.objects.get(id=id)
    except Marche.DoesNotExist:
        messages.error(request, "Ce marché n'existe pas.")
        return HttpResponseRedirect(reverse('localisation:localisation'))

    if marche:
        marche.delete()
        messages.info(request, "Suppression réussie.")

    return HttpResponseRedirect(reverse('localisation:localisation'))

@login_required
@permission_required('localisation.view_marche', raise_exception=True)
def details_quartier(request):

    if request.method == "GET":
        id = request.GET.get('id', None)
        if id:
            ajax_quartier = Quartier.objects.filter(commune=id).order_by('libelle')

            if ajax_quartier:
                data = [{'id': quartier.id, 'libelle': quartier.libelle} for quartier in ajax_quartier]

                return JsonResponse({'data': data}, status=200)

    return HttpResponseRedirect(reverse('localisation:localisation'))

@login_required
@permission_required('localisation.view_marche', raise_exception=True)
def details_marche(request):

    if request.method == "GET":
        id = request.GET.get('id', None)
        if id:
            ajax_marche = Marche.objects.filter(quartier=id).order_by('libelle')

            if ajax_marche:
                data = [{'id': marche.id, 'libelle': marche.libelle} for marche in ajax_marche]

                return JsonResponse({'data': data}, status=200)

    return HttpResponseRedirect(reverse('localisation:localisation'))

# Fin de la Gestion du marché -------------------------------------