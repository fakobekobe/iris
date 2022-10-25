from django.urls import path
from . import views

app_name = 'etatcivil'
urlpatterns = [
    path('', views.etatcivil, name = 'etatcivil'),

    # Url du type de pièce
    path('ajouter-typepiece', views.ajouter_typepiece, name = 'ajouter_typepiece'),
    path('modifier-typepiece', views.modifier_typepiece, name = 'modifier_typepiece'),
    path('supprimer-typepiece/<str:id>', views.supprimer_typepiece, name = 'supprimer_typepiece'),

    # Url du niveau
    path('ajouter-niveau', views.ajouter_niveau, name = 'ajouter_niveau'),
    path('modifier-niveau', views.modifier_niveau, name = 'modifier_niveau'),
    path('supprimer-niveau/<str:id>', views.supprimer_niveau, name = 'supprimer_niveau'),
]