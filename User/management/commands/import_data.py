import pandas as pd
from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from User.models import Eleve, Enseignant

class Command(BaseCommand):
    help = 'Importer des données depuis un fichier CSV'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Le chemin vers le fichier CSV')
        parser.add_argument('--eleves', action='store_true', help='Importer des élèves')
        parser.add_argument('--enseignants', action='store_true', help='Importer des enseignants')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        eleves = kwargs['eleves']
        enseignants = kwargs['enseignants']

        if not eleves and not enseignants:
            self.stdout.write(self.style.ERROR("Veuillez spécifier si vous voulez importer des élèves (--eleves) ou des enseignants (--enseignants)."))
            return
        elif eleves and enseignants:
            self.stdout.write(self.style.ERROR("Veuillez spécifier un seul type d'importation : élèves (--eleves) ou enseignants (--enseignants), pas les deux."))
            return

        try:
            data = pd.read_csv(csv_file)
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f"Le fichier {csv_file} n'a pas été trouvé."))
            return
        except pd.errors.EmptyDataError:
            self.stdout.write(self.style.ERROR("Le fichier est vide."))
            return
        except pd.errors.ParserError:
            self.stdout.write(self.style.ERROR("Erreur de parsing dans le fichier CSV."))
            return

        if eleves:
            model = Eleve
        elif enseignants:
            model = Enseignant

        for index, row in data.iterrows():
            try:
                obj = model.objects.create(
                    name=row['NOM'],
                    firstName=row['Prénom'],
                    email=row['email'],
                    password=make_password(row['password']),  # Hashage du mot de passe
                    is_first_co=True if pd.isna(row['Premiere connexion']) else False,  # Convertir la valeur en booléen
                    last_login=row['Derniere connexion'] if pd.notna(row['Derniere connexion']) else None,  # Assigner la valeur de date
                    is_active=False if pd.isna(row['est actif']) else True
                )
                self.stdout.write(self.style.SUCCESS(f"{model.__name__} {obj.name} {obj.firstName} importé avec succès."))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Erreur lors de l'importation de {model.__name__} à la ligne {index+1}: {e}"))

        self.stdout.write(self.style.SUCCESS(f'Importation des données terminée avec succès'))
