"""projet URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('utilisateur.urls')),
    path('localisation/',include('localisation.urls')),
    # path('utilisateur/',include('utilisateur.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
