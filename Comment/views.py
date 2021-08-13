from django.shortcuts import render

# Create your views here.
from django.db.models import query
from django.shortcuts import render,redirect
from rest_framework import viewsets
from django.contrib.auth import authenticate,login
from .serializers import *
from .models import *

from rest_framework.response import Response 
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated,AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters



class Customercomment_view(viewsets.ViewSet):
    #permission_classes=[IsAuthenticated]

    def list(self,request):
       # Customer.objects.filter(ratings__isnull=False).order_by('ratings__average')

        queryset = Customer.objects.all()
        serializer_class =CustomercommentSerializer(queryset,many=True)
        #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        return Response(serializer_class.data)

    def create(self,request,pk=None):
        serializer_class = CustomercommentSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)

        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        queryset = Customer.objects.get(pk=pk)
      
        serializer_class = CustomercommentSerializer(queryset)
        return Response(serializer_class.data)

    def update(self,request,pk=None):
        queryset = Customer.objects.get(pk=pk)
        serializer_class = CustomercommentSerializer(queryset,data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None):
        queryset = Customer.objects.get(pk=pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)