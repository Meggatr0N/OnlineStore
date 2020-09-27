from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name = "Категория товара"
        verbose_name_plural = "Категория товаров"


class Product(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    discount = models.IntegerField(default=0)
    price_with_discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, blank=True, null=True, default=None)
    short_description = models.TextField(blank=True, null=True, default=None)
    description = models.TextField(blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "{}, {}".format(self.price, self.name)

        
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def save(self, *args, **kwargs):

        if self.discount != 0 :
            price_with_discount = self.price * (100 - self.discount) / 100
        else:
            price_with_discount = 0

        self.price_with_discount = price_with_discount
        super(Product, self).save(*args, **kwargs)  # Call the "real" save() method.





class ProductImage(models.Model):
    product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')
    is_main = models.BooleanField(default = False)
    is_active = models.BooleanField(default = True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "{}".format(self.id)

    class Meta:
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"



class Comment(models.Model):
    product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.product)
