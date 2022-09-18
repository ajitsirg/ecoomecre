# Generated by Django 4.1.1 on 2022-09-18 02:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0001_initial'),
        ('products', '0003_alter_productcategory_options_alter_products_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.productcategory'),
        ),
        migrations.AddField(
            model_name='products',
            name='vendor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='vendor.vendor'),
        ),
    ]