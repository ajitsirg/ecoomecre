from rest_framework import  serializers
from .models import *

class CoustmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coustmer
        fields =['id' ,'name','mobile_number','address','gender','city','state','pincode']

    def __init__(self, *args, **kwargs):
        super(CoustmerSerializer, self).__init__(*args,**kwargs)
        self.Meta.depth = 1    

















