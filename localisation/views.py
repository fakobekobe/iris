from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .models import *

def localisation(request):

    districts = District.objects.all().order_by("id")

    context = {
        "titre" : "Localisation",
        "districts" : districts,
    }
    return render(request, "localisation/localisation.html", context)

# Gestion du district -----------------------------------------------

def ajouter_district(request):

    context = {
        "titre": "Localisation",
    }

    if request.method == "POST":
        if request.POST.get("code") and request.POST.get("libelle"):
            # On vérifie si le code et le libelle existe

            #----
            district = District()
            district.code = request.POST.get("code")
            district.libelle = request.POST.get("libelle")
            district.save()

            messages.success(request,"Enregistrement réussi.")

            return HttpResponseRedirect(reverse('localisation:localisation'))
    else:
        return render(request, "localisation/ajouter_district.html", context)

def details_district(request, id):

    context = {
        "titre": "Details du district",
    }
    district = District.objects.get(id = id)
    if district != None:
        return render(request,'localisation/modifier_district.html', context)

    return render(request, "localisation/localisation.html", context)

def modifier_district(request):

    context = {
        "titre": "Localisation",
    }
    if request.method == "POST":

        district = District.objects.get(id = request.POST.get('id'))

        if district != None:
            district.code = request.POST.get("code")
            district.libelle = request.POST.get("libelle")
            district.save()

            messages.success(request, "Modification réussie.")

            return HttpResponseRedirect(reverse('localisation:localisation'))
    else:
        return render(request, "localisation/modifier_district.html", context)

def supprimer_district(request, id):
    district = District.objects.get(id=id)
    district.delete()
    messages.success(request, "Suppression réussie.")

    return HttpResponseRedirect(reverse('localisation:localisation'))

# Fin de la Gestion du district -------------------------------------
