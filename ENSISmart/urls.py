from django.urls import path
from .views import login_view, success_view

urlpatterns = [
    path('', login_view, name='login'),
    path('success/', success_view, name='success'),
]

