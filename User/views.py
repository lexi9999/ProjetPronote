from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Avg
from .models import Note, Eleve
from .forms import NoteForm

@csrf_exempt
@require_POST
def update_note_ajax(request, pk):
    if request.META.get('HTTP_X_REQUESTED_WITH') != 'XMLHttpRequest':
        return JsonResponse({'success': False, 'error': 'Invalid request type: Expected AJAX request.'}, status=400)

    try:
        note = get_object_or_404(Note, pk=pk)
    except Note.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Note not found: No note exists with the provided ID.'}, status=404)
    
    form = NoteForm(request.POST, instance=note)
    if form.is_valid():
        try:
            form.save()
            # Calcul de la nouvelle moyenne
            notes = Note.objects.filter(matiere=note.matiere)
            moyenne = notes.aggregate(Avg('note'))['note__avg']
            return JsonResponse({'success': True, 'note': form.cleaned_data['note'], 'matiere': form.cleaned_data['matiere'], 'moyenne': moyenne})
        except Exception as e:
            return JsonResponse({'success': False, 'error': f'Server error: Failed to save the note. Details: {str(e)}'}, status=500)
    else:
        return JsonResponse({'success': False, 'errors': form.errors, 'error': 'Validation error: Provided data is not valid.'}, status=400)

def note_liste(request, matiere):
    notes = Note.objects.filter(matiere=matiere)
    eleves = notes.values_list('eleve', flat=True).distinct()
    moyenne = notes.aggregate(Avg('note'))['note__avg']
    return render(request, 'note_liste.html', {'notes': notes, 'eleves': eleves, 'moyenne': moyenne})

#@permission_required('User.edit_note')
def ajouter_note(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('note_liste', matiere=form.cleaned_data['matiere'])
    else:
        form = NoteForm()
    return render(request, 'ajouter_note.html', {'form': form})

#@permission_required('User.edit_note')
def modifier_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('note_liste', matiere=note.matiere)
    else:
        form = NoteForm(instance=note)
    return render(request, 'modifier_note.html', {'form': form})

def matiere_liste(request):
    matieres = Note.objects.values_list('matiere', flat=True).distinct()
    return render(request, 'matiere_liste.html', {'matieres': matieres})
