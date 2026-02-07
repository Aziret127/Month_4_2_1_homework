from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.category_list, name='categories'),
    path('products/', views.product_list, name='products'),
    path('category/<int:category_id>/', views.category_detail, name='category_products'),
]