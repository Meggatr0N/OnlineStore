# Generated by Django 2.2.12 on 2020-08-09 20:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_auto_20200809_2259'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productinorder',
            old_name='price_per_item_with_discount',
            new_name='discount_price',
        ),
        migrations.RenameField(
            model_name='productinorder',
            old_name='discount_of_product',
            new_name='product_discount',
        ),
    ]