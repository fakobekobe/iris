from django.db import models

# Create your models here.
class Personne(models.Model):
    nom = models.CharField(max_length=150)

    def __str__(self):
        return self.nom


class Message(models.Model):
    titre = models.CharField(max_length=150)
    message = models.TextField()
    proprietaire = models.ForeignKey(Personne,on_delete=models.CASCADE)
    destinateurs = models.ManyToManyField(Personne,related_name='destinateurs_message')

    def __str__(self):
        return self.titre + ' de ' + self.proprietaire.nom
