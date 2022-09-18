from django.shortcuts import render

# Create your views here.


from products.models import ProductCategory,Products
from .serializer import ProductCatogoriesSerializer,ProductSerializer
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
