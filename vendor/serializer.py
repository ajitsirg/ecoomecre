from rest_framework import serializers
from .models import Vendor


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['id', 'user', 'full_name', 'address', 'mobile_number']


    def __init__(self, *args, **kwargs):
        super(VendorSerializer, self).__init__(*args,**kwargs)
        self.Meta.depth = 1

        






class VendorDeatailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['id', 'user', 'full_name', 'address', 'mobile_number']

    def __init__(self, *args, **kwargs):
        super(VendorDeatailsSerializer, self).__init__(*args,**kwargs)
        self.Meta.depth = 1    