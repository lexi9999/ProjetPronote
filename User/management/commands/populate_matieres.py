from django.core.management.base import BaseCommand
from User.models import Eleve, Note

class Command(BaseCommand):
    help = 'Populate the Matiere model with initial data'

    def handle(self, *args, **kwargs):
        # Récupérez tous les élèves de la base de données
        eleves = Eleve.objects.all()

        # Récupérez toutes les matières
        matieres = [
            "Mathématiques",
            "Physique",
            "Chimie",
            "Biologie",
            "Histoire",
            "Géographie",
            "Langues",
            "Informatique",
            # Ajoutez d'autres matières si nécessaire
        ]

        # Pour chaque élève, créez une note avec une valeur de zéro pour chaque matière
        for eleve in eleves:
            for matiere in matieres:
                Note.objects.get_or_create(eleve=eleve, matiere=matiere, note=0.0)

        self.stdout.write(self.style.SUCCESS('Successfully populated Matiere model with default notes'))
