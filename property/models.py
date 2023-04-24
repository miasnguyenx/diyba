from django.db import models
import uuid
import random
from django import forms
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Property(AbstractUser):
    username = models.CharField(max_length=30, default='nameuser', unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(
        default='abc',
        max_length=200,
        )
    def __str__(self) -> str:
        return self.user.username
        
class Product(models.Model):
    code = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         null=False,
         editable = False)
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)