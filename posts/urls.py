from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    CommentCreateView,
    category_list,
    category_detail,
)

urlpatterns = [
    path('', category_list, name='category_list'),  # Página inicial mostrando as categorias
    path('categories/<int:pk>/', category_detail, name='category_detail'),  # Posts de uma categoria específica
    path('posts/', PostListView.as_view(), name='posts_list'),  # Lista de posts
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),  # Detalhe do post
    path('posts/create/', PostCreateView.as_view(), name='posts_create'),  # Criar novo post
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),  # Editar post
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),  # Deletar post
    path('posts/<int:post_id>/comment/', CommentCreateView.as_view(), name='add_comment'),  # Adicionar comentário
]
