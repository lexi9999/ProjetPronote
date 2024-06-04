
from django import forms
from django.core.exceptions import ValidationError
from .models import Eleve, Enseignant

def validate_uha_email(value):
    value_t = value.split(".")
    if len(value_t) != 2:
        raise ValidationError('L\'adresse e-mail doit se terminer par @uha.fr')
    for e in "@.,;:!":
        if e in value*[0]:
            raise ValidationError('L\'adresse e-mail doit se terminer par @uha.fr')
        if e in value[1]:
            raise ValidationError('L\'adresse e-mail doit se terminer par @uha.fr')

class LoginForm(forms.Form):
    email = forms.TextInput(
        label='Adresse e-mail',
        max_length=100,
        validators=[validate_uha_email],
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Adresse e-mail'})
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not Eleve.objects.filter(email=email).exists():
            if not Enseignant.objects.filter(email=email).exists():
                raise ValidationError('Adresse e-mail non reconnue (ni étudiant ni enseignant)')
        return email
        