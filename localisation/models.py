from django.db import models

class District(models.Model):
    code = models.CharField(max_length=100, unique=True)
    libelle = models.CharField(max_length=250, verbose_name="District", unique=True)

    def __str__(self):
        return self.libelle

class Region(models.Model):
    code = models.CharField(max_length=100, unique=True)
    libelle = models.CharField(max_length=250, verbose_name="Region", unique=True)
    district = models.ForeignKey(District,on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.libelle

class Departement(models.Model):
    code = models.CharField(max_length=100, unique=True)
    libelle = models.CharField(max_length=250, verbose_name="Departement", unique=True)
    region = models.ForeignKey(Region,on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.libelle

class Ville(models.Model):
    code = models.CharField(max_length=100, unique=True)
    libelle = models.CharField(max_length=250, verbose_name="Ville", unique=True)
    region = models.ForeignKey(Departement,on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.libelle