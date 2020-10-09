from django.db import models
from products.models import Product
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class Status(models.Model):
    name = models.CharField(max_length=24, blank=True, null=True, default=0)
    is_active = models.BooleanField(default = True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Статус {}".format(self.name)

    class Meta:
        verbose_name = "Статус заказа"
        verbose_name_plural = "Статусы заказа"



class Order(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, default=None, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0) #total price for all products in order
    customer_name = models.CharField(max_length=64, blank=True, null=True, default=None)
    customer_email = models.EmailField(blank=True, null=True, default=None)
    customer_phone = models.CharField(max_length=48, blank=True, null=True, default=None)
    customer_address = models.CharField(max_length=128, blank=True, null=True, default=None)
    comments = models.TextField(blank=True, null=True, default=None)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Заказ {} {}".format(self.id, self.status.name)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def save(self, *args, **kwargs):
        super(Order, self).save(*args, **kwargs)



class  ProductInOrder(models.Model):
    order = models.ForeignKey(Order,  blank=True, null=True, default=None, on_delete=models.CASCADE)
    product = models.ForeignKey(Product,  blank=True, null=True, default=None, on_delete=models.CASCADE)
    nmb = models.IntegerField(default=1)
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    product_discount = models.IntegerField(default=0)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0) #price*nmb
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Товар {}, {}".format(self.id, self.product.name)

    class Meta:
        verbose_name = "Товар в заказе"
        verbose_name_plural = "Товары в заказе"


    def save(self, *args, **kwargs):
        product_discount = self.product.discount
        self.product_discount = product_discount
        price_per_item = self.product.price
        self.price_per_item = price_per_item
        discount_price = self.product.price_with_discount
        self.discount_price = discount_price
        print(self.nmb)

        if product_discount != 0:
            total_price = int(self.nmb) * discount_price
        else:
            total_price = int(self.nmb) * price_per_item

        self.total_price = total_price
        super(ProductInOrder, self).save(*args, **kwargs)




def product_in_order_post_save(sender, instance, created, **kwargs):
    order = instance.order
    all_products_in_order = ProductInOrder.objects.filter(order=order, is_active=True)

    order_total_price = 0
    for item in all_products_in_order:
        order_total_price += item.total_price

    instance.order.total_price = order_total_price
    instance.order.save(force_update=True)

post_save.connect(product_in_order_post_save, sender=ProductInOrder)


class  ProductInBasket(models.Model):
    session_key = models.CharField(max_length=128, blank=True, null=True, default=None)
    order = models.ForeignKey(Order,  blank=True, null=True, default=None, on_delete=models.CASCADE)
    product = models.ForeignKey(Product,  blank=True, null=True, default=None, on_delete=models.CASCADE)
    nmb = models.IntegerField(default=1)
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0) #price*nmb
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Товар {}".format(self.product.name)

    class Meta:
        verbose_name = "Товар в корзине"
        verbose_name_plural = "Товары в корзине"

    def save(self, *args, **kwargs):
        if self.product.discount != 0 :
            price_per_item = self.product.price_with_discount
        else:
            price_per_item = self.product.price

        self.price_per_item = float(price_per_item)
        self.total_price = int(self.nmb) * price_per_item

        super(ProductInBasket, self).save(*args, **kwargs)
