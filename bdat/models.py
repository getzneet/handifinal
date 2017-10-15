from django.db import models

# Create your models here.

class Institution(models.Model):
    nom = models.CharField(max_length=100, null=True)
    source = models.TextField(null=True)
    article = models.TextField(null=True)
    type = models.CharField(max_length=100, null=True)
    pays = models.CharField(max_length=100, null=True)
    where = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.nom

class Technology(models.Model):
    nom = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    prix = models.FloatField(null=True)
    age = models.CharField(max_length=100, null=True)
    type_techno = models.CharField(max_length=100, null=True)
    activite = models.CharField(max_length=100, null=True)
    commentaires = models.CharField(max_length=100, null=True)
    source = models.CharField(max_length=100, null=True)
    article = models.TextField(null=True)
    entreprise = models.CharField(max_length=100, null=True)
    patho = models.CharField(max_length=100, null=True)
    cif = models.CharField(max_length=100, null=True)
    fonction = models.CharField(max_length=100, null=True)
    idx = models.IntegerField(max_length=100, null=True)

    def __str__(self):
        return self.nom
