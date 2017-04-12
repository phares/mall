from django.db import models
from datetime import date

from oscar.apps.catalogue.abstract_models import AbstractProduct

class Brand(models.Model):
    name = models.CharField(max_length=50)

    @property
    def stock(self):
        return Product.objects.filter(brand=self).count()

    def __str__(self):
        return self.name
    def __unicode__(self):
        return self.name


class Product(AbstractProduct):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    @property
    def is_new(self):
        day_diff = (date.today()-self.date_created.date()).days
        return day_diff > 2

from oscar.apps.catalogue.models import *
