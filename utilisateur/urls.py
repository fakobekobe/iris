from django.urls import path
from . import views

app_name = 'utilisateur'
urlpatterns = [
    path('', views.connexion, name = 'connexion'),
    path('inscription/<int:ajouter_utilisateur>', views.inscription, name = 'inscription'),
    path('deconnexion/', views.deconnexion, name = 'deconnexion'),

    path('utilisateur/', views.utilisateur, name = 'utilisateur'),
    path('infos-utilisateur/<int:id>', views.detail_utilisateur, name = 'detail_utilisateur'),
    path('modifier-utilisateur/<int:id>', views.modifier_utilisateur, name = 'modifier_utilisateur'),
    path('supprimer-utilisateur/<int:id>', views.supprimer_utilisateur, name = 'supprimer_utilisateur'),
    path('supprimer-groupe-utilisateur/<int:id>', views.supprimer_groupe_utilisateur, name = 'supprimer_groupe_utilisateur'),


    path('groupe/', views.groupe, name = 'groupe'),
    path('ajouter-groupe/', views.ajouter_groupe, name = 'ajouter_groupe'),
    path('infos-groupe/<int:id>', views.detail_groupe, name = 'detail_groupe'),
    path('modifier-groupe/<int:id>', views.modifier_groupe, name = 'modifier_groupe'),
    path('supprimer-groupe/<int:id>', views.supprimer_groupe, name = 'supprimer_groupe'),
    path('supprimer-utilisateur-groupe/<int:id>', views.supprimer_utilisateur_groupe, name = 'supprimer_utilisateur_groupe'),

    path('index/', views.index, name = 'index'),
    path('motdepasse/<str:id>', views.motdepasse, name = 'motdepasse'),
]