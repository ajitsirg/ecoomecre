from django.db import models

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
    product_details=models.TextField(blank=True, null=True)
    price=models.DecimalField(max_digits=8, decimal_places=2,blank=True)
    margin=models.DecimalField(max_digits=8, decimal_places=2,blank=True)
    discount=models.DecimalField(max_digits=8, decimal_places=2,blank=True)
    
    def __str__(Products) :
        return Products.title
    
    
    class Meta:
        verbose_name_plural = "Products"
       