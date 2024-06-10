from django.urls import path
from .views import signup_view, dashboard_view, reset_password_view, error_view

urlpatterns = [
    path('', signup_view, name='login'),
    path('success/', dashboard_view, name='success'), 
    path('reset-password/<str:token>/', reset_password_view, name='reset_password_view'),
    path('error/', error_view, name='error')
]


