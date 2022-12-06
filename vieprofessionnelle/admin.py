from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Document)
admin.site.register(SecteurAgricole)
admin.site.register(Parent)
admin.site.register(Membre)
admin.site.register(MembreSecteurAgricole)
admin.site.register(Chapeau)
admin.site.register(PersonneRessource)
admin.site.register(TypePersonneRessource)