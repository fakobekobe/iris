from django.db import models

class District(models.Model):
    code = models.CharField(max_length=100, unique=True)
    libelle = models.CharField(max_length=250, verbose_name="Libellé", unique=True)

    def __str__(self):
        return self.libelle

class Region(models.Model):
    code = models.CharField(max_length=100, unique=True)
    libelle = models.CharField(max_length=250, verbose_name="Libellé", unique=True)
    district = models.ForeignKey(District,on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.libelle

class Departement(models.Model):
    code = models.CharField(max_length=100, unique=True)
    libelle = models.CharField(max_length=250, verbose_name="Libellé", unique=True)
    region = models.ForeignKey(Region,on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.libelle