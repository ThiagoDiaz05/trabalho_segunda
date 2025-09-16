# register/views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Conta criada com sucesso para {username}! Você já pode fazer login.')
            return redirect('login') # Redireciona para a página de login
    else:
        form = RegisterForm()

    # A única mudança real na lógica está aqui, no caminho do template:
    return render(request, 'register/register.html', {'form': form})