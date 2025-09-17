from django.db import models
from django.contrib.auth.models import User

class Grupo(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    criador = models.ForeignKey(User, on_delete=models.CASCADE)
    participantes = models.ManyToManyField(User, related_name='grupos')
    imagem = models.ImageField(upload_to='grupo_pics/', blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Postagem(models.Model):
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, related_name='postagens')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    imagem = models.ImageField(upload_to='postagens/', blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.autor.username} - {self.grupo.nome}'
