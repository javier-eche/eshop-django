from django.db import models
from products.models import Product

class Item(models.Model):
    product = models.ManyToManyField(Product)
