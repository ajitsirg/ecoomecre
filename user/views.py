from django.shortcuts import render
from .models import Coustmer
from rest_framework import generics ,permissions
from . serializer import *

# Create your views here.

class CoustmerList(generics.ListCreateAPIView):
    queryset = Coustmer.objects.all()
    serializer_class = CoustmerSerializer
    permission_classes=[permissions.IsAuthenticated]  




class CoustmerDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Coustmer.objects.all()
    serializer_class = CoustmerSerializer
    permission_classes=[permissions.IsAuthenticated] 