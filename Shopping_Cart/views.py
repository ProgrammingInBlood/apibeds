from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class Cart_view(viewsets.ViewSet):
    def list(self,request):
        queryset =Cart.objects.all()
        serializer_class =Cart_Serializer(queryset,many=True)
        #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        return Response(serializer_class.data)

    def create(self,request,pk=None):
        serializer_class = Cart_Serializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)

        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        queryset =Cart.objects.get(pk=pk)
      
        serializer_class =Cart_Serializer(queryset,pk=pk)
        Response(serializer_class.data)

    def update(self,request,pk=None):
        queryset =Cart.objects.get(pk=pk)
        serializer_class = Cart_Serializer(queryset)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None):
        queryset =Carts.objects.get(pk=pk)
        return Response(status=status.HTTP_204_NO_CONTENT)