from django.urls import path
from . import views

app_name = 'presentation'
urlpatterns = [

    # Url du Secteur Agricole
    path('index/', views.index, name = 'index'),
    path('ajouter-secteuragricole/', views.ajouter_secteuragricole, name='ajouter_secteuragricole'),
    path('modifier-secteuragricole/<str:id>', views.modifier_secteuragricole, name='modifier_secteuragricole'),
    path('supprimer-secteuragricole/<str:id>', views.supprimer_secteuragricole, name='supprimer_secteuragricole'),
    path('details-secteuragricole/<str:id>', views.detail_secteuragricole, name='detail_secteuragricole'),
    path('details-niveauscolaire/', views.details_niveauscolaire, name='details_niveauscolaire'),
    path('ajouter-secteur-membre', views.ajouter_secteur_membre, name='ajouter_secteur_membre'),
    path('supprimer-secteur-membre', views.supprimer_secteur_membre, name='supprimer_secteur_membre'),
    path('ajouter-document-membre', views.ajouter_document_membre, name='ajouter_document_membre'),

    # Url du Type Secteur
    #path('supprimer-membre/<str:id>', views.supprimer_membre, name='supprimer_membre'),

]