from django.urls import path
from .views import note_main_view
from User import views

urlpatterns = [
    path('', note_main_view, name='notes')
]