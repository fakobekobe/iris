from django.urls import path
from . import views

app_name = 'etat'
urlpatterns = [
    path('', views.etat, name='etat'),

    # Url du type de pièce
    #path('ajouter-typepiece', views.ajouter_typepiece, name = 'ajouter_typepiece'),
    #path('modifier-typepiece', views.modifier_typepiece, name = 'modifier_typepiece'),
    #path('supprimer-typepiece/<str:id>', views.supprimer_typepiece, name = 'supprimer_typepiece'),

]