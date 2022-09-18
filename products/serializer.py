from rest_framework import  serializers
from .models import *

class ProductCatogoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields =['id' ,'product_name','ProductCategory_details']

    def __init__(self, *args, **kwargs):
        super(ProductCatogoriesSerializer, self).__init__(*args,**kwargs)
        self.Meta.depth = 1    






class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields =['id','title','product_details','category','vendor','price','margin','discount','actual_price']
    

    def __init__(self, *args, **kwargs):
        super(ProductSerializer, self).__init__(*args,**kwargs)
        self.Meta.depth = 1














