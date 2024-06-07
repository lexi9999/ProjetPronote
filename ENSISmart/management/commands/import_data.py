import pandas as pd
from django.core.management.base import BaseCommand
from ENSISmart.models import Eleve2  # Remplacez par votre modèle

class Command(BaseCommand):
    help = 'Import data from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The path to the CSV file')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        data = pd.read_csv(csv_file)

        for index, row in data.iterrows():
            Eleve2.objects.create(
                num_etudiant=row['N° étudiant'],
                NOM=row['NOM'],
                Prénom=row['Prénom'],
                email=row['email'],
                password=row['password'],
                role=row['role']
            )

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))