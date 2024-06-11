import random
from django.core.management.base import BaseCommand
from User.models import Eleve
from Notes.models import Matiere, Note

class Command(BaseCommand):
    help = 'Populate the Note model with initial data'

    def handle(self, *args, **kwargs):
        matieres = Matiere.objects.all()
        eleves = Eleve.objects.all()

        for matiere in matieres:
            for eleve in eleves:
                # Vérifier si une note existe déjà pour cet élève et cette matière
                existing_note = Note.objects.filter(eleve=eleve, matiere=matiere).first()
                if not existing_note:
                    # Générer une note aléatoire entre 0 et 20 uniquement si aucune note n'existe déjà
                    note_value = round(random.uniform(0, 20), 1)
                    Note.objects.create(eleve=eleve, matiere=matiere, note=note_value)

        self.stdout.write(self.style.SUCCESS('Successfully populated Note model with data'))
