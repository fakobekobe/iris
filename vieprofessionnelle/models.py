from django.db import models
from datetime import date

class TypeSecteur(models.Model):
    type = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.type

class Secteur(models.Model):
    secteur = models.CharField(max_length=250, unique=True)
    typesecteur = models.ForeignKey(TypeSecteur,null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.secteur

class SecteurActive(models.Model):
    nom = models.CharField(max_length=250,null=False,blank=False)
    date_adhesion = models.DateField(auto_now=True, verbose_name="Date d'adhésion")
    numero_carte = models.CharField(max_length=250,null=True, blank=True)

    class Meta:
        abstract = True

class Membre(models.Model):
    nom = models.CharField(max_length=250, null=False,blank=False)

    def __str__(self):
        return self.nom

class SecteurAgricole(SecteurActive):
    speculation_agricole = models.IntegerField(verbose_name="Spéculation agricole")
    superficie_en_culture = models.IntegerField(verbose_name="Superficie en culture")
    superficie_en_production = models.IntegerField(verbose_name="Superficie en production")
    gps_longitude = models.CharField(max_length=100, null=True, blank=True, verbose_name="GPS Longitude")
    gps_latitude = models.CharField(max_length=100, null=True, blank=True, verbose_name="GPS Latitude")

    membres = models.ManyToManyField(Membre)

    def __str__(self):
        return self.nom

class SecteurInformel(SecteurActive):
    metier = models.CharField(max_length=250, null=False, blank=False, verbose_name="Métier")

    membres = models.ManyToManyField(Membre)

    def __str__(self):
        return self.metier

class SecteurFemmeActive(SecteurActive):
    personne_ressource = models.ForeignKey(Membre, related_name='personne_membre_set',null=True,blank=True, on_delete=models.SET_NULL)

    membres = models.ManyToManyField(Membre)

    def __str__(self):
        return self.nom

class TypeParent(models.Model):
    libelle = models.CharField(max_length=100, verbose_name="Libellé", unique=True)

    def __str__(self):
        return self.libelle

class Parent(models.Model):
    nomprenoms = models.CharField(max_length=250, verbose_name="Nom et prénoms")
    datenaissance = models.DateField(null=True, blank=True, verbose_name="Date de naissance")

    typeparent = models.ForeignKey(TypeParent, on_delete=models.CASCADE)

    def __str__(self):
        return self.nomprenoms


class TypeEtatSante(models.Model):
    libelle = models.CharField(max_length=250, verbose_name="Libellé", unique=True)

    def __str__(self):
        return self.libelle


class EtatSante(models.Model):
    dateenre = models.DateField(null=True, blank=True, verbose_name="Date d'enregistrement")

    typeetatsante = models.ForeignKey(TypeEtatSante, on_delete=models.CASCADE)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.typeetatsante + " le " + self.dateenre


class TypeDocument(models.Model):
    libelle = models.CharField(max_length=250, verbose_name="Libellé", unique=True)

    def __str__(self):
        return self.libelle

class Document(models.Model):
    dateenre = models.DateField(default=date.today(), null=True, blank=True, verbose_name="Date d'enregistrement")
    typedocument = models.ForeignKey(TypeDocument,default=None, on_delete=models.CASCADE)
    membre = models.ManyToManyField(Membre)

    def __str__(self):
        return self.typedocument.libelle
