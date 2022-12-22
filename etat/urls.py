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
    path('total-deces', views.total_deces, name='total_deces'),
    path('total-deces-enfant', views.total_deces_enfant, name='total_deces_enfant'),
    path('total-accident', views.total_accident, name='total_accident'),
    path('total-accident-enfant', views.total_accident_enfant, name='total_accident_enfant'),

]