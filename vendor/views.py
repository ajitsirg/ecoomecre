
from .models import Vendor
from vendor.serializer import VendorSerializer
from rest_framework import generics ,permissions
    
class VendorList(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    permission_classes=[permissions.IsAuthenticated]
    


class VendorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer    
        