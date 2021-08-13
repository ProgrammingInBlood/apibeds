from rest_framework import serializers
from .models import *



class Cart_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Cart
        fields='__all__'
