from datetime import date

from django.db import models
from django.utils.text import slugify

from oscar.apps.catalogue.abstract_models import AbstractProduct

class Brand(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()

    @property
    def stock(self):
        return Product.objects.filter(brand=self).count()

    @models.permalink
    def get_absolute_url(self):
        return ("catalogue:brand", (), {"brand": self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Brand, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    def __unicode__(self):
        return self.name


class Product(AbstractProduct):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    price = models.PositiveIntegerField(default=0)

    @property
    def is_new(self):
        day_diff = (date.today()-self.date_created.date()).days
        return day_diff > 2

from oscar.apps.catalogue.models import *
