
from django import forms
from django.core.exceptions import ValidationError
from .models import Eleve

def validate_uha_email(value):
    if not value.endswith('@uha.fr'):
        raise ValidationError('L\'adresse e-mail doit se terminer par @uha.fr')

class LoginForm(forms.Form):
    email = forms.EmailField(
        label='Adresse e-mail',
        max_length=100,
        validators=[validate_uha_email],
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Adresse e-mail'})
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not Eleve.objects.filter(email=email).exists():
            raise ValidationError('Adresse e-mail non reconnue')
        return email