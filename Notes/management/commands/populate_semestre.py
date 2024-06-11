from django.core.management.base import BaseCommand
from Notes.models import Semestre

class Command(BaseCommand):
    help = 'Populate the Semestre model with initial data'

    def handle(self, *args, **kwargs):
        semestres = [
            {"name": "S5"},
            {"name": "S6"},
        ]

        for semestre in semestres:
            Semestre.objects.create(name=semestre["name"])

        self.stdout.write(self.style.SUCCESS('Successfully populated Semestre model'))
