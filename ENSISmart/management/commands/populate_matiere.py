from django.core.management.base import BaseCommand
from Notes.models import Matiere 

class Command(BaseCommand):
    help = 'Populate the Enseignant model with initial data'

    def handle(self, *args, **kwargs):
        matieres = [
            {"name": "Calcul matriciel", "coefficient": "10", "name_enseignant": "joel.dion@uha.fr", "ue": "Maths"}, 
            
        ]

        for matiere in matieres:
            Matiere.objects.create(name=matiere["name"], coefficient=matiere["coefficient"], name_enseignant=matiere["name_enseignant"], ue=matiere["ue"])

        self.stdout.write(self.style.SUCCESS('Successfully populated Enseignant model with emails'))
        
    