from django.db import models
from datetime import datetime
from django.utils import timezone
from etatcivil.models import *
from localisation.models import Quartier, Commune, Marche
from django.contrib.auth.models import User
from projet.models import *

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
    presidente = models.CharField(max_length=250, null=True, blank=True, default="")
    contact = models.CharField(max_length=100, null=True, blank=True, default="")
    dateenre = models.DateField(default=None, null=True, blank=True, verbose_name="Date d'enregistrement")
    gps_longitude = models.CharField(max_length=100, null=True, blank=True, verbose_name="GPS Longitude")
    gps_latitude = models.CharField(max_length=100, null=True, blank=True, verbose_name="GPS Latitude")

    class Meta:
        abstract = True

class Membre(models.Model):
    # Les attribues propres
    identifiant = models.CharField(max_length=12, null=True,blank=True, default=None, unique=True, verbose_name="Identifiant")
    nom = models.CharField(max_length=250, null=False,blank=False, verbose_name="Nom")
    nomjeunefille = models.CharField(max_length=250, null=True,blank=True,default="", verbose_name="Nom de jeune fille")
    prenoms = models.CharField(max_length=250, null=True,blank=True, default="", verbose_name="Prénoms")
    nom_prenoms = models.CharField(max_length=250, null=True,blank=True, default="",db_index=True, verbose_name="Nom et prénoms")
    actif = models.BooleanField(default=False)
    numerobadge = models.CharField(max_length=250,null=True,blank=True,  default=None, unique=True,verbose_name="N°Badge")
    qrcode = models.CharField(max_length=250,null=True,blank=True, default=None,unique=True,verbose_name="QR Code")
    dateenre = models.DateField(default=None, null=True, blank=True, verbose_name="Date d'enregistrement")
    date_naissance = models.DateField(default=None, null=True, blank=True, verbose_name="Date de naissance")
    contact = models.CharField(max_length=50, default=None, unique=True, verbose_name="Contact")
    numeropiece = models.CharField(max_length=100,default=None, unique=True, verbose_name="N°de la pièce")

    # Les relations
    secteurs = models.ManyToManyField(Secteur)
    typepiece = models.ForeignKey(TypePiece, null=True, on_delete=models.SET_NULL)
    niveauscolaire = models.ForeignKey(NiveauScolaire, null=True, on_delete=models.SET_NULL)
    sexe = models.ForeignKey(Sexe, null=True, on_delete=models.SET_NULL)
    nationalite = models.ForeignKey(Nationalite, null=True, on_delete=models.SET_NULL)
    parents = models.ManyToManyField("Parent")
    situationmatrimoniale = models.ForeignKey(SituationMatrimoniale, null=True, on_delete=models.SET_NULL)
    quartier = models.ForeignKey(Quartier, null=True, on_delete=models.SET_NULL)
    lieunaissance = models.ForeignKey(Commune, null=True, on_delete=models.SET_NULL)

    # A modifier lorsque l'utilisateur sera customisé
    utilisateur = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    # Les methodes
    def __str__(self):
        return self.nom_prenoms

    def set_nomprenoms(self):
        self.nom_prenoms = f"{self.nom} {self.prenoms}"

    def set_identifiant(self):
        self.identifiant = ajoute_zero_a_identifiant(
            departement=self.quartier.commune.ville.departement.code,
            ville=self.quartier.commune.ville.code,
            identifiant=self.id)

    def get_region(self):
        return self.quartier.commune.ville.departement.region.code

class SecteurAgricole(SecteurActive):
    speculation_agricole = models.IntegerField(verbose_name="Spéculation agricole")
    superficie_en_culture = models.IntegerField(verbose_name="Superficie en culture")
    superficie_en_production = models.IntegerField(verbose_name="Superficie en production")

    membres = models.ManyToManyField(Membre, through='MembreSecteurAgricole', through_fields=('secteuragricole', 'membre'))

    def __str__(self):
        return self.nom


class MembreSecteurAgricole(models.Model):
    membre = models.ForeignKey(Membre,on_delete=models.CASCADE)
    secteuragricole = models.ForeignKey(SecteurAgricole,on_delete=models.CASCADE)
    date_adhesion = models.DateField(default=None, null=True, blank=True, verbose_name="Date d'adhésion")
    numero_carte = models.CharField(max_length=250, null=True, blank=True, verbose_name="N°Carte de membre")

    def __str__(self):
        return self.membre.nom + ' ' + self.secteuragricole.nom

class SecteurInformel(SecteurActive):
    metier = models.ForeignKey(Secteur, null=True,blank=True, on_delete=models.SET_NULL)

    membres = models.ManyToManyField(Membre, through="MembreSecteurInformel", through_fields=('secteurinformel','membre'))

    def __str__(self):
        return self.metier.secteur


class MembreSecteurInformel(models.Model):
    membre = models.ForeignKey(Membre,on_delete=models.CASCADE)
    secteurinformel = models.ForeignKey(SecteurInformel,on_delete=models.CASCADE)
    date_adhesion = models.DateField(default=None, null=True, blank=True, verbose_name="Date d'adhésion")
    numero_carte = models.CharField(max_length=250, null=True, blank=True, verbose_name="N°Carte de membre")

    def __str__(self):
        return self.membre.nom + ' ' + self.secteurinformel.nom


class SecteurFemmeActive(SecteurActive):
    personne_ressource = models.ForeignKey(Membre, related_name='personne_membre_set',null=True,blank=True, on_delete=models.SET_NULL)

    marche = models.ForeignKey(Marche, null=True,blank=True, on_delete=models.SET_NULL)
    membres = models.ManyToManyField(Membre, through="MembreSecteurFemmeActive", through_fields=('secteurfemmeactive','membre'))

    def __str__(self):
        return self.nom


class MembreSecteurFemmeActive(models.Model):
    membre = models.ForeignKey(Membre,on_delete=models.CASCADE)
    secteurfemmeactive = models.ForeignKey(SecteurFemmeActive,on_delete=models.CASCADE)
    date_adhesion = models.DateField(default=None, null=True, blank=True, verbose_name="Date d'adhésion")
    numero_carte = models.CharField(max_length=250, null=True, blank=True, verbose_name="N°Carte de membre")

    def __str__(self):
        return self.membre.nom + ' ' + self.secteurfemmeactive.nom


class TypeParent(models.Model):
    libelle = models.CharField(max_length=100, verbose_name="Libellé", unique=True)

    def __str__(self):
        return self.libelle

class Parent(models.Model):
    nomprenoms = models.CharField(max_length=250, verbose_name="Nom et prénoms")
    datenaissance = models.DateField(null=True, blank=True, verbose_name="Date de naissance")
    contact = models.CharField(max_length=50, null=True, blank=True, default="", verbose_name="Contact")
    adresse = models.CharField(max_length=150, null=True, blank=True,default="", verbose_name="Adresse")
    dateenre = models.DateTimeField(default=None, null=True, blank=True, verbose_name="Date d'enregistrement")

    typeparent = models.ForeignKey(TypeParent, on_delete=models.CASCADE)

    def __str__(self):
        return self.nomprenoms


class TypeEtatSante(models.Model):
    libelle = models.CharField(max_length=250, verbose_name="Libellé", unique=True)

    def __str__(self):
        return self.libelle


class EtatSante(models.Model):
    dateenre = models.DateField(null=True, blank=True, default=None, verbose_name="Date d'enregistrement")

    typeetatsante = models.ForeignKey(TypeEtatSante, on_delete=models.CASCADE)
    parent = models.ForeignKey(Parent, null=True, blank=True, default=None, on_delete=models.CASCADE)
    membre = models.ForeignKey(Membre, null=True, blank=True, default=None, on_delete=models.CASCADE)

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
