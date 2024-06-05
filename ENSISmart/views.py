from django.shortcuts import render
from django.core.mail import send_mail
from django.http import JsonResponse
from .forms import SignupForm
from django.urls import reverse

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')

            # Send an email to the user
            send_mail(
                'Succès',
                'Vous êtes connecté avec succès.',
                'from@example.com',  # Sender's email address
                [email],  # Recipient's email address
                fail_silently=False,
            )

            return JsonResponse({'success': True, 'email': email})
        else:
            error_messages = [error.as_text() for error in form.errors.values()]
            return JsonResponse({'success': False, 'errors': error_messages})
    else:
        form = SignupForm()

    return render(request, 'frontend/general_index/general.html', {
        'form': form,
        'signup_url': reverse('login'),  # Assuming 'login' is the name of your URL pattern
    })

def success_view(request):
    return render(request, 'success.html')
