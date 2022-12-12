from django.db import models
from projet.models import *

# Liste des méthodes Globales du projet --------
def nombre_membre_par_ville(quartier=None, ville=None):
    """
        Cette méthode permet d'obtenir le nombre de membres par ville
        Ex: quartier = objet quartier ou ville = objet ville
            la valeur de retour = 0 s'il n'y a aucun membre dans cette ville
            la valeur de retour = 12 s'il y a des membres dans cette ville
    """
    if ville:
        return Quartier.objects.filter(membre__quartier__commune__ville__code=ville.code).count()
    else:
        return Quartier.objects.filter(membre__quartier__commune__ville__code=quartier.commune.ville.code).count()

#--------------------------------------------------


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
    commune = models.ForeignKey(Commune, on_delete=models.SET_NULL, null=True)

    # Les methodes
    def __str__(self):
        return self.libelle

    def get_nombre_membre_par_ville(self):
        return nombre_membre_par_ville(quartier=self)

class Marche(models.Model):
    code = models.CharField(max_length=100, unique=True)
    libelle = models.CharField(max_length=250, verbose_name="Marché", unique=True)
    quartier = models.ForeignKey(Quartier, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.libelle