from django.shortcuts import render
from .forms import SubscriberForm
from products.models import *

def blog(request):
    form = SubscriberForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        print(form.cleaned_data)
        data = form.cleaned_data
        print(data["name"])
        new_form = form.save()

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SubscriberForm()

    return render(request, 'blog/base.html', {'form': form})



def home(request):
    all_products = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active = True)
    category_kofe_v_zernah = all_products.filter(product__category__id=1)
    category_kofe_v_kapsulah = all_products.filter(product__category__id=2)

    all_products_last_add = all_products.order_by("-id")[:4]
    category_kofe_v_zernah_last_add = category_kofe_v_zernah.order_by("-id")[:4]
    category_kofe_v_kapsulah_last_add = category_kofe_v_kapsulah.order_by("-id")[:4]

    return render(request, 'blog/home.html', {
        'all_products' : all_products,
        'all_products_last_add' : all_products_last_add,
        'category_kofe_v_zernah_last_add' : category_kofe_v_zernah_last_add,
        'category_kofe_v_kapsulah_last_add' : category_kofe_v_kapsulah_last_add,
    })


def about(request):
    return render(request, 'blog/about.html', {})
