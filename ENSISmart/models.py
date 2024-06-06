from django.db import models
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.hashers import make_password


# Create your models here.


class TemporaryLink(models.Model):
    token = models.CharField(max_length=30, unique=True)
    email = models.EmailField()
    expires_at = models.DateTimeField()

    def is_valid(self):
        return self.expires_at > timezone.now()

class Eleve(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=30)
    is_first_co = models.BooleanField(default=True)
    def __str__(self):
        return self.email
    
class Enseignant(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=30)
    is_first_co = models.BooleanField(default=True)
    def __str__(self):
        return self.email
    
class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=30)
    tag = models.CharField(max_length=10)
    def __str__(self):
        return self.email
    

