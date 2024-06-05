from django.db import models

class Eleve(models.Model):
    name = models.CharField(max_length=255, unique=True)
    firstName = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    

    def __str__(self):
        return self.email
    
class Enseignant(models.Model):
    name = models.CharField(max_length=255, unique=True)
    firstName = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.email

class Administrateur(models.Model):
    name = models.CharField(max_length=255, unique=True)
    firstName = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.email