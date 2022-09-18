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



class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields =['id','order_number','coustmer','created','updated']
    

    def __init__(self, *args, **kwargs):
        super(OrderSerializer, self).__init__(*args,**kwargs)
        self.Meta.depth = 1

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields =['id','order','product']
    

    def __init__(self, *args, **kwargs):
        super(OrderItemSerializer, self).__init__(*args,**kwargs)
        self.Meta.depth = 1















