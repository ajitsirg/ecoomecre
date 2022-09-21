from unicodedata import category
from django.db import models
from user.models import Coustmer
from vendor.models import *

# Create your models here.


class ProductCategory(models.Model):
    product_name=models.CharField(max_length=255, unique=True)
    ProductCategory_details=models.TextField(blank=True, null=True)
    
    def __str__(ProductCategory) :
        return ProductCategory.product_name
    class Meta:
        verbose_name_plural = "Product Category"
    
    
    
class Products(models.Model): 
    title=models.CharField(max_length=255, blank=True,)
    category=models.ForeignKey(ProductCategory,on_delete=models.SET_NULL,null=True)
    vendor=models.ForeignKey(Vendor,on_delete=models.SET_NULL,null=True)
    product_details=models.TextField(blank=True, null=True)
    price=models.DecimalField(max_digits=8, decimal_places=2,blank=True)
    margin=models.DecimalField(max_digits=8, decimal_places=2,blank=True)
    discount=models.DecimalField(max_digits=8, decimal_places=2,blank=True)
    actual_price=models.DecimalField(max_digits=8, decimal_places=2,blank=True)
    
    def __str__(Products) :
        return Products.title
    
    
    class Meta:
        verbose_name_plural = "Products"



class Order(models.Model):
    order_number=models.CharField(max_length=8,unique=True)
    coustmer=models.ForeignKey(Coustmer,on_delete=models.CASCADE, related_name='coustmer_orders')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' (self.created)

    def __str__(Order) :
        return Order.order_number    




class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='order_items')
    product=models.ForeignKey(Products,on_delete=models.CASCADE)

    def __str__(self):
        return self.product.title