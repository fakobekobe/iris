from django.urls import path
from . import views

app_name = 'vieprofessionnelle'
urlpatterns = [
    path('', views.vieprofessionnelle, name = 'vieprofessionnelle'),

    # Url du Métier
    path('ajouter-typesecteur', views.ajouter_typesecteur, name = 'ajouter_typesecteur'),
    path('modifier-typesecteur', views.modifier_typesecteur, name = 'modifier_typesecteur'),
    path('supprimer-typesecteur/<str:id>', views.supprimer_typesecteur, name = 'supprimer_typesecteur'),


]