from django.db import models
from datetime import datetime
from django.utils import timezone
from etatcivil.models import *
from localisation.models import *
from django.contrib.auth.models import User
from projet.models import *

# Fonction pour ajouter les détails du temps devant le nom du fichier
def nomfichier(self, fichier):
    return f"{datetime.now().strftime('%d%m%Y%H%M%S')}_{fichier}"


def nombre_groupement_par_ville(ville):
    """
        Cette méthode permet d'obtenir le nombre de groupements par ville
        Ex: ville = objet ville
            la valeur de retour = 0 s'il n'y a aucun groupement dans cette ville
            la valeur de retour = 12 s'il y a des groupements dans cette ville
    """
    return SecteurFemmeActive.objects.filter(ville__code=ville.code).count()


#----------------------------------

class TypeSecteur(models.Model):
    type = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.type

class Secteur(models.Model):
    secteur = models.CharField(max_length=250, unique=True)
    typesecteur = models.ForeignKey(TypeSecteur, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.secteur

class Chapeau(models.Model):
    chapeau = models.CharField(max_length=250, unique=True, verbose_name="Chapeau")
    nom = models.CharField(max_length=250, verbose_name="Nom")
    contact = models.CharField(max_length=50, null=True, blank=True, default="", verbose_name="Contact")

    # Liste des methodes
    def __str__(self):
        return self.chapeau

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
    identifiant = models.CharField(max_length=13, null=True,blank=True, default=None, unique=True, verbose_name="Identifiant")
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
            identifiant=self.quartier.get_nombre_membre_par_ville() + 1)  # On fait +1 pour le membre en cours

    def get_region(self):
        return self.quartier.commune.ville.departement.region.code

    def get_nombre_parent(self, libelle):
        return self.parents.filter(typeparent__libelle=libelle).count()

    def get_nouvelle_naissance(self, libelle, datelimite):
        return self.parents.filter(typeparent__libelle=libelle).\
            filter(datenaissance__year__gte=datelimite).count()

    def get_etat_sante(self, id_etat_sante):
        """
        Cette méthode retourne l'état de santé du membre selon le paramètre
        :param id_etat_sante: id du type état de sansté du membre
        :return: 1 si le type du membre existe sinon 0
        """
        return 1 if self.etatsante_set.filter(typeetatsante=id_etat_sante).last() else 0

    def get_nombre_etat_parent(self, parent, id_etat_sante):
        """
        Cette méthode retourne le nombre d'état des parents
        :param parent: le libellé du parent
        :param id_etat_sante: id du type état de sansté du membre
        :return:  0 ou le nombre de décédés
        """
        liste_parent = self.parents.filter(typeparent__libelle=parent)
        total = 0
        for parent in liste_parent:
            total += 1 if parent.etatsante_set.filter(typeetatsante=id_etat_sante).last() else 0
        return total

    def get_lieu_habitation(self):
        return f"{self.quartier.commune.ville.departement.region.district.libelle}/" \
               f"{self.quartier.commune.ville.departement.region.libelle}/" \
               f"{self.quartier.commune.ville.departement.libelle}/" \
               f"{self.quartier.commune.ville.libelle}/" \
               f"{self.quartier.commune.libelle}/" \
               f"{self.quartier.libelle}"

    def get_lieu_naissance(self):
        return f"{self.lieunaissance.commune.ville.departement.region.district.libelle}/" \
               f"{self.lieunaissance.commune.ville.departement.region.libelle}/" \
               f"{self.lieunaissance.commune.ville.departement.libelle}/" \
               f"{self.lieunaissance.commune.ville.libelle}/" \
               f"{self.lieunaissance.commune.libelle}"


class SecteurAgricole(SecteurActive):
    speculation_agricole = models.IntegerField(verbose_name="Spéculation agricole")
    superficie_en_culture = models.IntegerField(verbose_name="Superficie en culture")
    superficie_en_production = models.IntegerField(verbose_name="Superficie en production")

    ville = models.ForeignKey(Ville, default=None, null=True, blank=True, on_delete=models.SET_NULL)
    membres = models.ManyToManyField(Membre, through='MembreSecteurAgricole', through_fields=('secteuragricole', 'membre'))

    def __str__(self):
        return self.nom


class MembreSecteurAgricole(models.Model):
    membre = models.ForeignKey(Membre,on_delete=models.CASCADE)
    secteuragricole = models.ForeignKey(SecteurAgricole,on_delete=models.CASCADE)
    date_adhesion = models.DateField(default=None, null=True, blank=True, verbose_name="Date d'adhésion")
    numero_carte = models.CharField(max_length=250, null=True, blank=True, verbose_name="N°Carte de membre")
    chapeau = models.ForeignKey(Chapeau, default=None, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.membre.nom + ' ' + self.secteuragricole.nom

class SecteurInformel(SecteurActive):
    metier = models.ForeignKey(Secteur, null=True,blank=True, on_delete=models.SET_NULL)
    ville = models.ForeignKey(Ville, default=None, null=True, blank=True, on_delete=models.SET_NULL)
    membres = models.ManyToManyField(Membre, through="MembreSecteurInformel", through_fields=('secteurinformel','membre'))

    def __str__(self):
        return self.metier.secteur


class MembreSecteurInformel(models.Model):
    membre = models.ForeignKey(Membre,on_delete=models.CASCADE)
    secteurinformel = models.ForeignKey(SecteurInformel,on_delete=models.CASCADE)
    date_adhesion = models.DateField(default=None, null=True, blank=True, verbose_name="Date d'adhésion")
    numero_carte = models.CharField(max_length=250, null=True, blank=True, verbose_name="N°Carte de membre")
    chapeau = models.ForeignKey(Chapeau, default=None, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.membre.nom + ' ' + self.secteurinformel.nom


class SecteurFemmeActive(SecteurActive):
    identifiant = models.CharField(max_length=19, null=True, blank=True, default=None, unique=True, verbose_name="Identifiant")

    ville = models.ForeignKey(Ville, default=None, null=True, blank=True, on_delete=models.SET_NULL)
    marche = models.ForeignKey(Marche, null=True, blank=True, default=None, on_delete=models.SET_NULL)
    membres = models.ManyToManyField(Membre, through="MembreSecteurFemmeActive", through_fields=('secteurfemmeactive','membre'))
    quantitegroupement = models.ForeignKey("QuantiteGroupement", default=None, null=True, blank=True, on_delete=models.SET_NULL)

    def set_identifiant(self):
        self.identifiant = f"0{self.quantitegroupement.quantite}{self.ville.departement.region.code}" \
                           f"{ajoute_zero_a_identifiant(departement=self.ville.departement.code, ville=self.ville.code, identifiant=nombre_groupement_par_ville(ville=self.ville) + 1)}"

    def __str__(self):
        return self.nom


class MembreSecteurFemmeActive(models.Model):
    membre = models.ForeignKey(Membre, on_delete=models.CASCADE)
    secteurfemmeactive = models.ForeignKey(SecteurFemmeActive, on_delete=models.CASCADE)
    date_adhesion = models.DateField(default=None, null=True, blank=True, verbose_name="Date d'adhésion")
    numero_carte = models.CharField(max_length=250, null=True, blank=True, verbose_name="N°Carte de membre")
    personneressource = models.ForeignKey("PersonneRessource", null=True, blank=True, default=True, on_delete=models.SET_NULL)
    typeresponsabilite = models.ForeignKey("TypeResponsabilite", null=True, blank=True, default=True, on_delete=models.SET_NULL)
    montantfinancement = models.ForeignKey("MontantFinancement", null=True, blank=True, default=True, on_delete=models.SET_NULL)
    chapeau = models.ForeignKey(Chapeau, default=None, null=True, blank=True, on_delete=models.SET_NULL)

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
        return self.typeetatsante.libelle + " le " + self.dateenre


class TypeDocument(models.Model):
    libelle = models.CharField(max_length=250, verbose_name="Libellé", unique=True)

    def __str__(self):
        return self.libelle

class Document(models.Model):
    dateenre = models.DateField(null=True, blank=True, verbose_name="Date d'enregistrement")
    photo = models.ImageField(null=True, blank=True, upload_to=nomfichier)
    typedocument = models.ForeignKey(TypeDocument,default=None, on_delete=models.CASCADE)
    membre = models.ForeignKey(Membre,default=None, on_delete=models.CASCADE)

    # Liste des methodes
    def __str__(self):
        return self.membre.nom + " - " + self.typedocument.libelle

    def get_photo_membre(self):
        if self.typedocument.libelle == "Photo":
            return self.photo


class TypePersonneRessource(models.Model):
    type = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.type

class PersonneRessource(models.Model):
    membre = models.ForeignKey(Membre, null=True, blank=True, default=None, on_delete=models.SET_NULL)
    chapeau = models.ForeignKey(Chapeau, null=True, blank=True, default=None, on_delete=models.SET_NULL)
    typepersonneressource = models.ForeignKey(TypePersonneRessource, null=True, blank=True, default=None, on_delete=models.SET_NULL)

    def get_personneressource(self):
        if self.membre:
            return self.membre.nom_prenoms
        else:
            return self.chapeau.chapeau

    def get_personneressource_contact(self):
        if self.membre:
            return self.membre.contact
        else:
            return self.chapeau.contact

    def __str__(self):
        return self.get_personneressource()

class QuantiteGroupement(models.Model):
    quantite = models.IntegerField(unique=True, verbose_name="Quantité")

    def __str__(self):
        return self.quantite

class TypeResponsabilite(models.Model):
    type = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.type

class MontantFinancement(models.Model):
    montant = models.IntegerField(unique=True, verbose_name="Montant")

    def __str__(self):
        return self.montant

