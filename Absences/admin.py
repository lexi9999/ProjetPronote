from django.contrib import admin

# Register your models here.
from .models import Events, Absence

admin.site.register(Events)
admin.site.register(Absence)