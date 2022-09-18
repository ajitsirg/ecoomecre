from django.db import models

# Create your models here.



class Seller(models.Model):
    name = models.CharField(max_length=120,null=True,blank=True)
    