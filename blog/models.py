from django.db import models
from django.utils import timezone
from django.urls import reverse

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    criado_em = models.DateTimeField(default=timezone.now)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse("post_detail", args=[self.id])