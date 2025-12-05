from django.urls import path
from .views import (
    PostListView, PostDetailView, PostCreateView,
    PostUpdateView, PostDeleteView, CommentCreateView
)

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('novo/', PostCreateView.as_view(), name='post_create'),
    path('<int:pk>/editar/', PostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/deletar/', PostDeleteView.as_view(), name='post_delete'),
    path('post/<int:post_id>/comment/new/', CommentCreateView.as_view(), name="comment_create"),
]

