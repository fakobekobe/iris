from django.db import models
from datetime import datetime
from etatcivil.models import *
from localisation.models import Quartier
from django.contrib.auth.models import User

# Fonction pour ajouter les détails du temps devant le nom du fichier
def nomfichier(self, fichier):
    return f"{datetime.now().strftime('%d%m%Y%H%M%S')}_{fichier}"
#----------------------------------

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
    nom = models.CharField(max_length=250, null=False, blank=False)
    presidente = models.CharField(max_length=250, null=False, blank=False, default="")
    contact = models.CharField(max_length=100, null=False, blank=False, default="")
    date_adhesion = models.DateField(auto_now=True, verbose_name="Date d'adhésion")
    numero_carte = models.CharField(max_length=250, null=True, blank=True)

    class Meta:
        abstract = True

class Membre(models.Model):
    # Les attribues propres
    nom = models.CharField(max_length=250, null=False,blank=False, verbose_name="Nom")
    prenoms = models.CharField(max_length=250, null=False,blank=False,  default="", verbose_name="Prénoms")
    actif = models.BooleanField(default=False)
    numerobadge = models.CharField(max_length=250, null=False,blank=False, default="", verbose_name="N°Badge")
    qrcode = models.CharField(max_length=250, null=False,blank=False, default="", verbose_name="QR Code")
    dateenre = models.DateTimeField(default=None, null=True, blank=True, verbose_name="Date d'enregistrement")
    contact = models.CharField(max_length=50, null=True, blank=True,default="", verbose_name="Contact")
    adresse = models.CharField(max_length=150, null=True, blank=True,default="", verbose_name="Adresse")

    # Les relations
    secteurs = models.ManyToManyField(Secteur)
    typepiece = models.ForeignKey(TypePiece, null=True, on_delete=models.SET_NULL)
    niveauscolaire = models.ForeignKey(NiveauScolaire, null=True, on_delete=models.SET_NULL)
    sexe = models.ForeignKey(Sexe, null=True, on_delete=models.SET_NULL)
    nationalite = models.ForeignKey(Nationalite, null=True, on_delete=models.SET_NULL)
    parents = models.ManyToManyField("Parent")
    situationmatrimoniale = models.ForeignKey(SituationMatrimoniale, null=True, on_delete=models.SET_NULL)
    quartier = models.ForeignKey(Quartier, null=True, on_delete=models.SET_NULL)

    # A modifier lorsque l'utilisateur sera customisé
    utilisateur = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.nom + " " + self.prenoms

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
    contact = models.CharField(max_length=50, null=True, blank=True, default="", verbose_name="Contact")
    adresse = models.CharField(max_length=150, null=True, blank=True,default="", verbose_name="Adresse")

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
    dateenre = models.DateField(null=True, blank=True, verbose_name="Date d'enregistrement")
    photo = models.ImageField(null=True, blank=True, upload_to=nomfichier)
    typedocument = models.ForeignKey(TypeDocument,default=None, on_delete=models.CASCADE)
    membre = models.ForeignKey(Membre,default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.membre.nom + " - " + self.typedocument.libelle
