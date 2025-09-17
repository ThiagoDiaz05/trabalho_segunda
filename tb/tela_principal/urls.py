from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('grupos/criar/', views.criar_grupo, name='criar_grupo'),
    path('grupos/pesquisar/', views.pesquisar_grupos, name='pesquisar_grupos'),
    path('grupos/<int:grupo_id>/', views.grupo_detail, name='grupo_detail'),
    path('grupos/<int:grupo_id>/entrar/', views.entrar_grupo, name='entrar_grupo'),
    path('grupos/<int:grupo_id>/sair/', views.sair_grupo, name='sair_grupo'),
]
