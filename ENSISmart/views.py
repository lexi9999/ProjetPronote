from django.shortcuts import get_object_or_404, redirect, render
from django.core.mail import send_mail
from django.http import JsonResponse
from .forms import PasswordResetForm, SignupForm, LoginForm
from django.utils.crypto import get_random_string
from django.utils import timezone
from datetime import timedelta
from User.models import Eleve, Enseignant
from .models import TemporaryLink
from django.contrib.auth.models import *
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password
from django.core.mail import send_mail
from django.conf import settings


def signup_view(request):
    if request.method == 'POST':
        # Determine which form is being submitted
        if 'email_login' in request.POST:
            form_login = LoginForm(request.POST)
            form = SignupForm()  # Initialize an empty signup form
            if form_login.is_valid():
                email = form_login.cleaned_data.get('email_login')
                password = form_login.cleaned_data.get('password')

                user = None
                try:
                    user = Eleve.objects.get(email=email)
                except Eleve.DoesNotExist:
                    try:
                        user = Enseignant.objects.get(email=email)
                    except Enseignant.DoesNotExist:
                        user = None

                if user and check_password(password, user.password):
                    # Authenticate and login the user
                    login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                    if form_login.cleaned_data.get('remember_me'):
                        request.session.set_expiry(1209600)  # 2 weeks
                    else:
                        request.session.set_expiry(0)
                    return redirect('success')  # Redirect to the desired success page
                else:
                    form_login.add_error(None, 'Invalid email or password')
        else:
            form = SignupForm(request.POST)
            form_login = LoginForm()  # Initialize an empty login form
            if form.is_valid():
                email = form.cleaned_data.get('email')
                token = get_random_string(30)
                expires_at = timezone.now() + timedelta(hours=24)  # Link valid for 1 hour
                TemporaryLink.objects.create(token=token, expires_at=expires_at, email=email) 
                
                link = request.build_absolute_uri(f'/reset-password/{token}/')
                print(link)
                
                # Send an email to the user
                send_mail(
                    'Succès',
                    f'Lien pour créer un mot de passe : {link}',
                    '761ae1002@smtp-brevo.com',  # Sender's email address
                    [email],  # Recipient's email address
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
                    return render(request, 'frontend/reset_password/invalid.html')

            user.password = hashed_password
            print(user.password,"Azerty123456")
            user.is_first_co = False
            user.save()
            
            temp_link.delete()  # Remove the temporary link after successful password reset
            return redirect('success')  # Redirect to a success page or login page
    else:
        form = PasswordResetForm()

    return render(request, 'frontend/general_index/change_password.html', {'form': form})


def reset_password(request, token):
    temp_link = get_object_or_404(TemporaryLink, token=token)

    if not temp_link.is_valid():
        return render(request, 'expired.html')

    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            new_password = form.cleaned_data.get('new_password')
            user = User.objects.get(email=temp_link.email)
            user.password = make_password(new_password)
            user.save()
            temp_link.delete()
            return render(request, 'success.html')
    else:
        form = PasswordResetForm()

    return render(request, 'frontend/general_index/change_password.html', {'form': form})

def success_view(request):
    return render(request, 'success.html')


