from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('dashboard')  # ou para onde você quiser
        else:
            messages.error(request, 'Usuário ou senha inválidos.')

    return render(request, 'login/login.html')


def logout_view(request):
    auth_logout(request)
    return redirect('login')  # redireciona de volta pro login
