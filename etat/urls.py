from django.urls import path
from . import views

app_name = 'etat'
urlpatterns = [
    path('', views.etat, name='etat'),

    # Url des bouttons
    path('fiche-identification', views.fiche_identification, name='fiche_identification'),
    path('retour-etat/<str:id>', views.retour_etat, name='retour_etat'),
    path('liste-badge', views.liste_badge, name='liste_badge'),

]