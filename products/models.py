from django.db import models
from subcategories.models import Subcategory


class Product(models.Model):
    name = models.CharField(null=False, blank=False, max_length=100)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    image1 = models.ImageField(upload_to='products/', null=True, blank=True)
    image2 = models.ImageField(upload_to='products/', null=True, blank=True)
    image3 = models.ImageField(upload_to='products/', null=True, blank=True)
    image4 = models.ImageField(upload_to='products/', null=True, blank=True)
    image5 = models.ImageField(upload_to='products/', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(null=False, blank=False, max_length=200)
    brand = models.CharField(null=False, blank=False, max_length=50)

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name