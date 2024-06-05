from django.core.management.base import BaseCommand
from User.models import Enseignant  

class Command(BaseCommand):
    help = 'Populate the Enseignant model with initial data'

    def handle(self, *args, **kwargs):
        enseignants = [
            {"nom": "DION", "prenom": "Joel", "email": "joel.dion@uha.fr"}, 
            {"nom": "ANICIC", "prenom": "Sylvia", "email": "sylvia.anicic@uha.fr"},
            {"nom": "THIRY", "prenom": "Laurent", "email": "laurent.thiry@uha.fr"},
            {"nom": "STUDER", "prenom": "Philippe", "email": "philippe.studer@uha.fr"},
            {"nom": "FORESTIER", "prenom": "Germain", "email": "germain.forestier@uha.fr"},
            {"nom": "HILT", "prenom": "Benoit", "email": "benoit.hilt@uha.fr"},
            {"nom": "HAYE", "prenom": "Ludovic", "email": "ludovic.haye@uha.fr"},
            {"nom": "VIGOUROUX", "prenom": "Christian", "email": "christian.vigouroux@uha.fr"},
            {"nom": "RUMA", "prenom": "Corinne", "email": "corinne.ruma@uha.fr"},
            {"nom": "GEYER", "prenom": "Cyril", "email": "cyril.geyer@uha.fr"},
            {"nom": "WEBER", "prenom": "Jonathan", "email": "jonathan.weber@uha.fr"},
                    
        ]

        for enseignant in enseignants:
            Enseignant.objects.create(nom=enseignant["nom"], prenom=enseignant["prenom"], email=enseignant["email"])

        self.stdout.write(self.style.SUCCESS('Successfully populated Enseignant model with emails'))
        
    
