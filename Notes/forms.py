from django import forms
from .models import Matiere

class MatiereForm(forms.ModelForm):
    class Meta:
        model = Matiere
        fields = ['name', 'coefficient', 'name_enseignant', 'ue']