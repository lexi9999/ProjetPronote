from django.db import models
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class Eleve(AbstractBaseUser):
    id = models.AutoField(primary_key=True) 
    name = models.CharField(max_length=255)
    firstName = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255, null=True)
    is_first_co = models.BooleanField(default=True)
    last_login = models.DateTimeField(auto_now_add=True, null=True)
    is_active = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return "Eleve: " +  self.name + " " + self.firstName
    
class Enseignant(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    firstName = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255, null=True)
    is_first_co = models.BooleanField(default=True)
    last_login = models.DateTimeField(auto_now_add=True, null=True)
    is_active = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return "Enseignant: " + self.name +" "+ self.firstName

class Administrateur(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    firstName = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255, null=True)
    last_login = models.DateTimeField(auto_now_add=True, null=True)
    is_active = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email