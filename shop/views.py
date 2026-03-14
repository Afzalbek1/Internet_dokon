from django.shortcuts import get_object_or_404, render
from .models import Category, Product


def index(request):
    categories = Category.objects.prefetch_related("products").all()
    products = Product.objects.filter(
        is_available=True
    ).select_related("category").prefetch_related("images")

    context = {
        "categories": categories,
        "products": products,
        "featured_products": products[:8],
        "new_products": products[:4],
    }
    return render(request, "index.html", context)


def products_by_category(request, slug):
    categories = Category.objects.prefetch_related("products").all()
    category = get_object_or_404(Category, slug=slug)

    products = Product.objects.filter(
        category=category,
        is_available=True,
    ).select_related("category").prefetch_related("images")

    context = {
        "categories": categories,
        "category": category,
        "products": products,
    }
    return render(request, "category_products.html", context)


def product_detail(request, slug):
    categories = Category.objects.prefetch_related("products").all()
    product = get_object_or_404(
        Product.objects.select_related("category").prefetch_related("images"),
        slug=slug,
        is_available=True,
    )
    related_products = Product.objects.filter(
        category=product.category,
        is_available=True,
    ).exclude(id=product.id).select_related("category").prefetch_related("images")[:4]

    context = {
        "categories": categories,
        "product": product,
        "images": product.images.all(),
        "related_products": related_products,
    }
    return render(request, "product_detail.html", context)
