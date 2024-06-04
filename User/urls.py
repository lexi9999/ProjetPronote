from django.urls import path
from . import views

urlpatterns = [
    path('', views.note_liste, name='note_liste'),  # Liste des notes
    path('ajouter/', views.ajouter_note, name='ajouter_note'),  # Ajouter une note
    path('modifier/<int:pk>/', views.modifier_note, name='modifier_note'),  # Modifier une note
]
