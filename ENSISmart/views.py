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
            message = 'Erreur : ' + ', '.join(form.errors.values())
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form, 'message': message})

def success_view(request):
    return render(request, 'success.html')
