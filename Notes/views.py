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
import csv
from django.http import HttpResponse
from django.contrib.auth.models import User


def get_current_user(request):
    user_id = request.session.get('current_user_id')
    if user_id:
        return get_object_or_404(User, pk=user_id)
    return None

#@permission_required('User.edit_note')
def ajouter_note(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            matiere_id = form.cleaned_data['matiere'].id
            return redirect('note_liste', matiere=matiere_id)
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
    print(f"note_liste: {request.user.is_authenticated}")
    notes = Note.objects.filter(matiere=matiere).select_related('eleve')
    eleves = notes.values_list('eleve', flat=True).distinct()
    nom_matiere = Matiere.objects.get(id=matiere)
    return render(request, 'note_liste.html', {'notes': notes, 'eleves': eleves, 'matiere': nom_matiere.name})

@login_required
def matiere_liste(request):
    print(f"matiere_liste: {request.user.is_authenticated}")
    if isinstance(request.user, Eleve):
        return redirect("notes")
    matieres = Matiere.objects.filter(name_enseignant=request.user)

    if request.method == "POST":
        form_id = request.POST.get('form_id')
        print(request.POST)

        if form_id:
            # Do whatever you need to do with the form_id
            print("Form ID:", form_id)
            # Then you can redirect or render another view passing this form_id
            # For example:
            return note_liste(request, matiere=form_id)
        
    enseignant_id = request.user.id
    if isinstance(request.user, Eleve):
        return redirect("notes")
    matieres = Matiere.objects.filter(name_enseignant=request.user)
    return render(request, 'matiere_liste.html', {'matieres': matieres, 'enseignant_id': enseignant_id})


def matiere_notes(request, matiere_id):
    print(f"matiere_notes: {request.user.is_authenticated}")
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
    print(f"note_main_view: {request.user.is_authenticated}")
    ues = UE.objects.all()
    notes = Note.objects.filter(eleve=request.user)
    semestres = Semestre.objects.all()
    usertype = 'eleve'
    eleve_id = request.user.id
    return render(request, 'main_note.html', {'ues': ues,'notes': notes, 'semestres': semestres, 'usertype': usertype,  'eleve_id': eleve_id})

@login_required
def note_main_edit(request):
    print(f"note_main_edit: {request.user.is_authenticated}")
    ues = UE.objects.all()
    matieres = Matiere.objects.filter(name_enseignant=request.user)
    notes = Note.objects.filter(matiere__in=matieres)
    semestres = Semestre.objects.all()
    return render(request, '', {'ues': ues,'notes': notes, 'semestres': semestres, 'matieres': matieres})


@login_required
@csrf_exempt
def import_notes(request):
    print(request.user,"   z6e4f8z4ef98z4ef9ze")
    if request.method == "POST":
        csv_file = request.FILES['csv_file']
        if not csv_file.name.endswith('.csv'):
            return HttpResponse("Le fichier n'est pas un CSV")
        
        file_data = csv_file.read().decode("utf-8")
        lines = file_data.split("\n")

        csv_reader = csv.reader(lines)
        next(csv_reader)  # Skip the header row

        for line in csv_reader:
            if line:  # Ignorer les lignes vides
                note_value = float(line[0])
                matiere_id = int(line[1])
                eleve_id = int(line[2])

                matiere = get_object_or_404(Matiere, pk=matiere_id)
                eleve = get_object_or_404(Eleve, pk=eleve_id)

                Note.objects.update_or_create(
                    eleve=eleve,
                    matiere=matiere,
                    defaults={'note': note_value},
                )
        
        # Rediriger vers la liste des notes de la première matière du CSV
        return note_liste(request, matiere_id)
    
    return render(request, 'note_liste.html')

