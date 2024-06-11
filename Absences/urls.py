# urls.py
from django.contrib import admin
from django.urls import include, path
from Absences import views
from Absences.views import UploadICSView, UploadICalendarLinkView, DeleteAllEventsView, AbsenceView, AbsenceView_eleve

urlpatterns = [
    
    path('calendar/<int:enseignant_id>/', views.index, name='index'),
    path('all_events/', views.all_events, name='all_events'), 
    path('add_event/', views.add_event, name='add_event'), 
    path('update/', views.update, name='update'),
    path('remove/', views.remove, name='remove'),
    path('upload_ics/', UploadICSView.as_view(), name='upload_ics'),
    path('upload_icalendar_link/', UploadICalendarLinkView.as_view(), name='upload_icalendar_link'),
    path('delete_all_events/', DeleteAllEventsView.as_view(), name='delete_all_events'),
    path('absence/<int:event_id>/<int:enseignant_id>/', AbsenceView.as_view(), name='absence'),
    path('absences_eleve/<int:eleve_id>/', AbsenceView_eleve.as_view(), name='absences_eleve'),
]

