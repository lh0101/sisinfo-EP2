from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post

# ListView: Exibe a lista de posts
class PostListView(ListView):
    model = Post
    template_name = 'posts/posts_list.html'
    context_object_name = 'posts'
    ordering = ['-post_date']

# DetailView: Exibe os detalhes de um post
class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'

# CreateView: Cria um novo post
class PostCreateView(CreateView):
    model = Post
    template_name = 'posts/post_form.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('posts_list')

# UpdateView: Edita um post existente
class PostUpdateView(UpdateView):
    model = Post
    template_name = 'posts/post_form.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('posts_list')

# DeleteView: Deleta um post (com página de confirmação)
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts/post_confirm_delete.html'
    success_url = reverse_lazy('posts_list')
