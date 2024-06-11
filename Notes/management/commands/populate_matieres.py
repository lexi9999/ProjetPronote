# Notes/management/commands/populate_matieres.py
from django.core.management.base import BaseCommand
from User.models import Enseignant
from Notes.models import Matiere, UE

class Command(BaseCommand):
    help = 'Populate the Matiere model with initial data'

    def handle(self, *args, **kwargs):
        matieres = [
            {"name": "Mise à niveau Maths", "coefficient": 12, "nom_enseignant": "DION", "prenom_enseignant": "Joel", "ue_name": "Mise à niveau Maths"},
            {"name": "Immersion", "coefficient": 70, "nom_enseignant": "THIRY", "prenom_enseignant": "Laurent", "ue_name": "Immersion"},
            {"name": "Matématiques discrètes I", "coefficient": 20, "nom_enseignant": "FRUCHARD", "prenom_enseignant": "Augustin", "ue_name": "Maths-Info"},
            {"name": "Mathématiques discrètes II", "coefficient": 24, "nom_enseignant": "FRUCHARD", "prenom_enseignant": "Augustin", "ue_name": "Maths-Info"},
            {"name": "Mathématiques et signal", "coefficient": 28, "nom_enseignant": "DION", "prenom_enseignant": "Joel", "ue_name": "Maths-Info"},
            {"name": "Programmation fonctionnelle & preuves", "coefficient": 20, "nom_enseignant": "THIRY", "prenom_enseignant": "Laurent", "ue_name": "Maths-Info"},
            {"name": "Architecture des ordinateurs", "coefficient": 10, "nom_enseignant": "PERRONNE", "prenom_enseignant": "Jean-Marc", "ue_name": "Informatique base"},
            {"name": "ICG", "coefficient": 26, "nom_enseignant": "THIRY", "prenom_enseignant": "Laurent", "ue_name": "Informatique base"},
            {"name": "Découverte des Réseaux", "coefficient": 25, "nom_enseignant": "HILT", "prenom_enseignant": "Benoit", "ue_name": "Informatique base"},
            {"name": "Unix commandes de base", "coefficient": 24, "nom_enseignant": "HASSENFORDER", "prenom_enseignant": "Michel", "ue_name": "Informatique base"},
            {"name": "Systèmes d'exploitation", "coefficient": 30, "nom_enseignant": "DEVANNE", "prenom_enseignant": "Maxime", "ue_name": "Informatique base"},
            {"name": "Algorithmie et structures de données-C", "coefficient": 30, "nom_enseignant": "LIENHARDT", "prenom_enseignant": "Denis", "ue_name": "Informatique base"},
            {"name": "Technologies WEB I", "coefficient": 20, "nom_enseignant": "DINTERICH", "prenom_enseignant": "Jean", "ue_name": "Développement WEB"},
            {"name": "Technologies WEB II", "coefficient": 20, "nom_enseignant": "DEVANNE", "prenom_enseignant": "Maxime", "ue_name": "Développement WEB"},
            {"name": "Programmation WEB", "coefficient": 20, "nom_enseignant": "WEBER", "prenom_enseignant": "Jonathan", "ue_name": "Développement WEB"},
            {"name": "Communiquer et présenter un prJet", "coefficient": 2, "nom_enseignant": "GSCHWIND", "prenom_enseignant": "Florian", "ue_name": "Compétences Humaines, Economiques et Sociales"},
            {"name": "Analyse de la valeur", "coefficient": 4, "nom_enseignant": "VIGOUROUX", "prenom_enseignant": "Christian", "ue_name": "Compétences Humaines, Economiques et Sociales"},
            {"name": "PrJet Professionnel/Connaissance de soi", "coefficient": 8, "nom_enseignant": "VIGOUROUX", "prenom_enseignant": "Christian", "ue_name": "Compétences Humaines, Economiques et Sociales"},
            {"name": "CV/Lettre de motivation", "coefficient": 4, "nom_enseignant": "VIGOUROUX", "prenom_enseignant": "Christian", "ue_name": "Compétences Humaines, Economiques et Sociales"},
            {"name": "Français - PrJet Voltaire (en ligne)", "coefficient": 18, "nom_enseignant": "VIGOUROUX", "prenom_enseignant": "Christian", "ue_name": "Compétences Humaines, Economiques et Sociales"},
            {"name": "Anglais", "coefficient": 24, "nom_enseignant": "RUMA", "prenom_enseignant": "Corinne", "ue_name": "Anglais"},
            {"name": "Calcul matriciel", "coefficient": 10, "nom_enseignant": "DION", "prenom_enseignant": "Joel", "ue_name": "Maths générales"},
            {"name": "Analyse générale", "coefficient": 10, "nom_enseignant": "DION", "prenom_enseignant": "Joel", "ue_name": "Maths générales"},
            {"name": "Statistiques et systèmes stochastiques", "coefficient": 28, "nom_enseignant": "DION", "prenom_enseignant": "Joel", "ue_name": "Maths générales"},
            {"name": "Analyse numérique et calcul scientifique", "coefficient": 20, "nom_enseignant": "ANICIC", "prenom_enseignant": "Sylvia", "ue_name": "Maths générales"},
            {"name": "PrJet maths", "coefficient": 20, "nom_enseignant": "DION", "prenom_enseignant": "Joel", "ue_name": "Maths générales"},
            {"name": "AOO &langageJava", "coefficient": 32, "nom_enseignant": "THIRY", "prenom_enseignant": "Laurent", "ue_name": "Ingénierie objet"},
            {"name": "UML", "coefficient": 24, "nom_enseignant": "THIRY", "prenom_enseignant": "Laurent", "ue_name": "Ingénierie objet"},
            {"name": "PrJet", "coefficient": 20, "nom_enseignant": "DION", "prenom_enseignant":"Joel", "ue_name": "Ingénierie objet"},
            {"name": "SGBD", "coefficient": 28, "nom_enseignant": "STUDER", "prenom_enseignant": "Philippe", "ue_name": "Données"},
            {"name": "BI", "coefficient": 34, "nom_enseignant": "FORESTIER", "prenom_enseignant": "Germain", "ue_name": "Données"},
            {"name": "Configurations de base", "coefficient": 22, "nom_enseignant": "HILT", "prenom_enseignant": "Benoit", "ue_name": "Réseaux et Cybersécurité"},
            {"name": "Routage et commutations", "coefficient": 34, "nom_enseignant": "HILT", "prenom_enseignant": "Benoit", "ue_name": "Réseaux et Cybersécurité"},
            {"name": "Introduction à la Cyber-sécurité", "coefficient": 10, "nom_enseignant": "HAYE", "prenom_enseignant": "Ludovic", "ue_name": "Réseaux et Cybersécurité"},
            {"name": "Gestion de prJet", "coefficient": 22, "nom_enseignant": "VIGOUROUX", "prenom_enseignant": "Christian", "ue_name": "Compétences Humaines, Economiques et Sociales"},
            {"name": "Introduction à l’économie", "coefficient": 12, "nom_enseignant": "GEMS", "prenom_enseignant": "Armand", "ue_name": "Compétences Humaines, Economiques et Sociales"},
            {"name": "Simulation gestion d’entreprise", "coefficient": 8, "nom_enseignant": "GEMS", "prenom_enseignant": "Armand", "ue_name": "Compétences Humaines, Economiques et Sociales"},
            {"name": "DDRS", "coefficient": 2, "nom_enseignant": "FONDEMENT", "prenom_enseignant": "Frederic", "ue_name": "Compétences Humaines, Economiques et Sociales"},
            {"name": "Bilan carbone", "coefficient": 8, "nom_enseignant": "GEYER", "prenom_enseignant": "Christian", "ue_name": "Compétences Humaines, Economiques et Sociales"},
            {"name": "OJectif emploi", "coefficient": 4, "nom_enseignant": "VIGOUROUX", "prenom_enseignant": "Christian", "ue_name": "Compétences Humaines, Economiques et Sociales"},
            {"name": "Savoir communiquer", "coefficient": 12, "nom_enseignant": "VIGOUROUX", "prenom_enseignant": "Christian", "ue_name": "Compétences Humaines, Economiques et Sociales"},
            {"name": "Journée de l’ingénieur", "coefficient": 6, "nom_enseignant": "VIGOUROUX", "prenom_enseignant": "Christian", "ue_name": "Compétences Humaines, Economiques et Sociales"},
        ]

        for matiere in matieres:
            ue_name = matiere["ue_name"]
            ue = UE.objects.filter(name=ue_name).first()

            if ue is None:
                self.stdout.write(self.style.ERROR(f'UE {ue_name} does not exist'))
                continue

            enseignant_name = matiere["nom_enseignant"]
            enseignant_first_name = matiere["prenom_enseignant"]
            enseignant = Enseignant.objects.filter(name=enseignant_name, firstName=enseignant_first_name).first()

            if enseignant is None:
                self.stdout.write(self.style.ERROR(f'Enseignant {enseignant_first_name} {enseignant_name} does not exist'))
                continue

            Matiere.objects.create(
                name=matiere["name"],
                coefficient=matiere["coefficient"],
                name_enseignant=enseignant,  # Utilisez le nom correct du champ
                ue=ue
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated Matiere model'))