
from django import forms
from django.core.exceptions import ValidationError
from .models import Eleve, Enseignant

def validate_uha_email(value):
    value_t = value.split(".")
    if len(value_t) != 2:
        raise ValidationError("mail error")
    else:
        for c in "&@.,;:!§/":
            for val in value_t:
                if c in val:
                    raise ValidationError("mail error")

class SignupForm(forms.Form):
    email = forms.CharField(
        label='Adresse e-mail',
        max_length=100,
        validators=[validate_uha_email],
        widget=forms.TextInput(attrs={'class': 'form-control mail_input signup', 'placeholder': 'prénom.nom'})
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Append @uha.fr if not already present
        if not email.endswith('@uha.fr'):
            email += '@uha.fr'
        # Validate the email format and existence
        if not Eleve.objects.filter(email=email).exists() and not Enseignant.objects.filter(email=email).exists():
            raise ValidationError('Adresse e-mail non reconnue (ni étudiant ni enseignant)')
        return email