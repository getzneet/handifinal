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

    # technology's name
    nom = models.CharField(max_length=100, null=True, blank=True)

    # description
    description = models.TextField(null=True, blank=True)

    # price
    prix = models.FloatField(null=True, blank=True)

    # age slice
    age = models.CharField(max_length=100, null=True, blank=True)

    # source
    source = models.CharField(max_length=100, null=True, blank=True)
    article = models.TextField(null=True, blank=True)

    # company developping the technology
    entreprise = models.CharField(max_length=100, null=True, blank=True)

    # classification
    classification = models.CharField(max_length=100, null=True, blank=True)

    # video showing the techno
    video = models.TextField(blank=True)

    # image
    image = models.ImageField(upload_to="img/technos/")

    # is the techno visible on the website?
    # has to be set to true after a form submission
    # in order to see the techno on the website
    show = models.NullBooleanField(null=True, blank=True)

    tag1 = models.CharField(max_length=100, null=True, blank=True)
    tag2 = models.CharField(max_length=100, null=True, blank=True)
    tag3 = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.nom
