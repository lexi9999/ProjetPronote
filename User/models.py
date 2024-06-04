from django.db import models

# Create your models here.
class Utilisateur(models.Model):
    prenom = models.CharField(max_length=50)
    nom = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length = 12)

    def __str__(self):
        return f"{self.prenom} {self.nom}"


class Eleve(Utilisateur):
    TP = models.CharField(max_length=4)
    TD = models.CharField(max_length=4)


class Enseignant(Utilisateur):
    matiere = models.CharField(max_length=100)
    class Meta:
        permissions = [
            ("edit_note", "Peut ajouter et modier des notes"),
        ]

class Note(models.Model):
    eleve = models.ForeignKey(Eleve, on_delete=models.CASCADE)
    enseignant = models.ForeignKey(Enseignant, on_delete=models.CASCADE, blank=True)
    matiere = models.CharField(max_length=100, blank=True)
    note = models.DecimalField(max_digits=5, decimal_places=2)
    commentaire = models.TextField(blank=True)
    coefficient = models.IntegerField(blank = False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.eleve} - {self.matiere} - {self.note}"