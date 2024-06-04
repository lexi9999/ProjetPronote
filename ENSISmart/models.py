from django.db import models
from django.utils.translation import gettext as _


class Events(models.Model):
    name = models.CharField(max_length=255,null=True,blank=True)
    start = models.DateTimeField(null=True,blank=True)
    end = models.DateTimeField(null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = _('Calendar Events')
        verbose_name_plural = _('Calendar Events')


class Eleve(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)


class Absence(models.Model):
    eleve = models.ForeignKey(Eleve, on_delete=models.CASCADE)
    event = models.ForeignKey(Events, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Absence'
        verbose_name_plural = 'Absences'