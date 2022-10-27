from django.urls import path
from . import views

app_name = 'vieprofessionnelle'
urlpatterns = [
    path('', views.vieprofessionnelle, name = 'vieprofessionnelle'),

    # Url du Métier
    path('ajouter-metier', views.ajouter_metier, name = 'ajouter_metier'),
    path('modifier-metier', views.modifier_metier, name = 'modifier_metier'),
    path('supprimer-metier/<str:id>', views.supprimer_metier, name = 'supprimer_metier'),


]