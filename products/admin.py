from django.contrib import admin
from .models import *


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0

class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductCategory._meta.fields]
    prepopulated_fields = {'slug': ('name',)}

    class Meta:
        model = ProductCategory

admin.site.register(ProductCategory, ProductCategoryAdmin)



class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]
    inlines = [ProductImageInline]

    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)


class ProductImageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductImage._meta.fields]
    list_filter = ('is_main', 'is_active', 'created', 'updated')

    class Meta:
        model = ProductImage

admin.site.register(ProductImage, ProductImageAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'product', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')
admin.site.register(Comment, CommentAdmin)
