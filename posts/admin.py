from django.contrib import admin
from .models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'post_date')
    ordering = ('-post_date',)
    search_fields = ('title', 'author__username')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created_at')
    ordering = ('-created_at',)
    search_fields = ('post__title', 'author__username')
