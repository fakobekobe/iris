from django.urls import path
from . import views

app_name = 'presentation'
urlpatterns = [

    # Url du Type Secteur
    path('index/', views.index, name = 'index'),
    path('ajouter-secteuragricole', views.ajouter_secteuragricole, name='ajouter_secteuragricole'),
    path('modifier-secteuragricole/<str:id>', views.modifier_secteuragricole, name='modifier_secteuragricole'),
    path('supprimer-secteuragricole/<str:id>', views.supprimer_secteuragricole, name='supprimer_secteuragricole'),

]