from django.urls import path
from . import views

app_name = 'localisation'
urlpatterns = [
    path('', views.localisation, name = 'localisation'),
    # Url du district
    path('ajouter-district', views.modifier_district, name = 'ajouter_district'),
    path('details-district/<str:id>', views.modifier_district, name = 'details_district'),
    path('modifier-district', views.modifier_district, name = 'modifier_district'),
    path('supprimer-district/<str:id>', views.supprimer_district, name = 'supprimer_district'),
]