# Generated by Django 4.1.1 on 2022-09-16 03:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_products_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productcategory',
            options={'verbose_name_plural': 'Product Category'},
        ),
        migrations.AlterModelOptions(
            name='products',
            options={'verbose_name_plural': 'Products'},
        ),
    ]
