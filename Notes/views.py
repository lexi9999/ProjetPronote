from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.http import require_POST
from Notes.models import Note, Matiere, Semestre, UE
from .forms import NoteForm
from django.views.decorators.csrf import csrf_exempt
import json
from django.db.models import Avg
from User.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

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
def update_note_ajax(request, pk):
    note = get_object_or_404(Note, pk=pk)
    form = NoteForm(request.POST, instance=note)
    if form.is_valid():
        form.save()
        moyenne = Note.objects.filter(matiere=note.matiere).aggregate(Avg('note'))['note__avg']
        return JsonResponse({'success': True, 'note': form.cleaned_data['note'], 'moyenne': moyenne})
    else:
        return JsonResponse({'success': False, 'errors': form.errors})



def note_liste(request, matiere):
    notes = Note.objects.filter(matiere=matiere).select_related('eleve')
    eleves = notes.values_list('eleve', flat=True).distinct()
    return render(request, 'note_liste.html', {'notes': notes, 'eleves': eleves})

@login_required
def matiere_liste(request):
    if isinstance(request.user, Eleve):
        return redirect("notes")
    matieres = Matiere.objects.filter(name_enseignant=request.user)
    return render(request, 'matiere_liste.html', {'matieres': matieres})

def matiere_notes(request, matiere_id):
    matiere = get_object_or_404(Matiere, id=matiere_id)
    notes = Note.objects.filter(matiere=matiere).select_related('eleve')
    notes_data = [
        {
            'eleve': note.eleve.name,
            'note': note.note
        }
        for note in notes
    ]
    return JsonResponse(notes_data, safe=False)

@login_required
def note_main_view(request):
    ues = UE.objects.all()
    notes = Note.objects.filter(eleve=request.user)
    semestres = Semestre.objects.all()
    usertype = 'eleve'
    return render(request, 'main_note.html', {'ues': ues,'notes': notes, 'semestres': semestres, 'usertype': usertype})

@login_required
def note_main_edit(request):
    ues = UE.objects.all()
    matieres = Matiere.objects.filter(name_enseignant=request.user)
    notes = Note.objects.filter(matiere__in=matieres)
    semestres = Semestre.objects.all()
    return render(request, '', {'ues': ues,'notes': notes, 'semestres': semestres, 'matieres': matieres})