from django.urls import path
from .views import signup_view, success_view, reset_password_view

urlpatterns = [
    path('', signup_view, name='login'),
    path('success/', success_view, name='success'), 
    path('reset-password/<str:token>/', reset_password_view, name='reset_password')
]


