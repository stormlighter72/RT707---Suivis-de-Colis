from django.db import models

# Create your models here.

class Entrepot(models.Model):
    name = models.CharField(max_length=30)
    packages = models.ManyToManyField('Package', through = 'PackageEntrepot')