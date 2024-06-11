from django.core.management.base import BaseCommand
from Notes.models import UE, Semestre

class Command(BaseCommand):
    help = 'Populate the UE model with initial data'

    def handle(self, *args, **kwargs):
        ues = [
            {"name": "Mise à niveau Maths", "coefficient": 12, "semestre_name": "S5"},
            {"name": "Immersion", "coefficient": 70, "semestre_name": "S5"},
            {"name": "Maths-Info", "coefficient": 92, "semestre_name": "S5"},
            {"name": "Informatique base", "coefficient": 145, "semestre_name": "S5"},
            {"name": "Développement WEB", "coefficient": 60, "semestre_name": "S5"},
            {"name": "Compétences Humaines, Economiques et Sociales", "coefficient": 28, "semestre_name": "S5"},
            {"name": "Anglais", "coefficient": 24, "semestre_name": "S5"},
            {"name": "Stage Découverte de l'entreprise", "coefficient": 3, "semestre_name": "S5"},
            {"name": "Maths générales", "coefficient": 80, "semestre_name": "S6"},
            {"name": "Ingénierie objet", "coefficient": 76, "semestre_name": "S6"},
            {"name": "Données", "coefficient": 62, "semestre_name": "S6"},
            {"name": "Réseaux et Cybersécurité", "coefficient": 66, "semestre_name": "S6"},
            {"name": "Compétences Humaines, Economiques et Sociales", "coefficient": 86, "semestre_name": "S6"},
        ]

        for ue in ues:
            semestre = Semestre.objects.get(name=ue["semestre_name"])
            UE.objects.create(name=ue["name"], coefficient=ue["coefficient"], semestre=semestre)

        self.stdout.write(self.style.SUCCESS('Successfully populated UE model'))
