from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now available to Singin')
            return redirect('login')
        else:
            # Si el formulario no es válido, añade mensajes de error
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{error}')  # Puedes personalizar el mensaje si es necesario

    else:
        form = UserRegisterForm()

    return render(request, 'user/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'user/profile.html')