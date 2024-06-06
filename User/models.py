from django.db import models

class Utilisateur(models.Model):
    prenom = models.CharField(max_length=50)
    nom = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=12)

    def __str__(self):
        return f"{self.prenom} {self.nom}"

class Eleve(Utilisateur):
    TD= models.CharField(max_length=4)
    TD=models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nom} {self.prenom}'

class Enseignant(Utilisateur):
    matieres = models.ManyToManyField('Matiere')

    def __str__(self):
        return f'{self.nom} {self.prenom}'
    
    class Meta:
        permissions = [
            ("edit_note", "Peut ajouter et modier des notes"),
        ]

class Matiere(models.Model):
    nom= models.CharField(max_length=100)
    coefficient= models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.nom


class Note(models.Model):
    eleve = models.ForeignKey(Eleve, on_delete=models.CASCADE)
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    note = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        unique_together = ('eleve', 'matiere')
