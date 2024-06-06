from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from .models import Note, Eleve
from .forms import NoteForm

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
    
def note_liste(request):
    notes = Note.objects.all()
    eleves = Eleve.objects.all()  # Assurez-vous de passer la liste des élèves
    return render(request, 'note_liste.html', {'notes': notes, 'eleves': eleves})
