from django.core.management.base import BaseCommand
from User.models import Enseignant

class Command(BaseCommand):
    help = 'Populate the Enseignant model with initial data'

    def handle(self, *args, **kwargs):
        enseignants = [
            {"nom": "DION", "firstName": "Joel", "email": "joel.dion@uha.fr"},
            {"nom": "ANICIC", "firstName": "Sylvia", "email": "sylvia.anicic@uha.fr"},
            {"nom": "THIRY", "firstName": "Laurent", "email": "laurent.thiry@uha.fr"},
            {"nom": "STUDER", "firstName": "Philippe", "email": "philippe.studer@uha.fr"},
            {"nom": "FORESTIER", "firstName": "Germain", "email": "germain.forestier@uha.fr"},
            {"nom": "HILT", "firstName": "Benoit", "email": "benoit.hilt@uha.fr"},
            {"nom": "HAYE", "firstName": "Ludovic", "email": "ludovic.haye@uha.fr"},
            {"nom": "VIGOUROUX", "firstName": "Christian", "email": "christian.vigouroux@uha.fr"},
            {"nom": "RUMA", "firstName": "Corinne", "email": "corinne.ruma@uha.fr"},
            {"nom": "GEYER", "firstName": "Cyril", "email": "cyril.geyer@uha.fr"},
            {"nom": "WEBER", "firstName": "Jonathan", "email": "jonathan.weber@uha.fr"},
            {"nom": "FRUCHARD", "firstName": "Augustin", "email": "augustin.fruchard@uha.fr"},
            {"nom": "HASSENFORDER", "firstName": "Michel", "email": "michel.hassenforder@uha.fr"},
            {"nom": "LIENHARDT", "firstName": "Denis", "email": "denis.lienhardt@uha.fr"},
            {"nom": "DEVANNE", "firstName": "Maxime", "email": "maxime.devanne@uha.fr"},
            {"nom": "GSCHWIND", "firstName": "Florian", "email": "florian.gschwind@uha.fr"},
            {"nom": "PERRONNE", "firstName": "Jean-Marc", "email": "jean-marc.perronne@uha.fr"},
            {"nom": "GEMS", "firstName": "Armand", "email": "armand.gems@uha.fr"},
            {"nom": "FONDEMENT", "firstName": "Frederic", "email": "frederic.fondement@uha.fr"},
            {"nom": "DINTERICH", "firstName": "Jean", "email": "jean.dinterich@uha.fr"},
        ]

        for enseignant in enseignants:
            Enseignant.objects.create(
                name=enseignant["nom"],
                firstName=enseignant["firstName"],
                email=enseignant["email"],
                password="" 
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated Enseignant model with emails'))
