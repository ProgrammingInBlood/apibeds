from django.shortcuts import render
from rest_framework import viewsets
from .models import BillingDetails
from .serializers import BillingDetails_Serializer
from rest_framework.response import Response

# Create your views here.
class Billing_view(viewsets.ViewSet):
    def list(self,request):
        queryset =BillingDetails.objects.all()
        serializer_class =BillingDetails_Serializer(queryset,many=True)
        #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        return Response(serializer_class.data)

    def create(self,request,pk=None):
        serializer_class = BillingDetails_Serializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)

        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        queryset = BillingDetails.objects.get(pk=pk)
      
        serializer_class =BillingDetails_Serializer(queryset)
        return Response(serializer_class.data)

    def update(self,request,pk=None):
        queryset =BillingDetails.objects.get(pk=pk)
        serializer_class = BillingDetails_Serializer(queryset,data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None):
        queryset = BillingDetails.objects.get(pk=pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#=====================================================================================================================================================
from django.db.models import query
from django.shortcuts import render,redirect
from rest_framework import viewsets
from django.contrib.auth import authenticate,login
from .serializers import *
from Product.models import *

from rest_framework.response import Response 
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated,AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters



class Divanbeds_view(viewsets.ViewSet):
    #permission_classes=[IsAuthenticated]

    def list(self,request):
        queryset =Add_new_product.objects.all()
        serializer_class =Divanbed_Serializer(queryset,many=True)

        filter_backends = [filters.SearchFilter]
        search_fields = ['', 'email']
        #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        return Response(serializer_class.data)

    def create(self,request,pk=None):
        serializer_class = Divanbed_Serializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)

        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        queryset = Add_new_product.objects.get(pk=pk)
      
        serializer_class = Divanbed_Serializer(queryset)
        return Response(serializer_class.data)

    def update(self,request,pk=None):
        queryset = Add_new_product.objects.get(pk=pk)
        serializer_class = Divanbed_Serializer(queryset,data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None):
        queryset = Add_new_product.objects.get(pk=pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class Ottoman_view(viewsets.ViewSet):
    #permission_classes=[IsAuthenticated]

    def list(self,request):
        queryset =All_Beds.objects.filter(beds_category='Ottoman Beds')
        serializer_class =All_Beds_serializer(queryset,many=True)
        #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        return Response(serializer_class.data)

    def create(self,request,pk=None):
        serializer_class = All_Beds_serializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)

        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        queryset = All_Beds.objects.filter(beds_category='Ottoman Beds')
      
        serializer_class = All_Beds_serializer(queryset)
        return Response(serializer_class.data)

    def update(self,request,pk=None):
        queryset = All_Beds.objects.filter(beds_category='Ottoman Beds')
        serializer_class = All_Beds_serializer(queryset,data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None):
        queryset = All_Beds.objects.filter(beds_category='Ottoman Beds')
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


###################################>>>>>>>>>>>>>>>>>.Kids Beds<<<<<<<<<<<<<<<<<<<<<<<################################

class Kids_view(viewsets.ViewSet):
    #permission_classes=[IsAuthenticated]

    def list(self,request):
        queryset =All_Beds.objects.filter(beds_category='Kids Beds')
        serializer_class =All_Beds_serializer(queryset,many=True)
        #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        return Response(serializer_class.data)

    def create(self,request,pk=None):
        serializer_class = All_Beds_serializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)

        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        queryset = All_Beds.objects.filter(beds_category='Kids Beds')
      
        serializer_class = All_Beds_serializer(queryset)
        return Response(serializer_class.data)

    def update(self,request,pk=None):
        queryset = All_Beds.objects.filter(beds_category='Kids Beds')
        serializer_class = All_Beds_serializer(queryset,data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None):
        queryset = All_Beds.objects.filter(beds_category='Kids Beds')
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

################################>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Leather Beds <<<<<<<<<<<<<<<$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
class Leather_view(viewsets.ViewSet):
    #permission_classes=[IsAuthenticated]

    def list(self,request):
        queryset =All_Beds.objects.filter(beds_category='Leather Beds')
        serializer_class =All_Beds_serializer(queryset,many=True)
        #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        return Response(serializer_class.data)

    def create(self,request,pk=None):
        serializer_class = All_Beds_serializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)

        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        queryset = All_Beds.objects.filter(beds_category='Leather Beds')
      
        serializer_class = All_Beds_serializer(queryset)
        return Response(serializer_class.data)

    def update(self,request,pk=None):
        queryset = All_Beds.objects.filter(beds_category='Leather Beds')
        serializer_class = All_Beds_serializer(queryset,data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None):
        queryset = All_Beds.objects.filter(beds_category='Leather Beds')
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



################################>>>>>>>>>>>>>>>>>>>> Nevada Beds <<<<<<<<<<<<<$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
class Nevada_view(viewsets.ViewSet):
    #permission_classes=[IsAuthenticated]

    def list(self,request):
        queryset =All_Beds.objects.filter(beds_category='Nevada Beds')
        serializer_class =All_Beds_serializer(queryset,many=True)
        #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        return Response(serializer_class.data)

    def create(self,request,pk=None):
        serializer_class = All_Beds_serializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)

        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        queryset = All_Beds.objects.filter(beds_category='Nevada Beds')
      
        serializer_class = All_Beds_serializer(queryset)
        return Response(serializer_class.data)

    def update(self,request,pk=None):
        queryset = All_Beds.objects.filter(beds_category='Nevada Beds')
        serializer_class = All_Beds_serializer(queryset,data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None):
        queryset = All_Beds.objects.filter(beds_category='Nevada Beds')
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

##############################>>>>>>>>>>>>>>>>>>>  Stoarage Beds <<<<<<<<<<<<,,$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
class Storage_view(viewsets.ViewSet):
    #permission_classes=[IsAuthenticated]

    def list(self,request):
        queryset =All_Beds.objects.filter(beds_category='Storage Beds')
        serializer_class =All_Beds_serializer(queryset,many=True)
        #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        return Response(serializer_class.data)

    def create(self,request,pk=None):
        serializer_class = All_Beds_serializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)

        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        queryset = All_Beds.objects.filter(beds_category='Storage Beds')
      
        serializer_class = All_Beds_serializer(queryset)
        return Response(serializer_class.data)

    def update(self,request,pk=None):
        queryset = All_Beds.objects.filter(beds_category='Storage Beds')
        serializer_class = All_Beds_serializer(queryset,data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None):
        queryset = All_Beds.objects.filter(beds_category='Storage Beds')
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#########################################>>>>>>>>>>>>>>>>>>>>> Sleigh Beds <<<<<<<<<<<<<<<<<<<<< $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


#==========Florida beds ====================
class Florida_Beds_view(viewsets.ViewSet):
    #permission_classes=[IsAuthenticated]

    def list(self,request):
        queryset =All_Beds.objects.filter(beds_category='Florida Bed Range')
        serializer_class =All_Beds_serializer(queryset,many=True)
        #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        return Response(serializer_class.data)

    def create(self,request,pk=None):
        serializer_class = All_Beds_serializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)

        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        queryset = All_Beds.objects.filter(beds_category='Florida Bed Range')
      
        serializer_class = All_Beds_serializer(queryset)
        return Response(serializer_class.data)

    def update(self,request,pk=None):
        queryset = All_Beds.objects.filter(beds_category='Florida  Bed Range')
        serializer_class = All_Beds_serializer(queryset,data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None):
        queryset = All_Beds.objects.filter(beds_category='Florida Bed Range')
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#==========Ambassador Range beds ==============
class Ambassador_Beds_view(viewsets.ViewSet):
    #permission_classes=[IsAuthenticated]

    def list(self,request):
        queryset =All_Beds.objects.filter(beds_category='Ambassador Range')
        serializer_class =All_Beds_serializer(queryset,many=True)
        #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        return Response(serializer_class.data)

    def create(self,request,pk=None):
        serializer_class = All_Beds_serializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)

        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        queryset = All_Beds.objects.filter(beds_category='Ambassador Range')
      
        serializer_class = All_Beds_serializer(queryset)
        return Response(serializer_class.data)

    def update(self,request,pk=None):
        queryset = All_Beds.objects.filter(beds_category='Ambassador Range')
        serializer_class = All_Beds_serializer(queryset,data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None):
        queryset = All_Beds.objects.filter(beds_category='Ambassador Range')
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#==========Kendall Range beds
class Kendall_Beds_view(viewsets.ViewSet):
    #permission_classes=[IsAuthenticated]

    def list(self,request):
        queryset =All_Beds.objects.filter(beds_category='Kendal Bed')
        serializer_class =All_Beds_serializer(queryset,many=True)
        #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        return Response(serializer_class.data)

    def create(self,request,pk=None):
        serializer_class = All_Beds_serializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)

        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        queryset = All_Beds.objects.filter(beds_category='Kendal Bed')
      
        serializer_class = All_Beds_serializer(queryset)
        return Response(serializer_class.data)

    def update(self,request,pk=None):
        queryset = All_Beds.objects.filter(beds_category='Kendal Bed')
        serializer_class = All_Beds_serializer(queryset,data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None):
        queryset = All_Beds.objects.filter(beds_category='Kendal Bed')
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



#==========Kendall Range beds
class Manoco_Beds_view(viewsets.ViewSet):
    #permission_classes=[IsAuthenticated]

    def list(self,request):
        queryset =All_Beds.objects.filter(beds_category='Manoco Range')
        serializer_class =All_Beds_serializer(queryset,many=True)
        #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        return Response(serializer_class.data)

    def create(self,request,pk=None):
        serializer_class = All_Beds_serializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)

        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        queryset = All_Beds.objects.filter(beds_category='Manoco Range')
      
        serializer_class = All_Beds_serializer(queryset)
        return Response(serializer_class.data)

    def update(self,request,pk=None):
        queryset = All_Beds.objects.filter(beds_category='Manoco Range')
        serializer_class = All_Beds_serializer(queryset,data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None):
        queryset = All_Beds.objects.filter(beds_category='Manoco Range')
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



#==========Kendall Range beds
class Royal_Beds_view(viewsets.ViewSet):
    #permission_classes=[IsAuthenticated]

    def list(self,request):
        queryset =All_Beds.objects.filter(beds_category='Royal Beds Range')
        serializer_class =All_Beds_serializer(queryset,many=True)
        #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        return Response(serializer_class.data)

    def create(self,request,pk=None):
        serializer_class = All_Beds_serializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)

        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        queryset = All_Beds.objects.filter(beds_category='Royal Beds Range')
      
        serializer_class = All_Beds_serializer(queryset)
        return Response(serializer_class.data)

    def update(self,request,pk=None):
        queryset = All_Beds.objects.filter(beds_category='Royal Beds Range')
        serializer_class = All_Beds_serializer(queryset,data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None):
        queryset = All_Beds.objects.filter(beds_category='Royal Beds Range')
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



#==========  Swan  beds  Range
class Swan_Beds_view(viewsets.ViewSet):
    #permission_classes=[IsAuthenticated]

    def list(self,request):
        queryset =All_Beds.objects.filter(beds_category='Swan Bed Range')
        serializer_class =All_Beds_serializer(queryset,many=True)
        #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        return Response(serializer_class.data)

    def create(self,request,pk=None):
        serializer_class = All_Beds_serializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)

        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        queryset = All_Beds.objects.filter(beds_category='Kendal Bed')
      
        serializer_class = All_Beds_serializer(queryset)
        return Response(serializer_class.data)

    def update(self,request,pk=None):
        queryset = All_Beds.objects.filter(beds_category='Swan Bed Range')
        serializer_class = All_Beds_serializer(queryset,data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None):
        queryset = All_Beds.objects.filter(beds_category='Swan Bed Range')
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



#==========  Wing Range beds
class Wing_Beds_view(viewsets.ViewSet):
    #permission_classes=[IsAuthenticated]

    def list(self,request):
        queryset =All_Beds.objects.filter(beds_category='Wing Bed Range')
        serializer_class =All_Beds_serializer(queryset,many=True)
        #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        return Response(serializer_class.data)

    def create(self,request,pk=None):
        serializer_class = All_Beds_serializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)

        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        queryset = All_Beds.objects.filter(beds_category='Wing Bed Range')
      
        serializer_class = All_Beds_serializer(queryset)
        return Response(serializer_class.data)

    def update(self,request,pk=None):
        queryset = All_Beds.objects.filter(beds_category='Wing Bed Range')
        serializer_class = All_Beds_serializer(queryset,data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None):
        queryset = All_Beds.objects.filter(beds_category='Wing Bed Range')
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#==========  Wing Range beds
class Winchester_Beds_view(viewsets.ViewSet):
    #permission_classes=[IsAuthenticated]

    def list(self,request):
        queryset =All_Beds.objects.filter(beds_category='Winchester Bed')
        serializer_class =All_Beds_serializer(queryset,many=True)
        #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        return Response(serializer_class.data)

    def create(self,request,pk=None):
        serializer_class = All_Beds_serializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)

        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        queryset = All_Beds.objects.filter(beds_category='Winchester Bed')
      
        serializer_class = All_Beds_serializer(queryset)
        return Response(serializer_class.data)

    def update(self,request,pk=None):
        queryset = All_Beds.objects.filter(beds_category='Winchester Bed')
        serializer_class = All_Beds_serializer(queryset,data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None):
        queryset = All_Beds.objects.filter(beds_category='Winchester Bed')
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#######################################################$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$>>>>>>>>>  Others Products Views <<<<<<<<,,###########

########################## Fabric Sofa View #############################

class Fabric_Sofa_view(viewsets.ViewSet):
    #permission_classes=[IsAuthenticated]

    def list(self,request):
        queryset =OTHERS.objects.filter(other_category='Fabric Sofa' )
        serializer_class =Other_Beds_serializer(queryset,many=True)
        #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        return Response(serializer_class.data)

    def create(self,request,pk=None):
        serializer_class = Other_Beds_serializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)

        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        queryset = OTHERS.objects.filter(other_category='Fabric Sofa')
      
        serializer_class = Other_Beds_serializer(queryset)
        return Response(serializer_class.data)

    def update(self,request,pk=None):
        queryset = OTHERS.objects.filter(other_category='Fabric Sofa')
        serializer_class = Other_Beds_serializer(queryset,data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None):
        queryset = OTHERS.objects.filter(other_category='Fabric Sofa')
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



###################################################>>>>>>>>>>>>  Leather Sofa <<<<<<<<< $$$$$$$$$$$$$$$$$$$$$$$$$$


class Leather_Sofa_view(viewsets.ViewSet):
    #permission_classes=[IsAuthenticated]

    def list(self,request):
        queryset =OTHERS.objects.filter(other_category='Leather Sofa')
        serializer_class =Other_Beds_serializer(queryset,many=True)
        #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        return Response(serializer_class.data)

    def create(self,request,pk=None):
        serializer_class = Other_Beds_serializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)

        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        queryset = OTHERS.objects.filter(other_category='Leather Sofa')
      
        serializer_class = Other_Beds_serializer(queryset)
        return Response(serializer_class.data)

    def update(self,request,pk=None):
        queryset = OTHERS.objects.filter(other_category='Leather_Sofa')
        serializer_class = Other_Beds_serializer(queryset,data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None):
        queryset = OTHERS.objects.filter(other_category='Leather Sofa')
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)








################################# >>>>>>>>>>>>>>>>... Furniture <<<<<<<<<<<<<<<<<<<<,$$$$$$$$$$$$$$$$$$$$$$$$$$

class Funiture_view(viewsets.ViewSet):
    #permission_classes=[IsAuthenticated]

    def list(self,request):
        queryset =OTHERS.objects.filter(other_category='Furniture')
        serializer_class =Other_Beds_serializer(queryset,many=True)
        #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        return Response(serializer_class.data)

    def create(self,request,pk=None):
        serializer_class = Other_Beds_serializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)

        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        queryset = OTHERS.objects.filter(other_category='Furniture')
      
        serializer_class = All_Beds_serializer(queryset)
        return Response(serializer_class.data)

    def update(self,request,pk=None):
        queryset = OTHERS.objects.filter(other_category='Funiture')
        serializer_class = Other_Beds_serializer(queryset,data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None):
        queryset = OTHERS.objects.filter(other_category='Furniture')
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



################################# >>>>>>>>>>>>>>>>...TAbles <<<<<<<<<<<<<<<<<<<<,$$$$$$$$$$$$$$$$$$$$$$$$$$

class Table_view(viewsets.ViewSet):
    #permission_classes=[IsAuthenticated]

    def list(self,request):
        queryset =OTHERS.objects.filter(other_category='Tables')
        serializer_class =Other_Beds_serializer(queryset,many=True)
        #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        return Response(serializer_class.data)

    def create(self,request,pk=None):
        serializer_class = Other_Beds_serializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)

        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        queryset = OTHERS.objects.filter(other_category='Tables')
      
        serializer_class = Other_Beds_serializer(queryset)
        return Response(serializer_class.data)

    def update(self,request,pk=None):
        queryset = OTHERS.objects.filter(other_category='Tables')
        serializer_class = Other_Beds_serializer(queryset,data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None):
        queryset = OTHERS.objects.filter(other_category='Tables')
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



#========== Bar Tables======

class BarTable_view(viewsets.ViewSet):
    #permission_classes=[IsAuthenticated]

    def list(self,request):
        queryset =OTHERS.objects.filter(other_category='Bar Tables')
        serializer_class =Other_Beds_serializer(queryset,many=True)
        #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        return Response(serializer_class.data)

    def create(self,request,pk=None):
        serializer_class = Other_Beds_serializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)

        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        queryset = OTHERS.objects.filter(other_category='Bar Tables')
      
        serializer_class = Other_Beds_serializer(queryset)
        return Response(serializer_class.data)

    def update(self,request,pk=None):
        queryset = OTHERS.objects.filter(other_category='Bar Tables')
        serializer_class = Other_Beds_serializer(queryset,data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None):
        queryset = OTHERS.objects.filter(other_category='Bar Tables')
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#===============  Coffee Tables


class CoffeeTable_view(viewsets.ViewSet):
    #permission_classes=[IsAuthenticated]

    def list(self,request):
        queryset =OTHERS.objects.filter(other_category='Coffee Tables')
        serializer_class =Other_Beds_serializer(queryset,many=True)
        #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        return Response(serializer_class.data)

    def create(self,request,pk=None):
        serializer_class = Other_Beds_serializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)

        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        queryset = OTHERS.objects.filter(other_category='Coffee Tables')
      
        serializer_class = Other_Beds_serializer(queryset)
        return Response(serializer_class.data)

    def update(self,request,pk=None):
        queryset = OTHERS.objects.filter(other_category='Coffee Tables')
        serializer_class = Other_Beds_serializer(queryset,data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None):
        queryset = OTHERS.objects.filter(other_category='Coffee Tables')
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Table_view(viewsets.ViewSet):
    #permission_classes=[IsAuthenticated]

    def list(self,request):
        queryset =OTHERS.objects.filter(other_category='Coffee Tables')
        serializer_class =Other_Beds_serializer(queryset,many=True)
        #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        return Response(serializer_class.data)

    def create(self,request,pk=None):
        serializer_class = Other_Beds_serializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)

        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        queryset = OTHERS.objects.filter(other_category='Coffee Tables')
      
        serializer_class = Other_Beds_serializer(queryset)
        return Response(serializer_class.data)

    def update(self,request,pk=None):
        queryset = OTHERS.objects.filter(other_category='Coffee Tables')
        serializer_class = Other_Beds_serializer(queryset,data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None):
        queryset = OTHERS.objects.filter(other_category='Coffee Tables')
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#================== Dinning TAbles


class DinningTable_view(viewsets.ViewSet):
    #permission_classes=[IsAuthenticated]

    def list(self,request):
        queryset =OTHERS.objects.filter(other_category='Dinning Tables')
        serializer_class =Other_Beds_serializer(queryset,many=True)
        #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        return Response(serializer_class.data)

    def create(self,request,pk=None):
        serializer_class = Other_Beds_serializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)

        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        queryset = OTHERS.objects.filter(other_category='Dinning Tables')
      
        serializer_class = Other_Beds_serializer(queryset)
        return Response(serializer_class.data)

    def update(self,request,pk=None):
        queryset = OTHERS.objects.filter(other_category='Dinning Tables')
        serializer_class = Other_Beds_serializer(queryset,data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None):
        queryset = OTHERS.objects.filter(other_category='Dinning Tables')
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#================= Dressing Tables


class DressingTable_view(viewsets.ViewSet):
    #permission_classes=[IsAuthenticated]

    def list(self,request):
        queryset =OTHERS.objects.filter(other_category='Dressing Tables')
        serializer_class =Other_Beds_serializer(queryset,many=True)
        #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        return Response(serializer_class.data)

    def create(self,request,pk=None):
        serializer_class = Other_Beds_serializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)

        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        queryset = OTHERS.objects.filter(other_category='Dressing Tables')
      
        serializer_class = Other_Beds_serializer(queryset)
        return Response(serializer_class.data)

    def update(self,request,pk=None):
        queryset = OTHERS.objects.filter(other_category='Dressing Tables')
        serializer_class = Other_Beds_serializer(queryset,data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None):
        queryset = OTHERS.objects.filter(other_category='Dressing Tables')
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#============================

class ManicureTable_view(viewsets.ViewSet):
    #permission_classes=[IsAuthenticated]

    def list(self,request):
        queryset =OTHERS.objects.filter(other_category='Manicure Tables')
        serializer_class =Other_Beds_serializer(queryset,many=True)
        #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        return Response(serializer_class.data)

    def create(self,request,pk=None):
        serializer_class = Other_Beds_serializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)

        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        queryset = OTHERS.objects.filter(other_category='Manicure Tables')
      
        serializer_class = Other_Beds_serializer(queryset)
        return Response(serializer_class.data)

    def update(self,request,pk=None):
        queryset = OTHERS.objects.filter(other_category='Manicure Tables')
        serializer_class = Other_Beds_serializer(queryset,data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None):
        queryset = OTHERS.objects.filter(other_category='Manicure Tables')
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#=============== Side Table


class SideTable_view(viewsets.ViewSet):
    #permission_classes=[IsAuthenticated]

    def list(self,request):
        queryset =OTHERS.objects.filter(other_category='SideTables')
        serializer_class =Other_Beds_serializer(queryset,many=True)
        #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        return Response(serializer_class.data)

    def create(self,request,pk=None):
        serializer_class = Other_Beds_serializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)

        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        queryset = OTHERS.objects.filter(other_category='Side Tables')
      
        serializer_class = Other_Beds_serializer(queryset)
        return Response(serializer_class.data)

    def update(self,request,pk=None):
        queryset = OTHERS.objects.filter(other_category='Side Tables')
        serializer_class = Other_Beds_serializer(queryset,data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None):
        queryset = OTHERS.objects.filter(other_category='Side Tables')
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



################################# >>>>>>>>>>>>>>>>...Chairs  <<<<<<<<<<<<<<<<<<<<,$$$$$$$$$$$$$$$$$$$$$$$$$$

#============= Accent Chairs====

class AccentChairs_view(viewsets.ViewSet):
    #permission_classes=[IsAuthenticated]

    def list(self,request):
        queryset =OTHERS.objects.filter(other_category='Accent Tables')
        serializer_class =Other_Beds_serializer(queryset,many=True)
        #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        return Response(serializer_class.data)

    def create(self,request,pk=None):
        serializer_class = Other_Beds_serializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)

        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        queryset = OTHERS.objects.filter(other_category='Accent Chairs')
      
        serializer_class = Other_Beds_serializer(queryset)
        return Response(serializer_class.data)

    def update(self,request,pk=None):
        queryset = OTHERS.objects.filter(other_category='Accent Chairs')
        serializer_class = All_Beds_serializer(queryset,data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None):
        queryset = OTHERS.objects.filter(other_category='Accent Chairs')
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#============= Arm Tables====

class ArmChairs_view(viewsets.ViewSet):
    #permission_classes=[IsAuthenticated]

    def list(self,request):
        queryset =OTHERS.objects.filter(other_category='Arm Chairs')
        serializer_class =Other_Beds_serializer(queryset,many=True)
        #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        return Response(serializer_class.data)

    def create(self,request,pk=None):
        serializer_class = Other_Beds_serializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)

        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        queryset = OTHERS.objects.filter(other_category='Arm Chairs')
      
        serializer_class = Other_Beds_serializer(queryset)
        return Response(serializer_class.data)

    def update(self,request,pk=None):
        queryset = OTHERS.objects.filter(other_category='Arm Chairs')
        serializer_class = All_Beds_serializer(queryset,data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None):
        queryset = OTHERS.objects.filter(other_category='Arm Chairs')
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



#============= Arm Chairs====

class ChesterfieldChairs_view(viewsets.ViewSet):
    #permission_classes=[IsAuthenticated]

    def list(self,request):
        queryset =OTHERS.objects.filter(other_category='Chesterfield Chairs')
        serializer_class =Other_Beds_serializer(queryset,many=True)
        #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        return Response(serializer_class.data)

    def create(self,request,pk=None):
        serializer_class = Other_Beds_serializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)

        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        queryset = OTHERS.objects.filter(other_category='Chesterfield Chairs')
      
        serializer_class = Other_Beds_serializer(queryset)
        return Response(serializer_class.data)

    def update(self,request,pk=None):
        queryset = OTHERS.objects.filter(other_category='Chesterfield Chairs')
        serializer_class = All_Beds_serializer(queryset,data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None):
        queryset = OTHERS.objects.filter(other_category='Chesterfield Chairs')
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



#============= Dinning sets Chairs====

class DinningChairs_view(viewsets.ViewSet):
    #permission_classes=[IsAuthenticated]

    def list(self,request):
        queryset =OTHERS.objects.filter(other_category='Dinning sets Chairs')
        serializer_class =Other_Beds_serializer(queryset,many=True)
        #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        return Response(serializer_class.data)

    def create(self,request,pk=None):
        serializer_class = Other_Beds_serializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)

        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        queryset = OTHERS.objects.filter(other_category='Dinning sets Chairs')
      
        serializer_class = Other_Beds_serializer(queryset)
        return Response(serializer_class.data)

    def update(self,request,pk=None):
        queryset = OTHERS.objects.filter(other_category='Dinning sets Chairs')
        serializer_class = All_Beds_serializer(queryset,data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None):
        queryset = OTHERS.objects.filter(other_category='Dinning sets Chairs')
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



#============= Fireside Chairs====

class FiresideChairs_view(viewsets.ViewSet):
    #permission_classes=[IsAuthenticated]

    def list(self,request):
        queryset =OTHERS.objects.filter(other_category='Fireside Chairs')
        serializer_class =Other_Beds_serializer(queryset,many=True)
        #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        return Response(serializer_class.data)

    def create(self,request,pk=None):
        serializer_class = Other_Beds_serializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)

        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        queryset = OTHERS.objects.filter(other_category='Fireside Chairs')
      
        serializer_class = Other_Beds_serializer(queryset)
        return Response(serializer_class.data)

    def update(self,request,pk=None):
        queryset = OTHERS.objects.filter(other_category='Fireside Chairs')
        serializer_class = All_Beds_serializer(queryset,data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None):
        queryset = OTHERS.objects.filter(other_category='Fireside Chairs')
        queryset.delete()


#============= Lift Chairs===

class LiftChairs_view(viewsets.ViewSet):
    #permission_classes=[IsAuthenticated]

    def list(self,request):
        queryset =OTHERS.objects.filter(other_category='Lift Chairs')
        serializer_class =Other_Beds_serializer(queryset,many=True)
        #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        return Response(serializer_class.data)

    def create(self,request,pk=None):
        serializer_class = Other_Beds_serializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)

        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        queryset = OTHERS.objects.filter(other_category='Lift Chairs')
      
        serializer_class = Other_Beds_serializer(queryset)
        return Response(serializer_class.data)

    def update(self,request,pk=None):
        queryset = OTHERS.objects.filter(other_category='Lift Chairs')
        serializer_class = All_Beds_serializer(queryset,data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None):
        queryset = OTHERS.objects.filter(other_category='Lift Chairs')
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



#============= Recycling Chairs====

class RecyclingChairs_view(viewsets.ViewSet):
    #permission_classes=[IsAuthenticated]

    def list(self,request):
        queryset =OTHERS.objects.filter(other_category='Recycling Chairs')
        serializer_class =Other_Beds_serializer(queryset,many=True)
        #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        return Response(serializer_class.data)

    def create(self,request,pk=None):
        serializer_class = Other_Beds_serializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)

        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        queryset = OTHERS.objects.filter(other_category='Recycling Chairs')
      
        serializer_class = Other_Beds_serializer(queryset)
        return Response(serializer_class.data)

    def update(self,request,pk=None):
        queryset = OTHERS.objects.filter(other_category='Recycling Chairs')
        serializer_class = All_Beds_serializer(queryset,data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None):
        queryset = OTHERS.objects.filter(other_category='Recycling Chairs')
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(status=status.HTTP_204_NO_CONTENT)


################################# >>>>>>>>>>>>>>>>...ChestDraws <<<<<<<<<<<<<<<<<<<<,$$$$$$$$$$$$$$$$$$$$$$$$$$

class ChestDraws_view(viewsets.ViewSet):
    #permission_classes=[IsAuthenticated]

    def list(self,request):
        queryset =OTHERS.objects.filter(other_category='ChestDraws')
        serializer_class =Other_Beds_serializer(queryset,many=True)
        #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        return Response(serializer_class.data)

    def create(self,request,pk=None):
        serializer_class = Other_Beds_serializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)

        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        queryset = OTHERS.objects.filter(other_category='ChestDraws')
      
        serializer_class = All_Beds_serializer(queryset)
        return Response(serializer_class.data)

    def update(self,request,pk=None):
        queryset = OTHERS.objects.filter(other_category='ChestDraws')
        serializer_class = Other_Beds_serializer(queryset,data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None):
        queryset = OTHERS.objects.filter(other_category='ChestDraws')
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

################################# >>>>>>>>>>>>>>>>...Shelf <<<<<<<<<<<<<<<<<<<<,$$$$$$$$$$$$$$$$$$$$$$$$$$

class Shelf_view(viewsets.ViewSet):
    #permission_classes=[IsAuthenticated]

    def list(self,request):
        queryset =OTHERS.objects.filter(other_category='Shelf')
        serializer_class =Other_Beds_serializer(queryset,many=True)
        #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        return Response(serializer_class.data)

    def create(self,request,pk=None):
        serializer_class = Other_Beds_serializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)

        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        queryset = OTHERS.objects.filter(other_category='Shelf')
      
        serializer_class = Other_Beds_serializer(queryset)
        return Response(serializer_class.data)

    def update(self,request,pk=None):
        queryset = OTHERS.objects.filter(other_category='Shelf')
        serializer_class =Other_Beds_serializer(queryset,data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None):
        queryset = OTHERS.objects.filter(other_category='Shelf')
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

################################# >>>>>>>>>>>>>>>>...WardRobes <<<<<<<<<<<<<<<<<<<<,$$$$$$$$$$$$$$$$$$$$$$$$$$

class WardRobes_view(viewsets.ViewSet):
    #permission_classes=[IsAuthenticated]

    def list(self,request):
        queryset =OTHERS.objects.filter(other_category='WardRobes')
        serializer_class =Other_Beds_serializer(queryset,many=True)
        #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        return Response(serializer_class.data)

    def create(self,request,pk=None):
        serializer_class = Other_Beds_serializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)

        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        queryset = OTHERS.objects.filter(other_category='WardRobes')
      
        serializer_class = All_Beds_serializer(queryset)
        return Response(serializer_class.data)

    def update(self,request,pk=None):
        queryset = OTHERS.objects.filter(other_category='WardRobes')
        serializer_class = Other_Beds_serializer(queryset,data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None):
        queryset = OTHERS.objects.filter(other_category='WardRobes')
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

