"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from products import views

urlpatterns = [
    path('product/<int:product_id>', views.product, name='product')
    #path('', views.blog, name='blog'),
    #path('post/<int:pk>/', views.post_detail, name='post_detail'),
    #path('post/new/', views.post_new, name='post_new'),
    #path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    #path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]
