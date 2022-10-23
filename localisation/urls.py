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

    # Url de la Commune
    path('ajouter-commune', views.ajouter_commune, name = 'ajouter_commune'),
    path('modifier-commune', views.modifier_commune, name = 'modifier_commune'),
    path('supprimer-commune/<str:id>', views.supprimer_commune, name = 'supprimer_commune'),
    path('details-ville', views.details_ville, name = 'details_ville'),

    # Url du Quartier
    path('ajouter-quartier', views.ajouter_quartier, name = 'ajouter_quartier'),
    path('modifier-quartier', views.modifier_quartier, name = 'modifier_quartier'),
    path('supprimer-quartier/<str:id>', views.supprimer_quartier, name = 'supprimer_quartier'),
    path('details-commune', views.details_commune, name = 'details_commune'),
]