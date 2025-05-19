import os
import django

# Configurar entorno Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cafe_project.settings')
django.setup()

from django.contrib.auth.models import User
from cafe_api.models import Category, Product

def create_superuser():
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
        print('Superusuario creado: admin / admin123')
    else:
        print('El superusuario ya existe')

def create_categories():
    categories = [
        {'name': 'Entradas', 'slug': 'starters'},
        {'name': 'Platos Principales', 'slug': 'main'},
        {'name': 'Bebidas', 'slug': 'drinks'},
        {'name': 'Postres', 'slug': 'desserts'},
    ]
    
    for cat_data in categories:
        Category.objects.get_or_create(
            slug=cat_data['slug'],
            defaults={'name': cat_data['name']}
        )
    
    print('Categorías creadas')

def create_products():
    # Asegurarse de que existen las categorías
    if Category.objects.count() == 0:
        create_categories()
    
    products = [
        {
            'name': 'Ensalada César',
            'description': 'Lechuga romana, crutones, queso parmesano y aderezo César',
            'price': 12.99,
            'category_slug': 'starters',
        },
        {
            'name': 'Bruschetta',
            'description': 'Pan tostado con tomate, ajo y albahaca',
            'price': 8.99,
            'category_slug': 'starters',
        },
        {
            'name': 'Pasta Carbonara',
            'description': 'Espagueti con salsa cremosa, panceta y queso parmesano',
            'price': 16.99,
            'category_slug': 'main',
        },
        {
            'name': 'Risotto de Champiñones',
            'description': 'Arroz cremoso con champiñones y queso parmesano',
            'price': 18.99,
            'category_slug': 'main',
        },
        {
            'name': 'Café Americano',
            'description': 'Café negro suave y aromático',
            'price': 3.99,
            'category_slug': 'drinks',
        },
        {
            'name': 'Limonada',
            'description': 'Refrescante limonada casera',
            'price': 4.99,
            'category_slug': 'drinks',
        },
        {
            'name': 'Tiramisú',
            'description': 'Postre italiano con café, mascarpone y cacao',
            'price': 7.99,
            'category_slug': 'desserts',
        },
        {
            'name': 'Cheesecake',
            'description': 'Tarta de queso cremosa con salsa de frutos rojos',
            'price': 6.99,
            'category_slug': 'desserts',
        },
    ]
    
    for prod_data in products:
        category = Category.objects.get(slug=prod_data['category_slug'])
        Product.objects.get_or_create(
            name=prod_data['name'],
            defaults={
                'description': prod_data['description'],
                'price': prod_data['price'],
                'category': category,
                'available': True,
            }
        )
    
    print('Productos creados')

if __name__ == '__main__':
    create_superuser()
    create_categories()
    create_products()
    print('Datos de ejemplo creados correctamente')
