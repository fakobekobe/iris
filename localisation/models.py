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
    departement = models.ForeignKey(Departement,on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.libelle

class Commune(models.Model):
    code = models.CharField(max_length=100, unique=True)
    libelle = models.CharField(max_length=250, verbose_name="Commune", unique=True)
    ville = models.ForeignKey(Ville,on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.libelle

class Quartier(models.Model):
    code = models.CharField(max_length=100, unique=True)
    libelle = models.CharField(max_length=250, verbose_name="Quartier", unique=True)
    commune = models.ForeignKey(Commune,on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.libelle

class Marche(models.Model):
    code = models.CharField(max_length=100, unique=True)
    libelle = models.CharField(max_length=250, verbose_name="Marché", unique=True)
    quartier = models.ForeignKey(Quartier,on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.libelle