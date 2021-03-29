from django.db import models
from users.models import User
from item_order.models import Item

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items_order = models.ManyToManyField(Item)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)