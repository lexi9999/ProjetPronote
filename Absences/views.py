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
    return render(request,'Absences/base.html',context)

def all_events(request, enseignant_id):
    all_events = Events.objects.filter(enseignant_id=enseignant_id)
    out = []
    for event in all_events:
        out.append({
            'title': event.name,
            'id': event.id,
            'start': event.start.strftime("%m/%d/%Y, %H:%M:%S") if event.start else None,
            'end': event.end.strftime("%m/%d/%Y, %H:%M:%S") if event.end else None,
        })
    return JsonResponse(out, safe=False)


def add_event(request, enseignant_id):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    event = Events(name=str(title), start=start, end=end, enseignant_id=enseignant_id)
    event.save()
    data = {}
    return JsonResponse(data)
 
def update(request, enseignant_id):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    id = request.GET.get("id", None)
    event = Events.objects.get(id=id, enseignant_id=enseignant_id)
    event.start = start
    event.end = end
    event.name = title
    event.save()
    data = {}
    return JsonResponse(data)
 
def remove(request, enseignant_id):
    id = request.GET.get("id", None)
    event = Events.objects.get(id=id, enseignant_id=enseignant_id)
    event.delete()
    data = {}
    return JsonResponse(data)


class DeleteAllEventsView(View):
    def get(self, request, enseignant_id):
        Events.objects.filter(enseignant_id=enseignant_id).delete()
        return JsonResponse({'status': 'Tous les événements ont été supprimés avec succès'})

#upload du fichier ics si l'utilsateur est un prof
class UploadICSView(View):
    def post(self, request, enseignant_id):  # enseignant_id is now a parameter of the post method
        ics_file = request.FILES['ics_file']

        if enseignant_id is None:
            return JsonResponse({'error': 'enseignant_id is required'}, status=400)

        cal = Calendar.from_ical(ics_file.read())

        for component in cal.walk():
            if component.name == "VEVENT":
                name = component.get('SUMMARY')
                start = component.get('DTSTART').dt
                end = component.get('DTEND').dt

                start_datetime = start if isinstance(start, datetime.datetime) else datetime.datetime.combine(start, datetime.time.min)
                end_datetime = end if isinstance(end, datetime.datetime) else datetime.datetime.combine(end, datetime.time.min)
                start_datetime += datetime.timedelta(hours=2)
                end_datetime += datetime.timedelta(hours=2)

                event = Events(name=name, start=start_datetime, end=end_datetime, enseignant_id=enseignant_id)
                event.save()

        return redirect('index', enseignant_id=enseignant_id)



class UploadICalendarLinkView(View):
    def post(self, request):
        ical_url = request.POST.get('ical_url')
        enseignant_id = request.POST.get('enseignant_id')
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

                start_datetime = start if isinstance(start, datetime.datetime) else datetime.datetime.combine(start, datetime.time.min)
                end_datetime = end if isinstance(end, datetime.datetime) else datetime.datetime.combine(end, datetime.time.min)
                start_datetime += datetime.timedelta(hours=2)
                end_datetime += datetime.timedelta(hours=2)

                event = Events(name=name, start=start_datetime, end=end_datetime, enseignant_id=enseignant_id)
                event.save()

        return JsonResponse({'status': 'calendrier importé avec succès'})

class AbsenceView(View):
    def get(self, request, event_id, enseignant_id):
        event = get_object_or_404(Events, id=event_id, enseignant_id=enseignant_id)
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
        event = get_object_or_404(Events, id=event_id, enseignant_id=enseignant_id)
        absent_students = request.POST.getlist('absent_students')
        Absence.objects.filter(event=event, enseignant_id=enseignant_id).delete()
        for eleve_id in absent_students:
            eleve = get_object_or_404(Eleve, id=eleve_id)
            Absence.objects.create(eleve=eleve, event=event, enseignant_id=enseignant_id)
        return redirect('index', enseignant_id=enseignant_id)


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