from django.contrib import admin
from .models import Post, Comment, Category

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')  # Alterado 'post_date' para 'created_at'
    ordering = ('-created_at',)  # Alterado 'post_date' para 'created_at'
    search_fields = ('title', 'author__username')  # Correção no lookup do campo author

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created_at')  # Mantém como antes
    ordering = ('-created_at',)  # Mantém como antes
    search_fields = ('post__title', 'author__username')  # Correção no lookup do campo author

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')  # Exibição básica para categorias
