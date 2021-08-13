#from bedsdivan_admin.Product.models import Add_new_product, Drawers, FeetCastor, Headboard, Mattress
from django.shortcuts import render
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



# Create your views here.
def modify_input_for_multiple_files(product_name,product_image):
    dict = {}
    dict['product_name'] = product_name
    dict['product_image'] = product_image
    return dict

class Add_product_view(viewsets.ViewSet):
    #permission_classes=[IsAuthenticated]

    def list(self,request):
        queryset =Add_new_product.objects.all()
        serializer_class =Add_product_Serializer(queryset,many=True)
        # filter_backends = [DjangoFilterBackend]

        # #filter_backends = [DjangoFilterBackend]
        # filterset_fields = ['product_type', 'product_name','size',]
        # #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

        filter_backends = [filters.SearchFilter]
        search_fields = ['product_type', 'product_name','size','color']
        return Response(serializer_class.data)

    def create(self, request):
        product_name = request.data['product_name']
        images = dict((request.data).lists())['product_image']
        flag = 1
        arr = []
        for img_name in images:
            modified_data = modify_input_for_multiple_files(product_name,
                                                            img_name)
            file_serializer = Add_product_Serializer(data=modified_data)
            if file_serializer.is_valid():
                file_serializer.save()
                arr.append(file_serializer.data)
            else:
                flag = 0

        if flag == 1:
            return Response(arr)
        else:
            return Response(arr)

    # def create(self,request,pk=None):
    #     serializer_class = Add_product_Serializer(data=request.data)
    #     if serializer_class.is_valid():
    #         serializer_class.save()
    #         return Response(serializer_class.data,status=status.HTTP_201_CREATED)

    #     else:
    #         return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        queryset = Add_new_product.objects.get(pk=pk)
      
        serializer_class = Add_product_Serializer(queryset)
        return Response(serializer_class.data)

    def update(self,request,pk=None):
        queryset = Add_new_product.objects.get(pk=pk)
        serializer_class = Add_product_Serializer(queryset,data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None):
        queryset = Add_new_product.objects.get(pk=pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# def modify_input_for_multiple_files(image):
#     dict = {}
#     # dict['property_id'] = property_id
#     dict['image'] = image
#     return dict

# from rest_framework import permissions
# from rest_framework.parsers import MultiPartParser, FormParser
# class ImageView(viewsets.ViewSet):
#     permission_classes=[permissions.AllowAny,]
#     parser_classes = (MultiPartParser, FormParser)

#     def list(self, request):
        
#         all_images = Image.objects.all()
#         serializer = ImageSerializer(all_images, many=True)
#         return Response(serializer.data)
    
#     def create(self, request, *args, **kwargs):
#         # property_id = request.data['property_id']

#         # converts querydict to original dict
#         images = dict((request.data).lists())['image']
#         flag = 1
#         arr = []
#         for img_name in images:
#             modified_data = modify_input_for_multiple_files(
#                                                             img_name)
#             file_serializer = ImageSerializer(data=modified_data)
#             if file_serializer.is_valid():
#                 file_serializer.save()
#                 arr.append(file_serializer.data)
#             else:
#                 flag = 0

#         if flag == 1:
#             return Response(arr)
#         else:
#             return Response(arr)





##################################### Divan beds views for end user ##################################
class Divanbeds_view(viewsets.ViewSet):
    #permission_classes=[IsAuthenticated]

    def list(self,request):
        queryset =Add_new_product.objects.all()
        serializer_class =Divanbed_Serializer(queryset,many=True)
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


######################################### Add HeadBoard VIEW ####################################################################

class Add_Headboard_view(viewsets.ViewSet):
    def list(self,request):
        queryset =Headboard.objects.all()
        serializer_class =Headboard_Serializer(queryset,many=True)
        #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        return Response(serializer_class.data)

    def create(self,request,pk=None):
        serializer_class = Headboard_Serializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)

        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        queryset = Headboard.objects.get(pk=pk)
      
        serializer_class = Headboard_Serializer(queryset)
        return Response(serializer_class.data)

    def update(self,request,pk=None):
        queryset = Headboard.objects.get(pk=pk)
        serializer_class = Headboard_Serializer(queryset,data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None):
        queryset = Headboard.objects.get(pk=pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

################################################  MATTRESSESS VIEW  ##############################################################


class Add_Mattress_view(viewsets.ViewSet):
    def list(self,request):
        queryset =Mattress.objects.all()
        serializer_class =Mattresses_Serializer(queryset,many=True)
        #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        return Response(serializer_class.data)

    def create(self,request,pk=None):
        serializer_class = Mattresses_Serializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)

        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        queryset = Mattress.objects.get(pk=pk)
      
        serializer_class =Mattresses_Serializer(queryset)
        return Response(serializer_class.data)

    def update(self,request,pk=None):
        queryset =Mattress.objects.get(pk=pk)
        serializer_class = Mattresses_Serializer(queryset,data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None):
        queryset = Mattress.objects.get(pk=pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



##################################  ADD DRAWERS VIEW   ########################################################################################

class Add_Drawers_view(viewsets.ViewSet):
    def list(self,request):
        queryset =Drawers.objects.all()
        serializer_class =Drawer_Serializer(queryset,many=True)
        #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        return Response(serializer_class.data)

    def create(self,request,pk=None):
        serializer_class = Drawer_Serializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)

        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        queryset = Drawers.objects.get(pk=pk)
      
        serializer_class =Drawer_Serializer(queryset)
        return Response(serializer_class.data)

    def update(self,request,pk=None):
        queryset =Drawers.objects.get(pk=pk)
        serializer_class = Drawer_Serializer(queryset,data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None):
        queryset = Drawers.objects.get(pk=pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


########################################=======>>>>> FEETCASTOR VIEW  <<<<<<======#################################################

class Add_FeetCastor_view(viewsets.ViewSet):
    def list(self,request):
        queryset =FeetCastor.objects.all()
        serializer_class =FeetCastor_Serializer(queryset,many=True)
        #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        return Response(serializer_class.data)

    def create(self,request,pk=None):
        serializer_class = FeetCastor_Serializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)

        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        queryset = FeetCastor.objects.get(pk=pk)
      
        serializer_class =FeetCastor_Serializer(queryset)
        return Response(serializer_class.data)

    def update(self,request,pk=None):
        queryset =Mattress.objects.get(pk=pk)
        serializer_class = FeetCastor_Serializer(queryset,data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None):
        queryset = FeetCastor.objects.get(pk=pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#################

##################################  ADD DRAWERS VIEW   ########################################################################################

class Add_Drawers_view(viewsets.ViewSet):
    def list(self,request):
        queryset =Drawers.objects.all()
        serializer_class =Drawer_Serializer(queryset,many=True)
        #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        return Response(serializer_class.data)

    def create(self,request,pk=None):
        serializer_class = Drawer_Serializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)

        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        queryset = Drawers.objects.get(pk=pk)
      
        serializer_class =Drawer_Serializer(queryset)
        return Response(serializer_class.data)

    def update(self,request,pk=None):
        queryset =Drawers.objects.get(pk=pk)
        serializer_class = Drawer_Serializer(queryset,data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None):
        queryset = Drawers.objects.get(pk=pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

