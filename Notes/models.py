from django.db import models

from User.models import Eleve


class UE(models.Model):
    name = models.CharField(max_length=255)
    coefficient = models.FloatField()
    
    def __str__(self):
        return self.name
    
    
class Matiere(models.Model):
    name = models.CharField(max_length=255)
    coefficient = models.FloatField()
    ue = models.ForeignKey(UE, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    

class Note(models.Model):
    note = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
    eleve = models.ForeignKey(Eleve, on_delete=models.CASCADE)
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)

    def __str__(self):
        return self.note
    


    
