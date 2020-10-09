from django.shortcuts import render
from .models import *

def product(request, product_id):
    product = Product.objects.get(id=product_id)

    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    print(request.session.session_key)

    product_sug = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active = True).order_by('product__category')
    product_suggestions = product_sug.order_by("-id")[:8]


    return render(request, 'products/product.html', {
        'product': product,
        'product_suggestions': product_suggestions,
    })
