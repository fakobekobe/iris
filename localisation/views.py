from django.shortcuts import render
from .models import *

def district(request):

    districts = District.objects.all().order_by("id")

    context = {
        "titre" : "Localisation",
        "districts" : districts,
    }
    return render(request, "localisation/localisation.html", context)
