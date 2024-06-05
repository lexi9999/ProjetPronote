from django.urls import path
from . import views

urlpatterns = [
    path('mesMatieres', views.index, name='mesMatieres'),
    path('ajouter', views.create_matiere, name='create_matiere'),
    path('delete/<int:matiere_id>/', views.delete_matiere, name='delete_matiere'),
]