from django.urls import path
from . import views

app_name = 'localisation'
urlpatterns = [
    path('', views.district, name = 'district'),
]