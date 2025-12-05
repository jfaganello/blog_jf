from django.shortcuts import render
from .models import Post
from django.shortcuts import redirect

def post_list(request):
    posts = Post.objects.all().order_by('-data_postagem')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_create(request):
    if request.method == "POST":
        titulo = request.POST.get("titulo")
        conteudo = request.POST.get("conteudo")

        Post.objects.create(
            titulo=titulo,
            conteudo=conteudo
        )

        return redirect('post_list')

    return render(request, 'blog/post_form.html')

def post_update(request, pk):
    post = Post.objects.get(pk=pk)

    if request.method == "POST":
        post.titulo = request.POST.get("titulo")
        post.conteudo = request.POST.get("conteudo")
        post.save()
        return redirect('post_detail', pk=post.pk)

    return render(request, 'blog/post_form.html', {'post': post})

def post_delete(request, pk):
    post = Post.objects.get(pk=pk)

    if request.method == "POST":
        post.delete()
        return redirect('post_list')

    return render(request, 'blog/post_delete.html', {'post': post})
