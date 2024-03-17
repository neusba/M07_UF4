from django.db import models

# Create your models here.

class User(models.Model):
    nom = models.CharField(max_length=30)
    cognom = models.CharField(max_length=30)
    cognom2 = models.EmailField(max_length=30)
    correu = models.CharField(max_length=30)
    curs = models.CharField(max_length=30)