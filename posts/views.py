from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import PermissionDenied
from .models import Post, Comment, Category

# View para registro de usuários
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Salva o usuário no banco de dados
            return redirect('login')  # Redireciona para a página de login
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

# View para criação de comentários
class CommentCreateView(LoginRequiredMixin, View):
    def post(self, request, post_id):
        # Garante que o post exista ou retorna 404
        post = get_object_or_404(Post, id=post_id)
        text = request.POST.get('text')
        # Cria o comentário associado ao post
        Comment.objects.create(post=post, author=request.user, text=text)
        return redirect('post_detail', pk=post_id)

# View para listar categorias (página inicial)
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'posts/category_list.html', {'categories': categories})

# View para detalhes de uma categoria
def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    posts = category.posts.all()
    return render(request, 'posts/posts_list.html', {'posts': posts, 'category': category})

# View para listar posts
class PostListView(ListView):
    model = Post
    template_name = 'posts/posts_list.html'
    context_object_name = 'posts'
    ordering = ['-created_at']  # Ordena por data de criação, mais recente primeiro

# View para detalhes de um post
class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        user = self.request.user

        # Adicionar permissões de post no contexto
        context['can_edit_post'] = user.is_authenticated and (user == post.author or user.has_perm('posts.can_manage_all_posts'))
        context['can_delete_post'] = user.is_authenticated and (user == post.author or user.has_perm('posts.can_manage_all_posts'))

        # Adicionar categorias do post no contexto
        context['categories'] = post.categories.all()

        # Adicionar comentários ordenados no contexto
        context['comments'] = post.comments.all().order_by('-created_at')
        return context

# View para criação de posts
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'posts/post_form.html'
    fields = ['title', 'content', 'categories']  # Inclui categorias no formulário
    success_url = reverse_lazy('category_list')

    def form_valid(self, form):
        form.instance.author = self.request.user  # Associa o post ao usuário logado
        return super().form_valid(form)

# View para atualização de posts
class PostUpdateView(UpdateView):
    model = Post
    template_name = 'posts/post_form.html'
    fields = ['title', 'content', 'categories']  # Permite editar categorias

    def dispatch(self, request, *args, **kwargs):
        post = self.get_object()
        if not (request.user == post.author or request.user.has_perm('posts.can_manage_all_posts')):
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

# View para exclusão de posts
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts/post_confirm_delete.html'
    success_url = reverse_lazy('category_list')

    def dispatch(self, request, *args, **kwargs):
        post = self.get_object()
        if not (request.user == post.author or request.user.has_perm('posts.can_manage_all_posts')):
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
