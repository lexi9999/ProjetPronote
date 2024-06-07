from django.db import models
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.hashers import make_password

class Eleve(models.Model):
    name = models.CharField(max_length=255, unique=True)
    firstName = models.CharField(max_length=255)
    email = models.EmailField(unique=True, primary_key=True)
    password = models.CharField(max_length=255)
    is_first_co = models.BooleanField(default=True)
    

    def __str__(self):
        return self.email
    
class Enseignant(models.Model):
    name = models.CharField(max_length=255, unique=True)
    firstName = models.CharField(max_length=255)
    email = models.EmailField(unique=True, primary_key=True)
    password = models.CharField(max_length=255)
    is_first_co = models.BooleanField(default=True)

    def __str__(self):
        return self.email

class Administrateur(models.Model):
    name = models.CharField(max_length=255, unique=True)
    firstName = models.CharField(max_length=255)
    email = models.EmailField(unique=True, primary_key=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.email