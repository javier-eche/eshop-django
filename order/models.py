from django.db import models
from item_order.models import Item

class Order(models.Model):
    user_name = models.CharField(null=False, blank=False, max_length=150)
    user_email = models.EmailField(max_length=100)
    user_dni = models.CharField(null=False, blank=False, max_length=9)
    items_order = models.ManyToManyField(Item)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['user_name']
    
    def __str__(self):
        return self.user_name