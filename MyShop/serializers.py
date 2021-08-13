from rest_framework import serializers
from .models import BillingDetails
#from Product.models import *
from Product.serializers import *


class BillingDetails_Serializer(serializers.ModelSerializer):
    class Meta:
        model=BillingDetails
        fields='__all__'


from django.db.models import fields
from django.urls.conf import include
from rest_framework import serializers
from .models import *

from django.contrib.auth import get_user_model
from rest_framework import serializers







class Add_product_Serializer(serializers.ModelSerializer):
    
    product_image=serializers.SerializerMethodField()
    Headboard_image=serializers.SerializerMethodField()
    storage_file=serializers.SerializerMethodField()
    mattresses_image=serializers.SerializerMethodField()
    price=serializers.SerializerMethodField()

    def get_price(self,obj):
        total = obj.price+obj.Headboard_price+obj.storage_price+obj.mattresses_price
        return total


    class Meta:
        model=Add_new_product
        fields='__all__'
        # exclude=['active']
    def get_product_image(self,obj):
        return f'http://127.0.0.1:8000/media/{obj.product_image}'

    def get_Headboard_image(self,obj):
        return f'http://127.0.0.1:8000/media/{obj.Headboard_image}'

    def get_storage_file(self,obj):
        return f'http://127.0.0.1:8000/media/{obj.storage_file}'
    def get_mattresses_image(self,obj):
        return f'http://127.0.0.1:8000/media/{obj.mattresses_image}'


    # def create(self, validated_date):
    #     images = self.context['request'].FILES.getlist('images')
    #     for image in list(images):
    #         m2 = PostImage(post=m1, images= image)

    #         m2.save()
####################### Divan beds Serializer for end user####################
class Divanbed_Serializer(serializers.ModelSerializer):
    
    product_image=serializers.SerializerMethodField()
    

    class Meta:
        model=Add_new_product
        #fields='__all__'
        fields=['id','product_type','product_name','Description','product_image','size','Color','compare_Price','price','created_at']
        # exclude=['active']
    def get_product_image(self,obj):
        return f'http://127.0.0.1:8000/media/{obj.product_image}'

class Add_product_size_Serializer(serializers.ModelSerializer):
    
    class Meta:
        model=Add_new_product
        fields=('size',)


class Headboard_Serializer(serializers.ModelSerializer):
    headboard_image=serializers.SerializerMethodField()
    size=Add_product_size_Serializer(many=False)
    class Meta:
        model=Headboard
        fields='__all__'
    def get_headboard_image(self,obj):
        return f'http://127.0.0.1:8000/media/{obj.headboard_image}'

class Mattresses_Serializer(serializers.ModelSerializer):
    mattresses_image=serializers.SerializerMethodField()
    size=Add_product_size_Serializer(many=False)
    class Meta:
        model=Mattress
        fields='__all__'
    def get_mattresses_image(self,obj):
        return f'http://127.0.0.1:8000/media/{obj.mattresses_image}'




class Drawer_Serializer(serializers.ModelSerializer):
    size=Add_product_size_Serializer(many=False)
     #size=serializers.SerializerMethodField()

    class Meta:
        model=Drawers
        fields='__all__'

    def get_size(self,obj):
        return obj.size

class FeetCastor_Serializer(serializers.ModelSerializer):
    class Meta:
        model=FeetCastor
        fields='__all__'

#######################============>>>>>>>>>>>>> Add Basket serializer >>>>>>>>>============########################################



########################## Customize beds Home page Serializrer #############################

class Add_Basket_serializer(serializers.ModelSerializer):
    # select_size= Add_new_product.objects.getlist(size=size)
    select_size= Divanbed_Serializer(many=False)
    storage_option= Drawer_Serializer(many=False)
    select_feet= FeetCastor_Serializer(many=False)
    select_headboard= Headboard_Serializer(many=False)
    select_mattresses= Mattresses_Serializer(many=False)
    # elect_size= Add_product_Serializer(many=False)

    class Meta:
        model=Add_Basket
        fields=['select_color','select_size','storage_option','select_feet','select_headboard','select_mattresses']
        
    #     #fields = ('id', 'equipment_type',)
    #     

        def create(self, validated_data):
            select_size = validated_data.pop('select_size')
            storage_option = validated_data.pop('storage_option')
            add_Basket = Add_Basket.objects.create(**validated_data)
            return add_Basket
############################################## List of all products ##########################################
class ProductListSerializer(serializers.Serializer):
    Bedsdivan=Add_product_Serializer(many=True)
    Headboards=Headboard_Serializer(many=True)
    Mattresses=Mattresses_Serializer(many=True)
    Drawers=Drawer_Serializer(many=True)
    FeetCastors=FeetCastor_Serializer(many=True)


############
class All_Beds_serializer(serializers.ModelSerializer):
    #beds_category=All_Beds.objects.filter(beds_category='Ottoman Beds')
    beds_image=serializers.SerializerMethodField()
      
    class Meta:
        model=All_Beds
        fields=['beds_category','product_name','size','Color','beds_image','price','compare_Price']

    def get_beds_image(self,obj):
        return f'http://127.0.0.1:8000/media/{obj.beds_image}'


#########################>>>>>>>>>>>>>>>>.Others Product serializer<<<<<<<<<<<<<<<<<<<<<<<<$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

class Other_Beds_serializer(serializers.ModelSerializer):
    #beds_category=All_Beds.objects.filter(beds_category='Ottoman Beds')
    beds_image=serializers.SerializerMethodField()
      
    class Meta:
        model=OTHERS
        fields=['other_category','product_type','size','Color','beds_image','price','compare_Price','material_type']

    def get_beds_image(self,obj):
        return f'http://127.0.0.1:8000/media/{obj.beds_image}'



#==================================image serial============================

# class ImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model= Image
#         fields=['image']






