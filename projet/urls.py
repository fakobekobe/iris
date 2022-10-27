"""projet URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls import handler404, handler500, handler400, handler403
from django.conf.urls.static import static

# Configuration des erreurs
handler404 = 'utilisateur.views.handler404'
handler500 = 'utilisateur.views.handler500'
handler400 = 'utilisateur.views.handler400'
handler403 = 'utilisateur.views.handler403'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('utilisateur.urls')),
    path('localisation/',include('localisation.urls')),
    path('etatcivil/',include('etatcivil.urls')),
    path('vieprofessionnelle/',include('vieprofessionnelle.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
