from django.urls import path
from . import views

urlpatterns = [
    path('', views.note_liste, name='note_liste'),  # L'URL de base User/ redirige vers note_liste
    path('note_liste/', views.note_liste, name='note_liste'),
    path('modifier_note/<int:note_id>/', views.modifier_note, name='modifier_note'),
    path('delete_note/<int:note_id>/', views.delete_note, name='delete_note'),
]

