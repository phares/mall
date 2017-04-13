from django.db import models
from django.contrib.sites.models import Site


# Create your models here.

class Carousel(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to="carousel_images/")

    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title
