from django.shortcuts import render
from django.core.mail import send_mail
from django.http import JsonResponse
from .forms import SignupForm

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            
            # Send an email to the user
            send_mail(
                'Succès',
                'Lien pour créer un mot de passe : http://127.0.0.1:5500/ENSISmart/templates/frontend/general_index/change_password.html',
                '761ae1002@smtp-brevo.com',  # Sender's email address
                ['oussama.kouiri@uha.fr'],  # Recipient's email address
                fail_silently=False,
            )
            
            return JsonResponse({'success': True, 'email': email})
        else:
            error_messages = [error.as_text() for error in form.errors.values()]
            return JsonResponse({'success': False, 'errors': error_messages})
    else:
        form = SignupForm()

    return render(request, 'frontend/general_index/general.html', {'form': form})


def success_view(request):
    return render(request, 'success.html')
