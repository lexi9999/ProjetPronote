from django.core.management.base import BaseCommand
from User.models import Eleve  

class Command(BaseCommand):
    help = 'Populate the Eleve model with initial data'

    def handle(self, *args, **kwargs):
        eleves = [
            {"nom": "ABI ISSI", "prenom": "ELIE"},
            {"nom": "ANTROPIUS", "prenom": "SIMON"},
            {"nom": "AUGEY", "prenom": "LOUIS"},
            {"nom": "BAYA", "prenom": "HAMZA"},
            {"nom": "BENCHAHBOUN", "prenom": "RIM"},
            {"nom": "BEN CHARNIA", "prenom": "SIRINE"},
            {"nom": "BERNARDI", "prenom": "NICOLAS"},
            {"nom": "BOMBA", "prenom": "ROMAIN"},
            {"nom": "BOUARAB", "prenom": "LIZA"},
            {"nom": "BOURICHI", "prenom": "IKRAM"},
            {"nom": "CARBON", "prenom": "BENJAMIN"},
            {"nom": "CHAABANE", "prenom": "MEJDA"},
            {"nom": "CHOUAF", "prenom": "MEHDI"},
            {"nom": "DESMONTEIX", "prenom": "MAXENCE"},
            {"nom": "DOUARD", "prenom": "EVAN"},
            {"nom": "EL MOUJARRADE", "prenom": "DOUAE"},
            {"nom": "ERTZER", "prenom": "LUDOVIC"},
            {"nom": "ESSLINGER", "prenom": "HARRY"},
            {"nom": "FADLALLAH", "prenom": "MOHAMED AMINE"},
            {"nom": "GACHA", "prenom": "MOHAMED"},
            {"nom": "GAILLOT", "prenom": "ALBAN"},
            {"nom": "GAUTHERET", "prenom": "ARNAUD"},
            {"nom": "GIRARDAT", "prenom": "QUENTIN"},
            {"nom": "HAMDANE", "prenom": "WISSAM"},
            {"nom": "IBRAHIM", "prenom": "ALEXIS"},
            {"nom": "JABRI", "prenom": "FADWA"},
            {"nom": "KEMICHA", "prenom": "DORRA"},
            {"nom": "KOUIRI", "prenom": "OUSSAMA"},
            {"nom": "LAHARGOUE", "prenom": "MATTHIS"},
            {"nom": "LAMOUALDA", "prenom": "SALMA"},
            {"nom": "LOUSSOUARN", "prenom": "QUENTIN"},
            {"nom": "MURRIS", "prenom": "VICTOR"},
            {"nom": "NABAT", "prenom": "SALAH-EDDINE"},
            {"nom": "NAJJI", "prenom": "AYA"},
            {"nom": "OUIDIR", "prenom": "NASSIM"},
            {"nom": "OUMALOUL", "prenom": "ZYAD"},
            {"nom": "PRAVEDNYI", "prenom": "OLEG"},
            {"nom": "ROCHDI", "prenom": "YOUSSEF"},
            {"nom": "ROUTIER", "prenom": "REMI"},
            {"nom": "SANCIAUME", "prenom": "MAXIME"},
            {"nom": "SENECHAL", "prenom": "LOUIS"},
            {"nom": "SOUKHRATI", "prenom": "MAROUANE"},
            {"nom": "TAGHOULT OUNMIR", "prenom": "AMRAN"},
            {"nom": "THIAM", "prenom": "MAME YACINE"},
            {"nom": "TIEMTORE", "prenom": "CLOVIS"},
            {"nom": "VANGU", "prenom": "ERWAN"},
            {"nom": "WURTZ", "prenom": "PERRINE"},
        ]

        for eleve in eleves:
            Eleve.objects.create(nom=eleve["nom"], prenom=eleve["prenom"])
        
        self.stdout.write(self.style.SUCCESS('Successfully populated Eleve model'))
