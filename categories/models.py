from django.db import models
from subcategories.models import Subcategory

class Category(models.Model):
    name = models.CharField(null=False, blank=False, max_length=100)
    subcategories = models.ManyToManyField(Subcategory)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
