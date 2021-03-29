from django.db import models


class Subcategory(models.Model):
    name = models.CharField(null=False, blank=False, max_length=100)

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name