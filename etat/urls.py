from django.urls import path
from . import views

app_name = 'etat'
urlpatterns = [
    path('', views.etat, name='etat'),

    # Url des bouttons
    path('fiche-identification', views.fiche_identification, name='fiche_identification'),
    #path('modifier-typepiece', views.modifier_typepiece, name = 'modifier_typepiece'),
    #path('supprimer-typepiece/<str:id>', views.supprimer_typepiece, name = 'supprimer_typepiece'),

]