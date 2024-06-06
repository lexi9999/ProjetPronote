from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Eleve, Note, Matiere
from .forms import NoteForm

def note_liste(request):
    eleves = Eleve.objects.all()
    notes = Note.objects.all()
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('note_liste')
    else:
        form = NoteForm()
    return render(request, 'note_liste.html', {'eleves': eleves, 'notes': notes, 'form': form})
"""""""""
def modifier_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)

    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('note_liste')
    else:
        form = NoteForm(instance=note)

    return redirect('note_liste')

"""""""""
def modifier_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            if request.is_ajax():
                return JsonResponse({'success': True, 'note': form.instance.note})
            return redirect('note_liste')
        else:
            if request.is_ajax():
                return JsonResponse({'success': False, 'errors': form.errors.as_json()})
    
    if request.is_ajax():
        return JsonResponse({'success': False, 'errors': 'Invalid request'})
    
    return redirect('note_liste')


def delete_note(request, note_id):
    if request.method == 'POST':
        note = Note.objects.get(id=note_id)
        note.delete()
    return redirect('note_liste')
