from django.shortcuts import render

def district(request):
    context = {
        "titre" : "Localisation",
    }
    return render(request, "localisation/localisation.html", context)
