from django.db import models
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.hashers import make_password

class Eleve(models.Model):
    name = models.CharField(max_length=255, unique=True)
    firstName = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255, null=True)
    is_first_co = models.BooleanField(default=True)
    last_login = models.DateTimeField(auto_now_add=True, null=True)
    id = models.AutoField(primary_key=True, default=0)    

    def __str__(self):
        return "Eleve: " +  self.email
    
class Enseignant(models.Model):
    name = models.CharField(max_length=255, unique=True)
    firstName = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255, null=True)
    is_first_co = models.BooleanField(default=True)
    last_login = models.DateTimeField(auto_now_add=True, null=True)
    id = models.AutoField(primary_key=True, default=0)
    def __str__(self):
        return "Enseignant: " + self.email

class Administrateur(models.Model):
    name = models.CharField(max_length=255, unique=True)
    firstName = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255, null=True)
    last_login = models.DateTimeField(auto_now_add=True, null=True)
    id = models.AutoField(primary_key=True, default=0)
    def __str__(self):
        return self.email