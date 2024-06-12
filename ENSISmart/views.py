from django.shortcuts import get_object_or_404, redirect, render
from django.core.mail import send_mail
from django.http import JsonResponse

from Notes.views import note_main_view, matiere_liste
from .forms import PasswordResetForm, SignupForm, LoginForm
from django.utils.crypto import get_random_string
from django.utils import timezone
from datetime import timedelta
from User.models import Eleve, Enseignant, Administrateur
from .models import TemporaryLink
from django.contrib.auth.models import *
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

def signup_view(request):
    if request.user.is_active:
        print(request.user.is_active)
        return dashboard_view(request)
    if request.method == 'POST':
        if 'email_login' in request.POST:
            form_login = LoginForm(request.POST)
            form = SignupForm()  # Initialize an empty signup form
            if form_login.is_valid():
                email = form_login.cleaned_data.get('email_login')
                
                user = None
                try:
                    user = Eleve.objects.get(email=email)  # Try to get an Eleve with the given email
                except Eleve.DoesNotExist:
                    pass  # If no Eleve is found, do nothing

                if user is None:  # If no Eleve was found, try to find an Enseignant
                    try:
                        user = Enseignant.objects.get(email=email)  # Try to get an Enseignant with the given email
                    except Enseignant.DoesNotExist:
                        pass
                    
                print(user," ezfefzef")

                if user is None:
                    return redirect('login')  # Redirect to login page if is_first_co is True

                password = form_login.cleaned_data.get('password')
                user = authenticate(request, email=email, password=password)
                if user is not None and user.password is not None:
                    user.is_active = True
                    user.save()
                    login(request, user, backend='User.backends.CustomBackend')
                    request.session.set_expiry(1209600)
                    if not form_login.cleaned_data.get('remember_me'):
                        request.session.set_expiry(0)
                    return dashboard_view(request)
                else:
                    form_login.add_error(None, 'Invalid email or password')
        else:
            form = SignupForm(request.POST)
            form_login = LoginForm()  # Initialize an empty login form
            if form.is_valid():
                email = form.cleaned_data.get('email')
                token = get_random_string(30)
                expires_at = timezone.now() + timedelta(hours=24)
                TemporaryLink.objects.create(token=token, expires_at=expires_at, email=email)

                link = request.build_absolute_uri(f'/reset-password/{token}/')
                send_mail(
                    'Password Reset Link',
                    f'Click here to reset your password: {link}',
                    settings.DEFAULT_FROM_EMAIL,
                    [email],
                    fail_silently=False,
                )
                return JsonResponse({'success': True, 'email': email})
            else:
                error_messages = [error.as_text() for error in form.errors.values()]
                return JsonResponse({'success': False, 'errors': error_messages})
    else:
        form = SignupForm()
        form_login = LoginForm()

    return render(request, 'frontend/general_index/general.html', {'form': form, 'form_login': form_login})

def error_view(request):
    if request.method == 'POST':
        return redirect('login')
    return render(request, 'frontend/general_index/error_page.html')

def reset_password_view(request, token):
    try:
        temp_link = TemporaryLink.objects.get(token=token)
        if temp_link.expires_at < timezone.now():
            return render(request, 'frontend/reset_password/expired.html')
    except TemporaryLink.DoesNotExist:
        return render(request, 'frontend/reset_password/invalid.html')
    
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            new_password = form.cleaned_data['new_password']
            hashed_password = make_password(new_password)

            email = temp_link.email

            try:
                user = Eleve.objects.get(email=email)
            except Eleve.DoesNotExist:
                try:
                    user = Enseignant.objects.get(email=email)
                except Enseignant.DoesNotExist:
                    return render(request, 'frontend/general_index/error_page.html')

            user.password = hashed_password
            user.is_active = True
            user.is_first_co = False
            user.save()
            
            temp_link.delete()
            return redirect('login')
    else:
        form = PasswordResetForm()

    return render(request, 'frontend/general_index/change_password.html', {'form': form})

def dashboard_view(request):
    if isinstance(request.user, Eleve):
        return note_main_view(request)
    elif isinstance(request.user, Enseignant):
        print("enseignant")
        return matiere_liste(request)
    elif (request.user, Administrateur):
        pass

def logout_view(request):
    if request.user.is_authenticated:
        request.user.is_active = False
        request.user.save()
    logout(request)
    return redirect("login")