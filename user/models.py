from random import choices
from django.db import models

# Create your models here.

gender_option=   (("male", "Male"),("female", "Female"))




class Coustmer(models.Model):
    name = models.CharField(max_length=255,blank=True,null=True)
    mobile_number=models.IntegerField(max_length=14,unique=True)
    address = models.CharField(max_length=1000,blank=True,null=True)
    city = models.CharField(max_length=255,blank=True,null=True)
    state = models.CharField(max_length=255,blank=True,null=True)
    pincode = models.IntegerField(max_length=6,blank=True,null=True)
    gender=models.CharField(max_length=10 ,choices=gender_option,default='male')

    def __init__(self):
        return self.name