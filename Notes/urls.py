from django.urls import path, include
from . import views
from .views import note_main_edit, note_main_view
from User import views
from Notes import views

urlpatterns = [
    path('', note_main_view, name='notes'),
    path('edit/', note_main_edit, name='notes_edit'),
    path('matieres/', views.matiere_liste, name='matiere_liste'),
    path('notes/<int:matiere>/', views.note_liste, name='note_liste'),
    path('ajouter/', views.ajouter_note, name='ajouter_note'),
    path('modifier/<int:pk>/', views.modifier_note, name='modifier_note'),
    path('ajax/update_note/<int:pk>/', views.update_note_ajax, name='update_note_ajax'),  # URL AJAX
    #path('accounts/', include('django.contrib.auth.urls')),
    path('matiere/<int:matiere_id>/', views.matiere_notes, name='matiere_notes'),
    path('import_notes/', views.import_notes, name='import_notes'),
]
