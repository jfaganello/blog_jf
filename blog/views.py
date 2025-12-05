from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404
from .models import Post, Comment, Category
from .forms import PostForm, CommentForm, CategoryForm

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-criado_em']

class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = self.object.comments.order_by("-data_postagem")
        return context

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post_list')

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    
    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.pk})

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('post_list')

class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "blog/comment_form.html"

    def form_valid(self, form):
        post = get_object_or_404(Post, id=self.kwargs["post_id"])
        form.instance.post = post
        form.instance.autor = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("post_detail", args=[self.kwargs["post_id"]])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_id"] = self.kwargs["post_id"] 
        return context

class CategoryListView(ListView):
    model = Category
    template_name = "blog/category_list.html"
    context_object_name = "categorias"

class CategoryDetailView(ListView):
    model = Post
    template_name = "blog/post_list.html"  
    context_object_name = "posts"

    def get_queryset(self):
        # pega a categoria, ou retorna 404
        self.category = get_object_or_404(Category, pk=self.kwargs["pk"])
        return self.category.posts.all().order_by("-criado_em")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = self.category
        return context
    
class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = "blog/category_form.html"