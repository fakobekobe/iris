from django.urls import path
from . import views

app_name = 'presentation'
urlpatterns = [

    # Url du Secteur Agricole
    path('index/', views.index, name='index'),
    path('ajouter-secteuragricole/', views.ajouter_secteuragricole, name='ajouter_secteuragricole'),
    path('modifier-secteuragricole/<str:id>', views.modifier_secteuragricole, name='modifier_secteuragricole'),
    path('supprimer-secteuragricole/<str:id>', views.supprimer_secteuragricole, name='supprimer_secteuragricole'),
    path('details-secteuragricole/<str:id>', views.detail_secteuragricole, name='detail_secteuragricole'),
    path('details-niveauscolaire/', views.details_niveauscolaire, name='details_niveauscolaire'),
    path('ajouter-secteur-membre', views.ajouter_secteur_membre, name='ajouter_secteur_membre'),
    path('supprimer-secteur-membre', views.supprimer_secteur_membre, name='supprimer_secteur_membre'),
    path('ajouter-document-membre', views.ajouter_document_membre, name='ajouter_document_membre'),
    path('supprimer-document-membre', views.supprimer_document_membre, name='supprimer_document_membre'),
    path('supprimer-parent-membre', views.supprimer_parent_membre, name='supprimer_parent_membre'),
    path('ajouter-parent-membre', views.ajouter_parent_membre, name='ajouter_parent_membre'),
    path('retour-liste-membre', views.retour_liste_membre, name='retour_liste_membre'),
    path('ajouter-etatsante-membre', views.ajouter_etatsante_membre, name='ajouter_etatsante_membre'),
    path('supprimer-etatsante-membre', views.supprimer_etatsante_membre, name='supprimer_etatsante_membre'),
    path('detail-parent-secteuragricole/<str:id>', views.detail_parent_secteuragricole, name='detail_parent_secteuragricole'),
    path('ajouter-etatsante-parent', views.ajouter_etatsante_parent, name='ajouter_etatsante_parent'),
    path('supprimer-etatsante-parent', views.supprimer_etatsante_parent, name='supprimer_etatsante_parent'),
    path('imprimer-secteuragricole/<str:id>', views.imprimer_secteuragricole, name='imprimer_secteuragricole'),

    # Url du Secteur Femme Active
    path('ajouter-secteurfemmeactive/', views.ajouter_secteurfemmeactive, name='ajouter_secteurfemmeactive'),
    path('modifier-secteurfemmeactive/<str:id>', views.modifier_secteurfemmeactive, name='modifier_secteurfemmeactive'),
    path('supprimer-secteurfemmeactive/<str:id>', views.supprimer_secteurfemmeactive, name='supprimer_secteurfemmeactive'),
    path('details-secteurfemmeactive/<str:id>', views.detail_secteurfemmeactive, name='detail_secteurfemmeactive'),
    path('imprimer-secteurfemmeactive/<str:id>', views.imprimer_secteurfemmeactive, name='imprimer_secteurfemmeactive'),

]