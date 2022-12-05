from django.db import models
from abc import ABCMeta, abstractmethod

# Create your models here.
class Personne(models.Model):
    nom = models.CharField(max_length=150)

    def __str__(self):
        return self.nom


class Message(models.Model):
    titre = models.CharField(max_length=150)
    message = models.TextField()
    proprietaire = models.ForeignKey(Personne, on_delete=models.CASCADE)
    destinateurs = models.ManyToManyField(Personne, related_name='destinateurs_message')

    def __str__(self):
        return self.titre + ' de ' + self.proprietaire.nom

class Chapeau(models.Model):
    nom = models.CharField(max_length=255)

    def __str__(self):
        return self.nom

class PersonneR(models.Model):
    personne = models.OneToOneField(Personne, default=None, blank=True, null=True, on_delete=models.SET_NULL)
    chapeau = models.OneToOneField(Chapeau, default=None, blank=True, null=True, on_delete=models.SET_NULL)
    contact = models.CharField(max_length=50)

    def __str__(self):
        return "Personne Ressource avec contact : " + self.contact


class IPersonneR(metaclass=ABCMeta):
    personne = models.OneToOneField(Personne, default=None, blank=True, null=True, on_delete=models.SET_NULL)
    chapeau = models.OneToOneField(Chapeau, default=None, blank=True, null=True, on_delete=models.SET_NULL)

    @abstractmethod
    def presentation(self):
        pass

    def get_parent(self):
        return self.__class__.__name__


class TestPersonneR(IPersonneR):

    def presentation(self):
        return self.__class__.__name__

    def get_nom(self):
        return self.__class__.__name__
