# urls.py
from django.contrib import admin
from django.urls import include, path
from Absences import views
from Absences.views import UploadICSView, UploadICalendarLinkView, DeleteAllEventsView, AbsenceView, AbsenceView_eleve

app_name = 'Absences'

urlpatterns = [
    
    path('calendar/<int:enseignant_id>/', views.index, name='index'),
    path('all_events/<int:enseignant_id>/', views.all_events, name='all_events'), 
    path('add_event/<int:enseignant_id>/', views.add_event, name='add_event'), 
    path('update/<int:enseignant_id>/', views.update, name='update'),
    path('remove/<int:enseignant_id>/', views.remove, name='remove'),
    path('upload_ics/<int:enseignant_id>/', UploadICSView.as_view(), name='upload_ics'),
    path('upload_icalendar_link/', UploadICalendarLinkView.as_view(), name='upload_icalendar_link'),
    path('delete_all_events/<int:enseignant_id>/', DeleteAllEventsView.as_view(), name='delete_all_events'),
    path('absence/<int:event_id>/<int:enseignant_id>/', AbsenceView.as_view(), name='absence'),
    path('absences_eleve/<int:eleve_id>/', AbsenceView_eleve.as_view(), name='absences_eleve'),
]

