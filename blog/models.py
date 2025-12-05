from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth import get_user_model

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    titulo_livro = models.CharField("Título do livro", max_length=200, blank=True, null=True)
    autor = models.CharField("Autor", max_length=200, blank=True, null=True)
    conteudo = models.TextField()
    criado_em = models.DateTimeField(default=timezone.now)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse("post_detail", args=[self.id])
    
User = get_user_model()

class Comment(models.Model):
    autor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    post = models.ForeignKey(
        'Post',
        on_delete=models.CASCADE,
        related_name='comments'
    )
    texto = models.TextField()
    data_postagem = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Comentário de {self.autor} em {self.data_postagem:%d/%m/%Y}'

