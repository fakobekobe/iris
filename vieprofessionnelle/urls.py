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

    # Url Type de Parent
    path('ajouter-typeparent', views.ajouter_typeparent, name='ajouter_typeparent'),
    path('modifier-typeparent', views.modifier_typeparent, name='modifier_typeparent'),
    path('supprimer-typeparent/<str:id>', views.supprimer_typeparent, name='supprimer_typeparent'),

    # Url Parent
    path('ajouter-parent', views.ajouter_parent, name='ajouter_parent'),
    path('modifier-parent', views.modifier_parent, name='modifier_parent'),
    path('supprimer-parent/<str:id>', views.supprimer_parent, name='supprimer_parent'),

    # Url Type d'état de santé
    path('ajouter-typeetatsante', views.ajouter_typeetatsante, name='ajouter_typeetatsante'),
    path('modifier-typeetatsante', views.modifier_typeetatsante, name='modifier_typeetatsante'),
    path('supprimer-typeetatsante/<str:id>', views.supprimer_typeetatsante, name='supprimer_typeetatsante'),

    # Url Type d'état de document
    path('ajouter-typedocument', views.ajouter_typedocument, name='ajouter_typedocument'),
    path('modifier-typedocument', views.modifier_typedocument, name='modifier_typedocument'),
    path('supprimer-typedocument/<str:id>', views.supprimer_typedocument, name='supprimer_typedocument'),


]