from django.contrib import admin
from django.urls import path, include
from posts import views  # Certifique-se de que o módulo 'views' está importado

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls')),  # Inclui as URLs do app 'posts'
    path('accounts/login/', include('django.contrib.auth.urls')),  # URLs padrão do Django
    path('accounts/signup/', views.register, name='signup'),  # Adiciona a URL de cadastro
]
