from django.shortcuts import render, get_object_or_404
from .models import Category, Product
# Create your views here.


def category_list(request):
    categories = Category.objects.all()
    return render(
        request, 
        'categories.html',
          {
            'categories': categories
          }
        )


def product_list(request):
    products = Product.objects.all()
    return render(
        request, 
        'products.html', 
        {
        'products': products
        }
        )


def category_detail(request, category_id):
    category = get_object_or_404(category, id=category_id)
    products = category.products.all()
    return render(
        request, 
        'category_products.html', 
        {
        'category': category, 
        'products': products
        }
        )


