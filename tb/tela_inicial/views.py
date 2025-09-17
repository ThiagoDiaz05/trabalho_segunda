from django.shortcuts import render

def home(request):
    return render(request, 'tela_inicial/index.html')
