from django.db import models

class TypeSecteur(models.Model):
    type = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.type
