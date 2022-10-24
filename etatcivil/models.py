from django.db import models

class TypePiece(models.Model):
    type = models.CharField(max_length=100, unique=True)
    libelle = models.CharField(max_length=250, verbose_name="Libellé", unique=True)

    def __str__(self):
        return self.libelle
