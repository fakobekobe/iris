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
    niveau = models.ForeignKey(Niveau,null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.classe

class Sexe(models.Model):
    code = models.CharField(max_length=1, unique=True)
    libelle = models.CharField(max_length=50, verbose_name="Libellé", unique=True)

    def __str__(self):
        return self.libelle

class Nationalite(models.Model):
    code = models.CharField(max_length=3, unique=True)
    nationalite = models.CharField(max_length=100, verbose_name="Nationalité", unique=True)
    pays = models.CharField(max_length=250, verbose_name="Pays", unique=True)

    def __str__(self):
        return self.nationalite
