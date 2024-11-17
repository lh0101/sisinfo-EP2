#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py migrate

# Criar um superusuário automático (substitua com seus dados)
echo "
from django.contrib.auth import get_user_model;
User = get_user_model();
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'luiz.piffermarques@usp.br', 'PMR3304');
else:
    print('Superuser already exists');
" | python manage.py shell

# Criar categorias padrão (verifica antes de criar)
echo "
from posts.models import Category;
categories = [
    {'name': 'Grande Prêmios', 'description': 'Descrição sobre Grande Prêmios'},
    {'name': 'Equipes', 'description': 'Descrição sobre Equipes'},
    {'name': 'Personalidades', 'description': 'Descrição sobre Personalidades'},
    {'name': 'Curiosidades', 'description': 'Descrição sobre Curiosidades'}
];
for category in categories:
    if not Category.objects.filter(name=category['name']).exists():
        Category.objects.create(**category);
    else:
        print(f\"Categoria '{category['name']}' já existe\");
" | python manage.py shell
