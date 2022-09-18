from operator import mod
from pyexpat import model
# from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Vendor(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    full_name=models.CharField(max_length=255,blank=True, null=True)
    address=models.TextField(max_length=300, blank=True, null=True)
    mobile_number=models.IntegerField(max_length=14, blank=True, null=True)
    
    
    def __str__(Vendor):
        return Vendor.full_name