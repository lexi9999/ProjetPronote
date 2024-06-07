from django.core.management.base import BaseCommand
from User.models import Enseignant
from Notes.models import Matiere, UE

class Command(BaseCommand):
    help = 'Populate the Matiere model with initial data'

    def handle(self, *args, **kwargs):
        matieres = [
            # Semestre 5
            {"name": "Mise à niveau Maths", "coefficient": 12, "nom_enseignant": "DION", "prenom_enseignant": "Joel", "ue_name": "Mise à niveau Maths"},
            {"name": "Immersion", "coefficient": 70, "nom_enseignant": "THIRY", "prenom_enseignant": "Laurent", "ue_name": "Immersion"},
            {"name": "Matématiques discrètes I", "coefficient": 20, "nom_enseignant": "Fruchard", "prenom_enseignant": "Augustin", "ue_name": "Maths-Info"},
            {"name": "Mathématiques discrètes II", "coefficient": 24, "nom_enseignant": "Fruchard", "prenom_enseignant": "Augustin", "ue_name": "Maths-Info"},
            {"name": "Mathématiques et signal", "coefficient": 28, "nom_enseignant": "DION", "prenom_enseignant": "Joel", "ue_name": "Maths-Info"},
            {"name": "Programmation fonctionnelle & preuves", "coefficient": 20, "nom_enseignant": "THIRY", "prenom_enseignant": "Laurent", "ue_name": "Maths-Info"},
            {"name": "Architecture des ordinateurs", "coefficient": 10, "nom_enseignant": "Perronne", "prenom_enseignant": "Jean-Marc", "ue_name": "Informatique base"},
            {"name": "ICG", "coefficient": 26, "nom_enseignant": "THIRY", "prenom_enseignant": "Laurent", "ue_name": "Informatique base"},
            {"name": "Découverte des Réseaux", "coefficient": 25, "nom_enseignant": "Hilt", "prenom_enseignant": "Benoit", "ue_name": "Informatique base"},
            {"name": "Unix commandes de base", "coefficient": 24, "nom_enseignant": "Hassenforder", "prenom_enseignant": "Michel", "ue_name": "Informatique base"},
            {"name": "Systèmes d'exploitation", "coefficient": 30, "nom_enseignant": "Devanne", "prenom_enseignant": "Maxime", "ue_name": "Informatique base"},
            {"name": "Algorithmie et structures de données-C", "coefficient": 30, "nom_enseignant": "Lienhardt", "prenom_enseignant": "Denis", "ue_name": "Informatique base"},
            {"name": "Technologies WEB I", "coefficient": 20, "nom_enseignant": "Dinterich", "prenom_enseignant": "Jean", "ue_name": "Développement WEB"},
            {"name": "Technologies WEB II", "coefficient": 20, "nom_enseignant": "Devanne", "prenom_enseignant": "Maxime", "ue_name": "Développement WEB"},
            {"name": "Programmation WEB", "coefficient": 20, "nom_enseignant": "Weber", "prenom_enseignant": "Jonathan", "ue_name": "Développement WEB"},
            {"name": "Communiquer et présenter un prJet", "coefficient": 2, "nom_enseignant": "Gschwind", "prenom_enseignant": "Florian", "ue_name": "Compétences Humaines, Economiques et Sociales"},
            {"name": "Analyse de la valeur", "coefficient": 4, "nom_enseignant": "Vigouroux", "prenom_enseignant": "Christian", "ue_name": "Compétences Humaines, Economiques et Sociales"},
            {"name": "PrJet Professionnel/Connaissance de soi", "coefficient": 8, "nom_enseignant": "Vigouroux", "prenom_enseignant": "Christian", "ue_name": "Compétences Humaines, Economiques et Sociales"},
            {"name": "CV/Lettre de motivation", "coefficient": 4, "nom_enseignant": "Vigouroux", "prenom_enseignant": "Christian", "ue_name": "Compétences Humaines, Economiques et Sociales"},
            {"name": "Français - PrJet Voltaire (en ligne)", "coefficient": 18, "nom_enseignant": "Vigouroux", "prenom_enseignant": "Christian", "ue_name": "Compétences Humaines, Economiques et Sociales"},
            {"name": "Anglais", "coefficient": 24, "nom_enseignant": "Ruma", "prenom_enseignant": "Corinne", "ue_name": "Anglais"},
            
            # Semestre 6
            {"name": "Calcul matriciel", "coefficient": 10, "nom_enseignant": "Dion", "prenom_enseignant": "Joel", "ue_name": "Maths générales"},
            {"name": "Analyse générale", "coefficient": 10, "nom_enseignant": "Dion", "prenom_enseignant": "Joel", "ue_name": "Maths générales"},
            {"name": "Statistiques et systèmes stochastiques", "coefficient": 28, "nom_enseignant": "Dion", "prenom_enseignant": "Joel", "ue_name": "Maths générales"},
            {"name": "Analyse numérique et calcul scientifique", "coefficient": 20, "nom_enseignant": "Anicic", "prenom_enseignant": "Sylvia", "ue_name": "Maths générales"},
            {"name": "PrJet maths", "coefficient": 20, "nom_enseignant": "Dion", "prenom_enseignant": "Joel", "ue_name": "Maths générales"},
            {"name": "AOO &langageJava", "coefficient": 32, "nom_enseignant": "Thiry", "prenom_enseignant": "Laurent", "ue_name": "Ingénierie oJet"},
            {"name": "UML", "coefficient": 24, "nom_enseignant": "Thiry", "prenom_enseignant": "Laurent", "ue_name": "Ingénierie oJet"},
            {"name": "PrJet", "coefficient": 20, "nom_enseignant": "Dion", "prenom_enseignant":"Joel", "ue_name": "Ingénierie oJet"},
            {"name": "SGBD", "coefficient": 28, "nom_enseignant": "Studer", "prenom_enseignant": "Philippe", "ue_name": "Données"},
            {"name": "BI", "coefficient": 34, "nom_enseignant": "Forestier", "prenom_enseignant": "Germain", "ue_name": "Données"},
            {"name": "Configurations de base", "coefficient": 22, "nom_enseignant": "Hilt", "prenom_enseignant": "Benoit", "ue_name": "Réseaux et Cybersécurité"},
            {"name": "Routage et commutations", "coefficient": 34, "nom_enseignant": "Hilt", "prenom_enseignant": "Benoit", "ue_name": "Réseaux et Cybersécurité"},
            {"name": "Introduction à la Cyber-sécurité", "coefficient": 10, "nom_enseignant": "Haye", "prenom_enseignant": "Ludovic", "ue_name": "Réseaux et Cybersécurité"},
            {"name": "Gestion de prJet", "coefficient": 22, "nom_enseignant": "Vigouroux", "prenom_enseignant": "Christian", "ue_name": "Compétences Humaines, Économiques et Sociales"},
            {"name": "Introduction à l’économie", "coefficient": 12, "nom_enseignant": "Gems", "prenom_enseignant": "Armand", "ue_name": "Compétences Humaines, Économiques et Sociales"},
            {"name": "Simulation gestion d’entreprise", "coefficient": 8, "nom_enseignant": "Gems", "prenom_enseignant": "Armand", "ue_name": "Compétences Humaines, Économiques et Sociales"},
            {"name": "DDRS", "coefficient": 2, "nom_enseignant": "Fondement", "prenom_enseignant": "Frederic", "ue_name": "Compétences Humaines, Économiques et Sociales"},
            {"name": "Bilan carbone", "coefficient": 8, "nom_enseignant": "Geyer", "prenom_enseignant": "Christian", "ue_name": "Compétences Humaines, Économiques et Sociales"},
        
            {"name": "OJectif emploi", "coefficient": 4, "nom_enseignant": "Vigouroux", "prenom_enseignant": "Christian", "ue_name": "Compétences Humaines, Économiques et Sociales"},
            {"name": "Savoir communiquer", "coefficient": 12, "nom_enseignant": "Vigouroux", "prenom_enseignant": "Christian", "ue_name": "Compétences Humaines, Économiques et Sociales"},
            {"name": "Journée de l’ingénieur", "coefficient": 6, "nom_enseignant": "Vigouroux", "prenom_enseignant": "Christian", "ue_name": "Compétences Humaines, Économiques et Sociales"},

            {"name": "Anglais", "coefficient": 24, "nom_enseignant": "Ruma", "prenom_enseignant": "Corinne", "ue_name": "Anglais"},
        ]

        for matiere in matieres:
            enseignant = None
            if matiere["nom_enseignant"] and matiere["prenom_enseignant"]:
                enseignant = Enseignant.objects.get(name=matiere["nom_enseignant"], firstName=matiere["prenom_enseignant"])
            ue = UE.objects.get(name=matiere["ue_name"])
            Matiere.objects.create(name=matiere["name"], coefficient=matiere["coefficient"], name_enseignant=enseignant, ue=ue)

        self.stdout.write(self.style.SUCCESS('Successfully populated Matiere model'))

