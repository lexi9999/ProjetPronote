from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
from .forms import NoteForm

@permission_required('User.edit_note')
def ajouter_note(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('note_liste')
    else:
        form = NoteForm()
    return render(request, 'User/ajouter_note.html', {'form': form})

@permission_required('User.edit_note')
def modifier_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('note_liste')
    else:
        form = NoteForm(instance=note)
    return render(request, 'User/modifier_note.html', {'form': form})

def note_liste(request):
    notes = Note.objects.all()
    return render(request, 'User/note_liste.html', {'notes': notes})
