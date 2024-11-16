from django.shortcuts import render, get_object_or_404, redirect
from .models import Post

def posts_list(request):
    posts = Post.objects.all().order_by('-post_date')
    return render(request, 'posts/posts_list.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'posts/post_detail.html', {'post': post})

def post_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        Post.objects.create(title=title, content=content)
        return redirect('posts_list')
    return render(request, 'posts/post_form.html')

def post_edit(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.save()
        return redirect('post_detail', post_id=post.id)
    return render(request, 'posts/post_form.html', {'post': post})

def post_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('posts_list')
    return render(request, 'posts/post_confirm_delete.html', {'post': post})
