from django.db import models
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

<<<<<<< HEAD
class Eleve(models.Model):
    id = models.AutoField(primary_key=True) 
=======
class Eleve(AbstractBaseUser):
>>>>>>> 5bdf2b3663d5f5787b3391e31a0301388388747f
    name = models.CharField(max_length=255, unique=True)
    firstName = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255, null=True)
    is_first_co = models.BooleanField(default=True)
    last_login = models.DateTimeField(auto_now_add=True, null=True)
<<<<<<< HEAD
       
=======
    is_active = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
>>>>>>> 5bdf2b3663d5f5787b3391e31a0301388388747f

    def __str__(self):
        return "Eleve: " +  self.name + " " + self.firstName
    
<<<<<<< HEAD
class Enseignant(models.Model):
    id = models.AutoField(primary_key=True)
=======
class Enseignant(AbstractBaseUser):
>>>>>>> 5bdf2b3663d5f5787b3391e31a0301388388747f
    name = models.CharField(max_length=255, unique=True)
    firstName = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255, null=True)
    is_first_co = models.BooleanField(default=True)
    last_login = models.DateTimeField(auto_now_add=True, null=True)
<<<<<<< HEAD
    
=======
    is_active = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

>>>>>>> 5bdf2b3663d5f5787b3391e31a0301388388747f
    def __str__(self):
        return "Enseignant: " + self.name +" "+ self.firstName

<<<<<<< HEAD
class Administrateur(models.Model):
    id = models.AutoField(primary_key=True)
=======
class Administrateur(AbstractBaseUser):
>>>>>>> 5bdf2b3663d5f5787b3391e31a0301388388747f
    name = models.CharField(max_length=255, unique=True)
    firstName = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255, null=True)
    last_login = models.DateTimeField(auto_now_add=True, null=True)
<<<<<<< HEAD
    
=======
    is_active = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

>>>>>>> 5bdf2b3663d5f5787b3391e31a0301388388747f
    def __str__(self):
        return self.email