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
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active = True)
    products_images_kofe_v_zernah = products_images.filter(product__category__id=1)
    products_images_kofe_v_kapsulah = products_images.filter(product__category__id=2)
    return render(request, 'blog/home.html', locals())
