from django.shortcuts import render, redirect
from .forms import LoginForm

def login_view(request):
    message = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # Handle successful login logic here
            message = 'Connexion réussie'
            return redirect('success')  # Redirect to a success page or handle login logic
        else:
            # Convertir chaque objet ErrorList en chaîne de caractères
            error_messages = [error.as_text() for error in form.errors.values()]
            message = 'Erreur : ' + ', '.join(error_messages)
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form, 'message': message})

def success_view(request):
    return render(request, 'success.html')
