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
    path('details-secteur', views.details_secteur, name='details_secteur'),
    path('details-activite', views.details_activite, name='details_activite'),

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

    # Url Type du document
    path('ajouter-document/', views.ajouter_document, name='ajouter_document'),
    path('modifier-document/', views.modifier_document, name='modifier_document'),
    path('supprimer-document/<str:id>', views.supprimer_document, name='supprimer_document'),

    # Url Coopérative
    path('ajouter-cooperative', views.ajouter_cooperative, name='ajouter_cooperative'),
    # Url Groupement
    path('ajouter-groupement', views.ajouter_groupement, name='ajouter_groupement'),

    # Url Chapeau
    path('ajouter-chapeau/', views.ajouter_chapeau, name='ajouter_chapeau'),
    path('modifier-chapeau/', views.modifier_chapeau, name='modifier_chapeau'),
    path('supprimer-chapeau/<str:id>', views.supprimer_chapeau, name='supprimer_chapeau'),

    # Url TypePersonneRessource
    path('ajouter-typepersonneressource/', views.ajouter_typepersonneressource, name='ajouter_typepersonneressource'),
    path('modifier-typepersonneressource/', views.modifier_typepersonneressource, name='modifier_typepersonneressource'),
    path('supprimer-typepersonneressource/<str:id>', views.supprimer_typepersonneressource, name='supprimer_typepersonneressource'),

    # Url PersonneRessource
    path('ajouter-personneressource', views.ajouter_personneressource, name='ajouter_personneressource'),
    path('supprimer-personneressource', views.supprimer_personneressource, name='supprimer_personneressource'),
    path('details-personneressource', views.details_personneressource, name='details_personneressource'),

    # Url TypeResponsabilité
    path('ajouter-typeresponsabilite/', views.ajouter_typeresponsabilite, name='ajouter_typeresponsabilite'),
    path('modifier-typeresponsabilite/', views.modifier_typeresponsabilite, name='modifier_typeresponsabilite'),
    path('supprimer-typeresponsabilite/<str:id>', views.supprimer_typeresponsabilite, name='supprimer_typeresponsabilite'),

    # Url MontantFinancement
    path('ajouter-montantfinancement/', views.ajouter_montantfinancement, name='ajouter_montantfinancement'),
    path('modifier-montantfinancement/', views.modifier_montantfinancement, name='modifier_montantfinancement'),
    path('supprimer-montantfinancement/<str:id>', views.supprimer_montantfinancement, name='supprimer_montantfinancement'),

    # Url QuantiteGroupement
    path('ajouter-quantitegroupement/', views.ajouter_quantitegroupement, name='ajouter_quantitegroupement'),
    path('modifier-quantitegroupement/', views.modifier_quantitegroupement, name='modifier_quantitegroupement'),
    path('supprimer-quantitegroupement/<str:id>', views.supprimer_quantitegroupement, name='supprimer_quantitegroupement'),


]