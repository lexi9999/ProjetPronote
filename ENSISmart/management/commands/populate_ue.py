from django.core.management.base import BaseCommand
from Notes.models import UE

class Command(BaseCommand):
    help = 'Populate the Enseignant model with initial data'

    def handle(self, *args, **kwargs):
        ues = [
            {"name": "Maths générales", "coefficient": "80"},
            {"name": "Ingénierie objet", "coefficient": "76"},
            {"name": "Données", "coefficient": "62"},
            {"name": "Réseaux et Cybersécurité", "coefficient": "66"},
            {"name": "CHES", "coefficient": "86"},
            {"name": "Anglais", "coefficient": "24"}  
        ]

        for ue in ues:
            UE.objects.create(name=ue["name"], coefficient=ue["coefficient"])

        self.stdout.write(self.style.SUCCESS('Successfully populated UE model'))
        
    