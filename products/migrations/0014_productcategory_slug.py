# Generated by Django 2.2.12 on 2020-10-10 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcategory',
            name='slug',
            field=models.SlugField(null=True, verbose_name='Транслит'),
        ),
    ]
