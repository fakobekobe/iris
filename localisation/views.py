from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required, permission_required

@login_required
@permission_required('auth.view_user', raise_exception=True)
@permission_required('auth.view_group', raise_exception=True)
def localisation(request):

    districts = District.objects.all().order_by("-id")
    regions = Region.objects.all().order_by("-id")

    context = {
        "titre" : "Localisation",
        "districts" : districts,
        "regions" : regions,
    }

    return render(request, "localisation/localisation.html", context)

# Gestion du district -----------------------------------------------

@login_required
@permission_required('localisation.view_district', raise_exception=True)
def ajouter_district(request):

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

    if request.method == "POST":
        # On initialise les variables
        code = request.POST.get("code", None)
        libelle = request.POST.get("libelle", None)

        if code and libelle:
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
            region.save()

            messages.success(request,"Enregistrement réussi.")

            return HttpResponseRedirect(reverse('localisation:localisation'))
    else:
        return HttpResponseRedirect(reverse('localisation:localisation'))

@login_required
@permission_required('localisation.change_region', raise_exception=True)
def modifier_region(request):

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
            libelle = libelle.capitalize()

            region.code = code
            region.libelle = libelle
            region.save()

            messages.success(request, "Modification réussie.")

            return HttpResponseRedirect(reverse('localisation:localisation'))
    else:
        return HttpResponseRedirect(reverse('localisation:localisation'))

@login_required
@permission_required('localisation.delete_region', raise_exception=True)
def supprimer_region(request, id):
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