# Generated by Django 2.2.12 on 2020-08-09 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20200531_1909'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price_with_discount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
