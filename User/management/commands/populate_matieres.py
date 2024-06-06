from django.core.management.base import BaseCommand
from User.models import Matiere  

class Command(BaseCommand):
    help = 'Populate the Matiere model with initial data'

    def handle(self, *args, **kwargs):
        matieres = [
            {"nom": "Mathématiques", "coefficient": 4.0}, 
            {"nom": "Physique", "coefficient": 3.5},
            {"nom": "Chimie", "coefficient": 3.0},
            {"nom": "Biologie", "coefficient": 3.0},
            {"nom": "Informatique", "coefficient": 2.5},
            {"nom": "Langues", "coefficient": 2.0},
            {"nom": "Histoire", "coefficient": 2.0},
            {"nom": "Géographie", "coefficient": 2.0},
            {"nom": "Arts", "coefficient": 1.5},
            {"nom": "Musique", "coefficient": 1.5},
            {"nom": "Éducation physique", "coefficient": 1.0},
        ]

        for matiere in matieres:
            Matiere.objects.create(nom=matiere["nom"], coefficient=matiere["coefficient"])

        self.stdout.write(self.style.SUCCESS('Successfully populated Matiere model with data'))
