from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Customer



class CustomercommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields='__all__'