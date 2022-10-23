from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category

# Create your views here.

def store(request, category_slug=None):
    if category_slug != None:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category, is_available=True)
        no_of_products = products.count()
    else:
        products = Product.objects.filter(is_available=True)
        no_of_products = products.count()

    context = {
        "products": products,
        "no_of_products": no_of_products,
    }
    return render(request, "store/store.html", context)

def product_details(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(slug=product_slug, category__slug=category_slug)
    except Exception as e:
        raise e

    context = {"single_product": single_product}
    return render(request, "store/product_details.html", context)