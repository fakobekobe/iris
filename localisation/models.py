from django.db import models

class District(models.Model):
    code = models.CharField(max_length=100, unique=True)
    libelle = models.CharField(max_length=150, verbose_name="Libellé", unique=True)

    def __str__(self):
        return self.libelle
