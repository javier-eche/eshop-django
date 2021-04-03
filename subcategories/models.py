from django.db import models
from categories.models import Category


class Subcategory(models.Model):
    name = models.CharField(null=False, blank=False, max_length=15)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name