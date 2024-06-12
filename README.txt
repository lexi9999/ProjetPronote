GUIDE D'UTILISATION D'ENSISMART


CONFIGURATION

dans le terminal dans le dossier racine du projet:

pip install -r requirements.txt         <- installer les modules nécessaires
python manage.py migrate
python manage.py populate_eleves        <- rajouter des élèves dans la bdd
python manage.py populate_enseignants   <- rajouter des enseignants dans la bdd
python manage.py populate_semestre   
python manage.py populate_ue   
python manage.py populate_matieres  
python manage.py populate_notes   


CONNEXION

1. Sur la page d'accueil, cliquez sur le bouton "Se connecter".
2. Entrez votre identifiant et votre mot de passe.
3. Cochez la case "Se souvenir de moi" si vous souhaitez que le site se souvienne de vos informations de connexion.
4. Cliquez sur le bouton "Se connecter".

Si vous êtes un nouvel utilisateur, cliquez sur "Première connexion / Mot de passe oublié" et entrez votre adresse e-mail UHA pour recevoir un lien par e-mail vous permettant de définir votre mot de passe.


FONCTIONNALITES POUR LES ETUDIANTS

Consultation des notes:

- Une fois connecté, vous accédez à vos notes détaillées pour chaque évaluation et chaque matière.
- Visualisez votre progression académique au fil du temps.
- Identifiez facilement les domaines à améliorer.
- Génération de rapports: Créez des rapports d'absences et de notes personnalisés.

Consultation de l'emploi du temps:

- Visualisez votre emploi du temps hebdomadaire complet.
- Soyez informé des changements d'horaire et des événements à venir.
- Planifiez efficacement votre temps en fonction de vos cours.

Navigation:

Le bouton "Notes" en haut à droite vous permet de basculer entre la vue de vos notes et de vos absences.


FONCTIONNALITES POUR LES ENSEIGNANTS 

- Gestion de l'emploi du temps : importez l'emploi du temps avec icalendar
- Gestion des absences: Ajoutez, modifiez et supprimez facilement les absences des élèves.
- Gestion des notes: Attribuez, modifiez et consultez les notes des élèves pour chaque évaluation en uploadant un fichier cvs.
- Génération de rapports: Créez des rapports des notes de votre classe de vos matières avec clique droit > imprimer


ASSISTANCE

Si vous avez des questions ou rencontrez des problèmes, n'hésitez pas à contacter notre équipe.
