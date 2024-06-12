from django.core.management.base import BaseCommand
from User.models import Eleve  

class Command(BaseCommand):
    help = 'Populate the Eleve model with initial data'

    def handle(self, *args, **kwargs):
        eleves = [
            {"name": "ABI ISSI", "firstName": "ELIE"},
            {"name": "ANTROPIUS", "firstName": "SIMON"},
            {"name": "AUGEY", "firstName": "LOUIS"},
            {"name": "BAYA", "firstName": "HAMZA"},
            {"name": "BENCHAHBOUN", "firstName": "RIM"},
            {"name": "BEN CHARNIA", "firstName": "SIRINE"},
            {"name": "BERNARDI", "firstName": "NICOLAS"},
            {"name": "BOMBA", "firstName": "ROMAIN"},
            {"name": "BOUARAB", "firstName": "LIZA"},
            {"name": "BOURICHI", "firstName": "IKRAM"},
            {"name": "CARBON", "firstName": "BENJAMIN"},
            {"name": "CHOUAF", "firstName": "MEHDI"},
            {"name": "DESMONTEIX", "firstName": "MAXENCE"},
            {"name": "DOUARD", "firstName": "EVAN"},
            {"name": "EL MOUJARRADE", "firstName": "DOUAE"},
            {"name": "ERTZER", "firstName": "LUDOVIC"},
            {"name": "ESSLINGER", "firstName": "HARRY"},
            {"name": "FADLALLAH", "firstName": "MOHAMED AMINE"},
            {"name": "GACHA", "firstName": "MOHAMED"},
            {"name": "GAILLOT", "firstName": "ALBAN"},
            {"name": "GAUTHERET", "firstName": "ARNAUD"},
            {"name": "GIRARDAT", "firstName": "QUENTIN"},
            {"name": "HAMDANE", "firstName": "WISSAM"},
            {"name": "IBRAHIM", "firstName": "ALEXIS"},
            {"name": "JABRI", "firstName": "FADWA"},
            {"name": "KEMICHA", "firstName": "DORRA"},
            {"name": "KOUIRI", "firstName": "OUSSAMA"},
            {"name": "LAHARGOUE", "firstName": "MATTHIS"},
            {"name": "LAMOUALDA", "firstName": "SALMA"},
            {"name": "LOUSSOUARN", "firstName": "QUENTIN"},
            {"name": "MURRIS", "firstName": "VICTOR"},
            {"name": "NABAT", "firstName": "SALAH-EDDINE"},
            {"name": "NAJJI", "firstName": "AYA"},
            {"name": "OUIDIR", "firstName": "NASSIM"},
            {"name": "OUMALOUL", "firstName": "ZYAD"},
            {"name": "PRAVEDNYI", "firstName": "OLEG"},
            {"name": "ROCHDI", "firstName": "YOUSSEF"},
            {"name": "ROUTIER", "firstName": "REMI"},
            {"name": "SANCIAUME", "firstName": "MAXIME"},
            {"name": "SENECHAL", "firstName": "LOUIS"},
            {"name": "SOUKHRATI", "firstName": "MAROUANE"},
            {"name": "TAGHOULT OUNMIR", "firstName": "AMRAN"},
            {"name": "THIAM", "firstName": "MAME YACINE"},
            {"name": "TIEMTORE", "firstName": "CLOVIS"},
            {"name": "VANGU", "firstName": "ERWAN"},
            {"name": "WURTZ", "firstName": "PERRINE"},
        ]

        for index, eleve_data in enumerate(eleves, start=1):
            email = f"{eleve_data['firstName'].lower()}.{eleve_data['name'].lower().replace(' ', '')}@uha.fr"
            Eleve.objects.create(id=index, name=eleve_data["name"], firstName=eleve_data["firstName"], email=email)

        self.stdout.write(self.style.SUCCESS('Successfully populated Eleve model with emails'))
