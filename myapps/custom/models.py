from django.db import models
from django.contrib.sites.models import Site

from oscar.core.loading import  get_model

Product = get_model("catalogue", "Product")

class CarouselItem(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to="carousel_images/")
    link = models.URLField(default="")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title
