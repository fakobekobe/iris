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
]