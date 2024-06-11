# User/management/commands/populate_enseignants.py

from django.core.management.base import BaseCommand
from User.models import Enseignant

Enseignant.objects.all().delete()

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
            {"name": "FRUCHARD", "firstName": "Augustin", "email": "augustin.fruchard@uha.fr"},
            {"name": "HASSENFORDER", "firstName": "Michel", "email": "michel.hassenforder@uha.fr"},
            {"name": "LIENHARDT", "firstName": "Denis", "email": "denis.lienhardt@uha.fr"},
            {"name": "DEVANNE", "firstName": "Maxime", "email": "maxime.devanne@uha.fr"},
            {"name": "GSCHWIND", "firstName": "Florian", "email": "florian.gschwind@uha.fr"},
            {"name": "PERRONNE", "firstName": "Jean-Marc", "email": "jean-marc.perronne@uha.fr"},
            {"name": "GEMS", "firstName": "Armand", "email": "armand.gems@uha.fr"},
            {"name": "FONDEMENT", "firstName": "Frederic", "email": "frederic.fondement@uha.fr"},
            {"name": "DINTERICH", "firstName": "Jean", "email": "jean.dinterich@uha.fr"},
        ]

        for i, enseignant in enumerate(enseignants, start=1):
            Enseignant.objects.create(
                id=i,
                name=enseignant["name"],
                firstName=enseignant["firstName"],
                email=enseignant["email"],
                password=""  # Make sure to handle passwords securely
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated Enseignant model with emails'))
