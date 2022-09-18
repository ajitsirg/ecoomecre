from django.shortcuts import render

# Create your views here.


from products.models import *
from .serializer import *
from rest_framework import generics ,permissions
    
class ProductCategoryList(generics.ListCreateAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCatogoriesSerializer
    permission_classes=[permissions.IsAuthenticated]


class ProductList(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    permission_classes=[permissions.IsAuthenticated]  




class ProductDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    permission_classes=[permissions.IsAuthenticated] 



class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes=[permissions.IsAuthenticated]  




class OrderDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes=[permissions.IsAuthenticated] 


class OrderItemList(generics.ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes=[permissions.IsAuthenticated]  




class OrderItemDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes=[permissions.IsAuthenticated] 