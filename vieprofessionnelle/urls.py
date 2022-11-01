from django.urls import path
from . import views

app_name = 'vieprofessionnelle'
urlpatterns = [
    path('', views.vieprofessionnelle, name = 'vieprofessionnelle'),

    # Url du Type Secteur d'activité
    path('ajouter-typesecteur', views.ajouter_typesecteur, name = 'ajouter_typesecteur'),
    path('modifier-typesecteur', views.modifier_typesecteur, name = 'modifier_typesecteur'),
    path('supprimer-typesecteur/<str:id>', views.supprimer_typesecteur, name = 'supprimer_typesecteur'),

    # Url du Secteur
    path('ajouter-secteur', views.ajouter_secteur, name='ajouter_secteur'),
    path('modifier-secteur', views.modifier_secteur, name='modifier_secteur'),
    path('supprimer-secteur/<str:id>', views.supprimer_secteur, name='supprimer_secteur'),


]