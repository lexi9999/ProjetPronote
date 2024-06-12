$(document).ready(function() {
    $('.matiere-btn').on('click', function() {
        var matiereId = $(this).data('matiere-id');
        $.ajax({
            url: '{% url "matiere_notes" 0 %}'.replace('0', matiereId),
            method: 'GET',
            success: function(data) {
                var notesList = $('#notes-list');
                notesList.empty();
                if (data.length > 0) {
                    data.forEach(function(note) {
                        notesList.append('<p>Élève: ' + note.eleve + ', Note: ' + note.note + '</p>');
                    });
                } else {
                    notesList.append('<p>Aucune note disponible pour cette matière.</p>');
                }
            },
            error: function(xhr, status, error) {
                console.error('Error fetching notes:', error);
            }
        });
    });
});