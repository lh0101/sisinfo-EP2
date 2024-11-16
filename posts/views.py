from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = 'posts/posts_list.html'
    context_object_name = 'posts'
    ordering = ['-post_date']  # Ordena por data de postagem, mais recente primeiro

class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'

class PostCreateView(CreateView):
    model = Post
    template_name = 'posts/post_form.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('posts_list')  # Redireciona para a lista após criar

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'posts/post_form.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('posts_list')  # Redireciona para a lista após editar

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts/post_confirm_delete.html'
    success_url = reverse_lazy('posts_list')  # Redireciona para a lista após excluir
