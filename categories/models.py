from django.db import models

class Category(models.Model):
    name = models.CharField(null=False, blank=False, max_length=15)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
