from django.utils.translation import gettext as _
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from icalendar import Calendar
from django.http import JsonResponse
import datetime
import requests
from .models import Events, Absence, Eleve
from django.core.serializers.json import DjangoJSONEncoder
import json

def index(request, enseignant_id):
    all_events = Events.objects.all()
    context = {
        "events":all_events,
        "enseignant_id": enseignant_id,  # Add enseignant_id to the context
    }
    return render(request,'Absences/calendar.html',context)

def all_events(request):
    all_events = Events.objects.all()
    out = []
    for event in all_events:
        out.append({
            'title': event.name,
            'id': event.id,
            'start': event.start.strftime("%m/%d/%Y, %H:%M:%S") if event.start else None,
            'end': event.end.strftime("%m/%d/%Y, %H:%M:%S") if event.end else None,
        })

    return JsonResponse(out, safe=False)

def add_event(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    event = Events(name=str(title), start=start, end=end)
    event.save()
    data = {}
    return JsonResponse(data)
 
def update(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    id = request.GET.get("id", None)
    event = Events.objects.get(id=id)
    event.start = start
    event.end = end
    event.name = title
    event.save()
    data = {}
    return JsonResponse(data)
 
def remove(request):
    id = request.GET.get("id", None)
    event = Events.objects.get(id=id)
    event.delete()
    data = {}
    return JsonResponse(data)


class DeleteAllEventsView(View):
    def get(self, request):
        Events.objects.all().delete()
        return JsonResponse({'status': 'Tous les événements ont été supprimés avec succès'})


#upload du fichier ics si l'utilsateur est un prof
class UploadICSView(View):
    def get(self, request):
        return render(request, 'Absences/upload_ics.html')

    def post(self, request):
        ics_file = request.FILES['ics_file']
        cal = Calendar.from_ical(ics_file.read())

        for component in cal.walk():
            if component.name == "VEVENT":
                name = component.get('SUMMARY')
                start = component.get('DTSTART').dt
                end = component.get('DTEND').dt

                # Convertir les dates de début et de fin en objets datetime
                start_datetime = start if isinstance(start, datetime.datetime) else datetime.datetime.combine(start, datetime.time.min)
                end_datetime = end if isinstance(end, datetime.datetime) else datetime.datetime.combine(end, datetime.time.min)
                start_datetime += datetime.timedelta(hours=2) # Ajouter 2 heures pour corriger le décalage horaire
                end_datetime += datetime.timedelta(hours=2) 
                # Créer et enregistrer une instance d'Events
                event = Events(name=name, start=start_datetime, end=end_datetime)
                event.save()

        # Rediriger vers la vue index après le traitement du fichier
        return redirect('index')



class UploadICalendarLinkView(View):
    def post(self, request):
        ical_url = request.POST.get('ical_url')
        if not ical_url:
            return JsonResponse({'error': 'Pas d\'URL fournie'}, status=400)

        response = requests.get(ical_url)
        if response.status_code != 200:
            return JsonResponse({'error': 'Échec de l\'extraction du fichier iCalendar'}, status=400)

        cal = Calendar.from_ical(response.content)
        for component in cal.walk():
            if component.name == "VEVENT":
                name = component.get('SUMMARY')
                start = component.get('DTSTART').dt
                end = component.get('DTEND').dt

                # Convertir les dates de début et de fin en objets datetime
                start_datetime = start if isinstance(start, datetime.datetime) else datetime.datetime.combine(start, datetime.time.min)
                end_datetime = end if isinstance(end, datetime.datetime) else datetime.datetime.combine(end, datetime.time.min)
                start_datetime += datetime.timedelta(hours=2)
                end_datetime += datetime.timedelta(hours=2)
                # Créer et enregistrer une instance d'Events
                event = Events(name=name, start=start_datetime, end=end_datetime)
                event.save()

        return JsonResponse({'status': 'calendrier importé avec succès'})


#affichage des absences si l'utilisateur est un prof
class AbsenceView(View):
    def get(self, request, event_id, enseignant_id):
        event = get_object_or_404(Events, id=event_id)
        eleves = Eleve.objects.all()
        absences = Absence.objects.filter(event=event, enseignant_id=enseignant_id)
        absent_students = [absence.eleve for absence in absences]
        context = {
            'event': event,
            'eleves': eleves,
            'absent_students': absent_students,
            'enseignant_id': enseignant_id,
        }
        return render(request, 'Absences/absence.html', context)

    def post(self, request, event_id, enseignant_id):
        event = get_object_or_404(Events, id=event_id)
        absent_students = request.POST.getlist('absent_students')
        Absence.objects.filter(event=event, enseignant_id=enseignant_id).delete()
        for eleve_id in absent_students:
            eleve = get_object_or_404(Eleve, id=eleve_id)
            Absence.objects.create(eleve=eleve, event=event, enseignant_id=enseignant_id)
        return redirect('index')


#affichage des absences si l'utilisateur est un élève
class AbsenceView_eleve(View):
    template_name = 'Absences/absences_eleve.html'

    def get(self, request, eleve_id, *args, **kwargs):
        eleve = Eleve.objects.get(id=eleve_id)
        absences = Absence.objects.filter(eleve=eleve)
        
        # Retrieve all events and mark those where the student is absent
        all_events = Events.objects.all()
        events_data = []
        for event in all_events:
            is_absent = absences.filter(event=event).exists()
            events_data.append({
                'title': event.name,
                'start': event.start.isoformat(),
                'end': event.end.isoformat(),
                'absent': is_absent
            })

        context = {
            'eleve': eleve,
            'absences_json': json.dumps(events_data, cls=DjangoJSONEncoder)
        }
        return render(request, self.template_name, context)