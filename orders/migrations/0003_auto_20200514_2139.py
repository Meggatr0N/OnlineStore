# Generated by Django 2.2.12 on 2020-05-14 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20200514_2130'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='total_price',
            new_name='total_amount',
        ),
    ]
