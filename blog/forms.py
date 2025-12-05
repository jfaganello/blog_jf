from django import forms
from .models import Post, Comment, Category

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

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["texto"]
        widgets = {
            "texto": forms.Textarea(attrs={"rows": 4})
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["nome", "descricao"]