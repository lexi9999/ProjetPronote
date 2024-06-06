# urls.py
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.note_liste, name='note_liste'),
    path('ajouter/', views.ajouter_note, name='ajouter_note'),
    path('modifier/<int:pk>/', views.modifier_note, name='modifier_note'),
    path('ajax/update_note/<int:pk>/', views.update_note_ajax, name='update_note_ajax'),  # URL AJAX
    path('accounts/', include('django.contrib.auth.urls')),
]
