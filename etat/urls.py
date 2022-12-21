from django.urls import path
from . import views

app_name = 'etat'
urlpatterns = [
    path('', views.etat, name='etat'),

    # Url des bouttons
    path('fiche-identification', views.fiche_identification, name='fiche_identification'),
    path('retour-etat/<str:id>', views.retour_etat, name='retour_etat'),
    path('liste-badge', views.liste_badge, name='liste_badge'),
    path('total-enfants', views.total_enfants, name='total_enfants'),
    path('nouvelle-naissance', views.nouvelle_naissance, name='nouvelle_naissance'),

]