const links = document.querySelectorAll('.semester-link');

// Add click event listener to each link
links.forEach(link => {
    link.addEventListener('click', function(event) {

        links.forEach(l => l.classList.remove('disabled'));
        if (!link.classList.contains('disabled')) {
            link.classList.add('disabled');
        }else {
            link.classList.remove('disabled');
        }
        const s_number = link.classList[1]; // Assuming the third class in the classList is the number
        const view_container = document.querySelector('.view-container.' + s_number);
        const view_containers= document.querySelectorAll('.view-container');  // Select view containers with the specified class
        view_containers.forEach(container => {container.classList.remove('selected');})
        view_container.classList.add('selected');
    });
});


document.addEventListener('DOMContentLoaded', (event) => {
    // Fonction pour calculer la moyenne pondérée
    function calculateAverage(notes) {
        let totalWeightedNotes = 0;
        let totalCoefficients = 0;

        notes.forEach(note => {
            const noteValue = parseFloat(note.innerText.split(': ')[1]);
            const coefficient = parseFloat(note.getAttribute('data-coeff'));
            totalWeightedNotes += noteValue * coefficient;
            totalCoefficients += coefficient;
        });

        return totalCoefficients ? (totalWeightedNotes / totalCoefficients).toFixed(2) : '';
    }

    // Parcourir chaque semestre
    document.querySelectorAll('.view-container').forEach(semestreContainer => {
        let totalUEWeightedAverages = 0;
        let totalUECoefficients = 0;

        // Parcourir chaque carte UE dans le semestre
        semestreContainer.querySelectorAll('.UE-card').forEach(ueCard => {
            const notes = ueCard.querySelectorAll('.ul-note h3');
            
            // Vérifier si l'UE a des matières
            if (notes.length > 0) {
                const average = calculateAverage(notes);
                const ueCoefficient = parseFloat(ueCard.getAttribute('data-coeff'));

                // Ajouter la moyenne pondérée de l'UE au total pour la moyenne générale du semestre
                totalUEWeightedAverages += average * ueCoefficient;
                totalUECoefficients += ueCoefficient;

                // Créer et insérer l'élément de moyenne pour chaque UE
                const averageElement = document.createElement('h2');
                averageElement.classList.add('UE-average');
                averageElement.innerText = ` ${average}`;

                ueCard.querySelector('.UE-title').appendChild(averageElement);
            }
        });

        // Calculer et afficher la moyenne générale du semestre
        const generalAverage = totalUECoefficients ? (totalUEWeightedAverages / totalUECoefficients).toFixed(2) : '';
        const generalAverageElement = document.createElement('h1');
        generalAverageElement.innerText = `Moyenne Générale du Semestre: ${generalAverage}`;
        semestreContainer.insertBefore(generalAverageElement, semestreContainer.firstChild);
    });
});