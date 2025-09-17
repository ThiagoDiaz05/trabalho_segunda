from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Grupo, Postagem
from .forms import GrupoForm, PostagemForm
from django.db.models import Q

# Dashboard: lista de grupos do usuário
@login_required
def dashboard(request):
    grupos = request.user.grupos.all()
    return render(request, 'tela_principal/dashboard.html', {'grupos': grupos})

# Criar grupo
@login_required
def criar_grupo(request):
    if request.method == 'POST':
        form = GrupoForm(request.POST, request.FILES)
        if form.is_valid():
            grupo = form.save(commit=False)
            grupo.criador = request.user
            grupo.save()
            grupo.participantes.add(request.user)  # criador entra automaticamente
            return redirect('dashboard')
    else:
        form = GrupoForm()
    return render(request, 'tela_principal/criar_grupo.html', {'form': form})

# Pesquisar grupos por nome ou descrição
@login_required
def pesquisar_grupos(request):
    query = request.GET.get('q', '')
    resultados = Grupo.objects.filter(Q(nome__icontains=query) | Q(descricao__icontains=query))
    return render(request, 'tela_principal/pesquisar_grupos.html', {'grupos': resultados, 'query': query})

# Página de grupo + postagens
@login_required
def grupo_detail(request, grupo_id):
    grupo = get_object_or_404(Grupo, id=grupo_id)
    postagens = grupo.postagens.all().order_by('-data_criacao')

    if request.method == 'POST':
        form = PostagemForm(request.POST, request.FILES)
        if form.is_valid():
            postagem = form.save(commit=False)
            postagem.autor = request.user
            postagem.grupo = grupo
            postagem.save()
            return redirect('grupo_detail', grupo_id=grupo.id)
    else:
        form = PostagemForm()

    return render(request, 'tela_principal/grupo_detail.html', {
        'grupo': grupo,
        'postagens': postagens,
        'form': form
    })

# Entrar e sair do grupo
@login_required
def entrar_grupo(request, grupo_id):
    grupo = get_object_or_404(Grupo, id=grupo_id)
    grupo.participantes.add(request.user)
    return redirect('grupo_detail', grupo_id=grupo.id)

@login_required
def sair_grupo(request, grupo_id):
    grupo = get_object_or_404(Grupo, id=grupo_id)
    grupo.participantes.remove(request.user)
    return redirect('dashboard')
