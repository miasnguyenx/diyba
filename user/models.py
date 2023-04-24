from django.db import models
from django import forms
from django.contrib.auth.models import AbstractUser

'''
asdfasdf
'''

class User(AbstractUser):
    username = models.CharField(max_length=30, default='nameuser', unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(
        default='abc',
        max_length=200,
        )
    def __str__(self):
        return self.user.username


class UserCOntact(models.Model):
    first_name = models.CharField(max_length=30, default="firstname")
    last_name = models.CharField(max_length=30, default="lastname")
    phone_number = models.CharField(max_length=30, default="00000")
    postcode = models.CharField(max_length=30)
    
