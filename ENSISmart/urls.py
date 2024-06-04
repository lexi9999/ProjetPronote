from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('notes/', include('User.urls')),  # Inclure les URLs de l'application Smart
]
