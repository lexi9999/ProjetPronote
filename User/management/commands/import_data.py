import pandas as pd
from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from User.models import Eleve  # Assurez-vous de remplacer 'User' par le nom réel de votre application

class Command(BaseCommand):
    help = 'Importer des données depuis un fichier CSV'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Le chemin vers le fichier CSV')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
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

        for index, row in data.iterrows():
            try:
                # Convertir les valeurs booléennes et gérer les valeurs manquantes
                is_first_co_value = row['Premiere connexion']
                if pd.isna(is_first_co_value):
                    is_first_co_value = True

                eleve = Eleve.objects.create(
                    name=row['NOM'],
                    firstName=row['Prénom'],
                    email=row['email'],
                    password=make_password(row['password']),  # Hashage du mot de passe
                    is_first_co=is_first_co_value,  # Convertir la valeur en booléen
                    last_login=row['Derniere connexion']  # Assigner la valeur de date
                )
                self.stdout.write(self.style.SUCCESS(f"Élève {eleve.email} importé avec succès."))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Erreur lors de l'importation de l'élève à la ligne {index+1}: {e}"))

        self.stdout.write(self.style.SUCCESS('Importation des données terminée avec succès'))
