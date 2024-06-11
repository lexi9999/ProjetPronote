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

    

class Eleve2(models.Model):
    num_etudiant = models.CharField(max_length=100)
    NOM = models.CharField(max_length=100)
    Prénom = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=50)