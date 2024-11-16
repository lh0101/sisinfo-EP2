from django.shortcuts import render, get_object_or_404, redirect
from .models import Post

# Listar todos os posts
def posts_list(request):
    posts = Post.objects.all().order_by('-post_date')
    return render(request, 'posts/posts_list.html', {'posts': posts})

# Exibir os detalhes de um post
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'posts/post_detail.html', {'post': post})

# Criar um novo post
def post_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        Post.objects.create(title=title, content=content)
        return redirect('posts_list')
    return render(request, 'posts/post_form.html')

# Editar um post existente
def post_edit(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return redirect('post_detail', post_id=post.id)
    return render(request, 'posts/post_form.html', {'post': post})

# Deletar um post existente
def post_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('posts_list')
    return render(request, 'posts/post_confirm_delete.html', {'post': post})
