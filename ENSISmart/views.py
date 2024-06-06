from django.shortcuts import get_object_or_404, redirect, render
from django.core.mail import send_mail
from django.http import JsonResponse
from .forms import PasswordResetForm, SignupForm
from django.utils.crypto import get_random_string
from django.utils import timezone
from datetime import timedelta
from .models import TemporaryLink
from django.contrib.auth.models import *
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.conf import settings


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            token = get_random_string(30)
            expires_at = timezone.now() + timedelta(hours=24)  # Link valid for 1 hour
            TemporaryLink.objects.create(token=token, expires_at=expires_at)    
            user = User.objects.filter(email=email).first()
            
            link = request.build_absolute_uri(f'/reset-password/{token}/')
            
            # Send an email to the user
            send_mail(
                'Succès',
                f'Lien pour créer un mot de passe : {link}',
                'settings.EMAIL_HOST_USER',  # Sender's email address
                [email],  # Recipient's email address
                fail_silently=False,
            )
            
            return JsonResponse({'success': True, 'email': email})
        else:
            error_messages = [error.as_text() for error in form.errors.values()]
            return JsonResponse({'success': False, 'errors': error_messages})
    else:
        form = SignupForm()

    return render(request, 'frontend/general_index/general.html', {'form': form})

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
            # You should add your logic to reset the user's password here.
            # Example:
            # user = temp_link.user
            # user.set_password(new_password)
            # user.save()
            
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


