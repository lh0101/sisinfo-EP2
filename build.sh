#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate
# Criar um superusuário automático (substitua com seus dados)
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'luiz.piffermarques@usp.br', 'PMR3304')" | python manage.py shell

# Criar categorias padrão (opcional)
echo "from posts.models import Category; Category.objects.bulk_create([Category(name='Grande Prêmios', description='Descrição'), Category(name='Equipes', description='Descrição'), Category(name='Personalidades', description='Descrição'), Category(name='Curiosidades', description='Descrição')], ignore_conflicts=True)" | python manage.py shell
