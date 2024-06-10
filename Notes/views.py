from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.http import require_POST
from Notes.models import Note, Matiere
from .forms import NoteForm
from django.views.decorators.csrf import csrf_exempt
import json
from django.db.models import Avg

#@permission_required('User.edit_note')
def ajouter_note(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('note_liste')
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
            return redirect('note_liste')
    else:
        form = NoteForm(instance=note)
    return render(request, 'modifier_note.html', {'form': form})


""""""""""
@require_POST
def update_note_ajax(request, pk):
    try:
        note = get_object_or_404(Note, pk=pk)
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True, 'note': form.cleaned_data['note'], 'matiere': form.cleaned_data['matiere']})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    except Exception as e:
        return JsonResponse({'success': False, 'errors': str(e)})
  """""""""""

@csrf_exempt
@require_POST
def update_note_ajax(request):
    data = json.loads(request.body)
    note_id = data['note_id']
    new_note = data['note']
    note = get_object_or_404(Note, pk=note_id)
    
    note.note = new_note
    note.save()

    # Calculate the new average
    matiere = note.matiere
    notes = Note.objects.filter(matiere=matiere)
    moyenne = notes.aggregate(Avg('note'))['note__avg']

    response_data = {
        'note': new_note,
        'moyenne': moyenne,
    }

    return JsonResponse(response_data)



def note_liste(request, matiere):
    notes = Note.objects.filter(matiere=matiere).select_related('eleve')
    eleves = notes.values_list('eleve', flat=True).distinct()
    return render(request, 'note_liste.html', {'notes': notes, 'eleves': eleves})

def matiere_liste(request):
    matieres = Matiere.objects.all()
    return render(request, 'matiere_liste.html', {'matieres': matieres})