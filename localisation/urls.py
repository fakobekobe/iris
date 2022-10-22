from django.urls import path
from . import views

app_name = 'localisation'
urlpatterns = [
    path('', views.localisation, name = 'localisation'),

    # Url du district
    path('ajouter-district', views.ajouter_district, name = 'ajouter_district'),
    path('modifier-district', views.modifier_district, name = 'modifier_district'),
    path('supprimer-district/<str:id>', views.supprimer_district, name = 'supprimer_district'),

    # Url de la région
    path('ajouter-region', views.ajouter_region, name = 'ajouter_region'),
    path('modifier-region', views.modifier_region, name = 'modifier_region'),
    path('supprimer-region/<str:id>', views.supprimer_region, name = 'supprimer_region'),
    path('details-region', views.details_region, name = 'details_region'),

    # Url de la département
    path('ajouter-departement', views.ajouter_departement, name = 'ajouter_departement'),
    path('modifier-departement', views.modifier_departement, name = 'modifier_departement'),
    path('supprimer-departement/<str:id>', views.supprimer_departement, name = 'supprimer_departement'),

    # Url de la ville
    path('ajouter-ville', views.ajouter_ville, name = 'ajouter_ville'),
    path('modifier-ville', views.modifier_ville, name = 'modifier_ville'),
    path('supprimer-ville/<str:id>', views.supprimer_ville, name = 'supprimer_ville'),
    path('details-departement', views.details_departement, name = 'details_departement'),
]