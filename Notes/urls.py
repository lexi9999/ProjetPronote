from django.urls import path, include
from . import views

urlpatterns = [
    path('matieres/', views.matiere_liste, name='matiere_liste'),
    path('notes/<str:matiere>/', views.note_liste, name='note_liste'),
    path('ajouter/', views.ajouter_note, name='ajouter_note'),
    path('modifier/<int:pk>/', views.modifier_note, name='modifier_note'),
    path('ajax/update_note/<int:pk>/', views.update_note, name='update_note'),  # URL AJAX
    path('accounts/', include('django.contrib.auth.urls')),
]
