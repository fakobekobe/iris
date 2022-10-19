from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required, permission_required

# Les constatntes et les variables globales
_active_onglet = "" # Variable globale pour l'activation des onglets

@login_required
@permission_required('auth.view_user', raise_exception=True)
@permission_required('auth.view_group', raise_exception=True)
def localisation(request):

    districts = District.objects.all().order_by("libelle")
    regions = Region.objects.all().order_by("libelle")

    # Initialisation de l'affichage de l'onglet active
    active_district = ['','false','']
    active_region = ['','false','']

    if _active_onglet == "district":
        active_district =  ['active', 'true', 'show active']
    elif _active_onglet == "region":
        active_region = ['active', 'true', 'show active']
    else:
        # Affichage par défaut
        active_district =  ['active', 'true', 'show active']


    context = {
        "titre" : "Localisation",
        "districts" : districts,
        "regions" : regions,
        "active_region": active_region,
        "active_district": active_district,
    }

    return render(request, "localisation/localisation.html", context)

# Gestion du district -----------------------------------------------

@login_required
@permission_required('localisation.view_district', raise_exception=True)
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
@permission_required('localisation.view_region', raise_exception=True)
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

# Fin de la Gestion de la région -------------------------------------