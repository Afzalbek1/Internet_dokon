from django.urls import path
from .views import index, product_detail, products_by_category

urlpatterns = [
    path('', index, name='index'),
    path('category/<slug:slug>/', products_by_category, name='products_by_category'),
    path('product/<slug:slug>/', product_detail, name='product_detail'),
]
