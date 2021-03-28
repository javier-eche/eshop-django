from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField('email address', unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    name = models.CharField(null=False, max_length=100)
    dni = models.CharField(null= False, max_length=10)
    phone = models.CharField(null=True, max_length=15)
    direction = models.CharField(null=False, max_length=255)
    is_superuser = models.BooleanField(default=False)