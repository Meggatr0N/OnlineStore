from django.shortcuts import render, get_object_or_404
from .models import *

def product(request, product_id, product_slug, category_slug):
    product = get_object_or_404(Product, id=product_id, slug=product_slug, is_active=True)

    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
    print("     Session_key:   " + request.session.session_key)

    #Предложение похожих продуктов под основной инфой про продукт
    product_sug = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active = True).filter(product__category__slug=category_slug).exclude(product__id=product_id)
    product_suggestions = product_sug.order_by("-id")[:4]

    return render(request, 'products/product.html', {
        'product': product,
        'product_suggestions': product_suggestions,
    })


def catalog(request, category_slug=None):
    category = None
    categories = ProductCategory.objects.all()
    products = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active = True)
    if category_slug:
        category = get_object_or_404(ProductCategory, slug=category_slug)
        products = products.filter(product__category=category)
    return render(request, 'catalog_page/catalog.html', {
        'category': category,
        'categories': categories,
        'products': products,
    })
