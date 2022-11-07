from django.db import models

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
    personne_ressource = models.ManyToManyField(Membre)

    def __str__(self):
        return self.nom
