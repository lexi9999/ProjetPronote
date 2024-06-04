from django.contrib import admin

from User.models import *

# Register your models here.
admin.site.register(Utilisateur)
admin.site.register(Eleve)
admin.site.register(Enseignant)
admin.site.register(Note)