
from django import forms
from django.core.exceptions import ValidationError
from .models import Eleve, Enseignant
import re

def validate_uha_email(value):
    value_t = value.split(".")
    if len(value_t) != 2:
        raise ValidationError("mail error")
    else:
        for c in "&@.,;:!§/":
            for val in value_t:
                if c in val:
                    raise ValidationError("mail error")
                
def validate_email(value):
    pattern = r'^[a-zA-Z]+\.[a-zA-Z]+@uha\.fr$'
    if not re.match(pattern, value):
        raise ValidationError('Email must be in the format prenom.nom@uha.fr')

class PasswordResetForm(forms.Form):
    new_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'type': 'password',
            'id': 'psw',
            'placeholder': 'Mot de passe',
            'pattern': '(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}',
            'title': 'Must contain at least one number and one uppercase and lowercase letter, and at least 8 or more characters'
        }),
        label='New Password'
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'type': 'password',
            'id': 'psw-conf',
            'placeholder': 'Confirmation'
        }),
        label='Confirm Password'
    )

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get('new_password')
        confirm_password = cleaned_data.get('confirm_password')

        if new_password and confirm_password and new_password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        
        return cleaned_data
    
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
    
class LoginForm(forms.Form):
    remember_me = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'tgl tgl-flip', 'id': 'cb5'})
    )
    email = forms.CharField(
        label='Adresse e-mail',
        max_length=100,
        validators=[validate_email],  # You can replace this with validate_uha_email if you have a custom validator.
        widget=forms.TextInput(attrs={
            'type': 'text',
            'placeholder': 'Mail UHA',
            'required': 'required',
            'class': 'form-control mail_input signup'
        })
    )
    
    password = forms.CharField(
        label='Mot de passe',
        widget=forms.PasswordInput(attrs={'class': 'password', 'placeholder': 'Mot de passe'})
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
    
    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get('new_password')
        confirm_password = cleaned_data.get('confirm_password')

        if new_password and confirm_password and new_password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")