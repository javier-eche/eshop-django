from django.db import models
from subcategories.models import Subcategory

from cloudinary.models import CloudinaryField


class Product(models.Model):
    name = models.CharField(null=False, blank=False, max_length=100)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    image1 = CloudinaryField('image')
    image2 = CloudinaryField('image')
    image3 = CloudinaryField('image')
    image4 = CloudinaryField('image')
    image5 = CloudinaryField('image')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(null=False, blank=False, max_length=200)
    brand = models.CharField(null=False, blank=False, max_length=50)

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name