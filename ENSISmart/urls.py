from django.urls import path
from .views import signup_view, success_view

urlpatterns = [
    path('', signup_view, name='login'),
    path('success/', success_view, name='success'),
]

