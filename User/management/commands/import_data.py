import pandas as pd
from django.core.management.base import BaseCommand
from models import Eleve  # Importer Eleve depuis le fichier models.py dans le même répertoire

class Command(BaseCommand):
    help = 'Import data from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The path to the CSV file')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        data = pd.read_csv(csv_file)

        for index, row in data.iterrows():
            Eleve.objects.create(
                name=row['NOM'],
                firstName=row['Prénom'],
                email=row['email'],
                password=row['password'],
                is_first_co=row['role']
            )

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
