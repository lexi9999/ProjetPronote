from django.db import models
from django.utils.translation import gettext as _
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from icalendar import Calendar
from django.http import JsonResponse
import datetime
from ENSISmart.models import Events
import requests

def index(request):  
    all_events = Events.objects.all()
    context = {
        "events":all_events,
    }
    return render(request,'calendar.html',context) 

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
        return JsonResponse({'status': 'All events deleted'})

def display_events(request):
    events = Events.objects.order_by('start')
    context = {'events': events}
    return render(request, 'display_events.html', context)

class UploadICSView(View):
    def get(self, request):
        return render(request, 'upload_ics.html')

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

                # Créer et enregistrer une instance d'Events
                event = Events(name=name, start=start_datetime, end=end_datetime)
                event.save()

        # Rediriger vers la vue index après le traitement du fichier
        return redirect('index')


class UploadICalendarLinkView(View):
    def post(self, request):
        ical_url = request.POST.get('ical_url')
        if not ical_url:
            return JsonResponse({'error': 'No URL provided'}, status=400)

        response = requests.get(ical_url)
        if response.status_code != 200:
            return JsonResponse({'error': 'Failed to fetch the iCalendar file'}, status=400)

        cal = Calendar.from_ical(response.content)
        for component in cal.walk():
            if component.name == "VEVENT":
                name = component.get('SUMMARY')
                start = component.get('DTSTART').dt
                end = component.get('DTEND').dt

                # Convertir les dates de début et de fin en objets datetime
                start_datetime = start if isinstance(start, datetime.datetime) else datetime.datetime.combine(start, datetime.time.min)
                end_datetime = end if isinstance(end, datetime.datetime) else datetime.datetime.combine(end, datetime.time.min)

                # Créer et enregistrer une instance d'Events
                event = Events(name=name, start=start_datetime, end=end_datetime)
                event.save()

        return JsonResponse({'status': 'iCalendar events uploaded'})
