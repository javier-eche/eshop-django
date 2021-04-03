from django.db import models
from products.models import Product

class Item(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        ordering = ['product']
    
    def __str__(self):
        return self.product.name