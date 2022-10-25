from django.db import models

class TypePiece(models.Model):
    type = models.CharField(max_length=100, unique=True)
    libelle = models.CharField(max_length=250, verbose_name="Libellé", unique=True)

    def __str__(self):
        return self.libelle

class Niveau(models.Model):
    niveau = models.CharField(max_length=250, verbose_name="Niveau", unique=True)

    def __str__(self):
        return self.niveau

class NiveauScolaire(models.Model):
    classe = models.CharField(max_length=250, verbose_name="Classe", unique=True)
    niveau = models.ForeignKey(Niveau, on_delete=models.CASCADE)

    def __str__(self):
        return self.classe
