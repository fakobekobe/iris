from django.shortcuts import render


def etat(request):
    context = {
        'titre': 'Etats',
    }
    return render(request, 'etat/etat.html', context)
