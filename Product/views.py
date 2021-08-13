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

def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            if user.is_superuser:
                login(request,user)
                return redirect('https://bedsdivan-62f7b.web.app/')
            else:
                return render(request,'login.html',{'error':True})
        else:
            return render(request,'login.html',{'error':True})
    else:
        return render(request,'login.html')

# @login_required(login_url='/')
# def dash_board(request):
#     return render(request,'index.html')
#============================================    Add divanbeds 2 aug 2021 ========================================================

class Add_New_Products_view(viewsets.ViewSet):
  
    permission_classes= (AllowAny,)
   # parser_classes = (MultiPartParser,FormParser,JSONParser,FileUploadParser)
    
    # permission_classes = (IsAuthenticated,)
    def list(self,request):
        queryset =Add_New_Products.objects.all()
        serializer =Add_New_Prduct_serializer(queryset,many=True)
        #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        return Response(serializer.data)

    def create(self,request,pk=None):
        queryset=Add_New_Products.objects.all()
        serializer = Add_New_Prduct_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        queryset = Add_New_Products.objects.get(pk=pk)
      
        serializer = Add_New_Prduct_serializer(queryset)
        return Response(serializer.data)

    def update(self,request,pk=None):
        queryset = Add_New_Products.objects.get(pk=pk)
        serializer = Add_New_Prduct_serializer(queryset,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None):
        queryset = Add_New_Products.objects.get(pk=pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





 



#==================================== Add ukdivanbeds===========
class UkDivanbeds_view(viewsets.ViewSet):
    #permission_classes=[IsAuthenticated]

    def list(self,request):
        queryset =Add_Divanbeds.objects.all()
        serializer_class =Add_Bedsdivanbed_serializer(queryset,many=True)
        #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        return Response(serializer_class.data)

    def create(self,request,pk=None):
        serializer_class = Add_Bedsdivanbed_serializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)

        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        queryset = Add_Divanbeds.objects.get(pk=pk)
      
        serializer_class = Add_Bedsdivanbed_serializer(queryset)
        return Response(serializer_class.data)

    def update(self,request,pk=None):
        queryset = Add_Divanbeds.objects.get(pk=pk)
        serializer_class = Add_Bedsdivanbed_serializer(queryset,data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None):
        queryset = Add_Divanbeds.objects.get(pk=pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#========================== Add variant view 5 july ================
class UkBedsVariant_view(viewsets.ViewSet):
    #permission_classes=[IsAuthenticated]

    def list(self,request):
        queryset =Add_BedsVariant.objects.all()
        serializer_class =Add_Bedsvariant_Serializer(queryset,many=True)
        #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        return Response(serializer_class.data)

    def create(self,request,pk=None):
        serializer_class = Add_Bedsvariant_Serializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)

        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        queryset = Add_Divanbeds.objects.get(pk=pk)
      
        serializer_class = Add_Bedsvariant_Serializer(queryset)
        return Response(serializer_class.data)

    def update(self,request,pk=None):
        queryset = Add_Divanbeds.objects.get(pk=pk)
        serializer_class =Add_Bedsvariant_Serializer(queryset,data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None):
        queryset = Add_Divanbeds.objects.get(pk=pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)









#============================  latest add product view===============


class add_Your_Product_view(viewsets.ViewSet):
    #permission_classes=[IsAuthenticated]

    def list(self,request):
        queryset =Add_Product.objects.all()
        serializer_class =Add_Your_Prduct_serializer(queryset,many=True)
        #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        return Response(serializer_class.data)

    def create(self,request,pk=None):
        serializer_class =Add_Your_Prduct_serializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save(product_images=request.data.get('product_images'))
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)

        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        queryset = Add_Product.objects.get(pk=pk)
      
        serializer_class = Add_Your_Prduct_serializer(queryset)
        return Response(serializer_class.data)

    def update(self,request,pk=None):
        queryset = Add_Product.objects.get(pk=pk)
        serializer_class = Add_Your_Prduct_serializer(queryset,data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None):
        queryset = Add_Product.objects.get(pk=pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#===============================================                 ==========================================
class divanbeds_view(viewsets.ViewSet):
    #permission_classes=[IsAuthenticated]

    def list(self,request):
        queryset =Add_Divanbeds.objects.all()
        serializer_class =Add_Your_Prduct_serializer(queryset,many=True)
        #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        return Response(serializer_class.data)

    def create(self,request,pk=None):
        serializer_class =Add_Your_Prduct_serializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)

        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)




#=========================================================multi image==========================
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


########################################=======>>>>> FEETCASTOR VIEW  <<<<<<======#################################################

class Add_Basket_view(viewsets.ViewSet):
    def list(self,request):
        queryset =Add_Basket.objects.all()
        serializer_class =Add_Basket_serializer(queryset,many=True)
        # queryset_list=[]
        # for query_data in query_set:
            
        #     # print(query_data)

        #     queryset_list.append({
        #         "select_color":query_data.select_color,
        #         "select_size":query_data.select_size,
        #         # "storage_option":query_data.storage_option.type,
        #         # "select_feet":query_data.select_feet.type,
        #         # "select_headboard":query_data.select_headboard.type,
        #         # "select_mattresses":query_data.select_mattresses.type,
        #     })
        # print(queryset_list)
        # # serializer_class =Add_Basket_serializer(queryset,many=True)
        # #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        # return Response({"response":queryset_list})
        return Response(serializer_class.data)

    def create(self,request,pk=None):
        serializer_class = Add_Basket_serializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)

        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        queryset = Add_Basket.objects.get(pk=pk)
      
        serializer_class =Add_Basket_serializer(queryset)
        return Response(serializer_class.data)

    def update(self,request,pk=None):
        queryset =Mattress.objects.get(pk=pk)
        serializer_class = Add_Basket_serializer(queryset,data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None):
        queryset = Add_Basket.objects.get(pk=pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


########################################################>>>>>>>>>>>>>>>>>>>>>>>>     <<<<<<<<<<<<<<<<<<<<<<###########################
from collections import namedtuple

Timeline = namedtuple('Timeline', ('Bedsdivan', 'Headboards','Mattresses','FeetCastors','Drawers'))
class ProductListView(viewsets.ViewSet):
     def list(self,request):
        timeline = Timeline(
            Bedsdivan=Add_new_product.objects.all(),
            Headboards=Headboard.objects.all(),
            Mattresses=Mattress.objects.all(),
            FeetCastors=FeetCastor.objects.all(),
            Drawers=Drawers.objects.all(),
        )
        serializer = ProductListSerializer(timeline)
        return Response(serializer.data)
        

####################################### Ottoman ==============================================
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


#==========Florida beds
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


#==========Ambassador Range beds
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
