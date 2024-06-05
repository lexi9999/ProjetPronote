from django.core.management.base import BaseCommand
from User.models import Enseignant  

class Command(BaseCommand):
    help = 'Populate the Enseignant model with initial data'

    def handle(self, *args, **kwargs):
        enseignants = [
            {"name": "DION", "firstName": "Joel", "email": "joel.dion@uha.fr"}, 
            {"name": "ANICIC", "firstName": "Sylvia", "email": "sylvia.anicic@uha.fr"},
            {"name": "THIRY", "firstName": "Laurent", "email": "laurent.thiry@uha.fr"},
            {"name": "STUDER", "firstName": "Philippe", "email": "philippe.studer@uha.fr"},
            {"name": "FORESTIER", "firstName": "Germain", "email": "germain.forestier@uha.fr"},
            {"name": "HILT", "firstName": "Benoit", "email": "benoit.hilt@uha.fr"},
            {"name": "HAYE", "firstName": "Ludovic", "email": "ludovic.haye@uha.fr"},
            {"name": "VIGOUROUX", "firstName": "Christian", "email": "christian.vigouroux@uha.fr"},
            {"name": "RUMA", "firstName": "Corinne", "email": "corinne.ruma@uha.fr"},
            {"name": "GEYER", "firstName": "Cyril", "email": "cyril.geyer@uha.fr"},
            {"name": "WEBER", "firstName": "Jonathan", "email": "jonathan.weber@uha.fr"},
                    
        ]

        for enseignant in enseignants:
            Enseignant.objects.create(name=enseignant["name"], firstName=enseignant["firstName"], email=enseignant["email"])

        self.stdout.write(self.style.SUCCESS('Successfully populated Enseignant model with emails'))
        
    