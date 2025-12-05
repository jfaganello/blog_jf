from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["titulo", "titulo_livro", "autor", "conteudo"]
        labels = {
            "titulo": "Título",
            "titulo_livro": "Título do livro",
            "autor": "Autor",
            "conteudo": "Conteúdo",
        }