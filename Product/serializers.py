from typing import Pattern
from django.db.models import fields
from django.urls.conf import include
from rest_framework import serializers
from rest_framework.fields import ReadOnlyField
from .models import *

from django.contrib.auth import get_user_model
from rest_framework import serializers


#======================================================== Add NEw beds Serializer for nested  ========================================= 
class Color_Serializers(serializers.ModelSerializer):
    grey_linen=serializers.SerializerMethodField()
    silver_crushed_velvet=serializers.SerializerMethodField()
    white_crushed_velvet=serializers.SerializerMethodField()
    Blue_plus_velvet=serializers.SerializerMethodField()
    # black_crushed_velvet=serializers.SerializerMethodField()
    grey_seude=serializers.SerializerMethodField()
    charcoal_chenille=serializers.SerializerMethodField()
    pattern_cream=serializers.SerializerMethodField()
      
    purple_velvet=serializers.SerializerMethodField()
   # white_crushed_velvet=serializers.SerializerMethodField()
    #Blue_plus_velvet=serializers.SerializerMethodField()
    black_crushed_velvet=serializers.SerializerMethodField()
    black_leather=serializers.SerializerMethodField()
    champagne_crushed_velvet=serializers.SerializerMethodField()
    gun_grey_crushed_velvet=serializers.SerializerMethodField()

    class Meta:
        model=Color
        fields=['grey_linen','silver_crushed_velvet','white_crushed_velvet','Blue_plus_velvet','grey_seude','charcoal_chenille','pattern_cream','purple_velvet',
        'black_leather','black_crushed_velvet','champagne_crushed_velvet','gun_grey_crushed_velvet']
    read_only_fields = (
        'color','color1'
    )


    def get_grey_linen(self,obj):
        return f'http://127.0.0.1:8000/media/{obj.grey_linen}'

    def get_silver_crushed_velvet(self,obj):
        return f'http://127.0.0.1:8000/media/{obj.silver_crushed_velvet}'

    def get_white_crushed_velvet(self,obj):
        return f'http://127.0.0.1:8000/media/{obj.white_crushed_velvet}'
    def get_Blue_plus_velvet(self,obj):
        return f'http://127.0.0.1:8000/media/{obj.Blue_plus_velvet}'
    def get_black_crushed_velvet(self,obj):
        return f'http://127.0.0.1:8000/media/{obj.black_crushed_velvet}'

    def get_grey_seude(self,obj):
        return f'http://127.0.0.1:8000/media/{obj.grey_seude}'
    def get_charcoal_chenille(self,obj):
        return f'http://127.0.0.1:8000/media/{obj.charcoal_chenille}'


    def get_pattern_cream(self,obj):
        return f'http://127.0.0.1:8000/media/{obj.pattern_cream}'

    def get_purple_velvet(self,obj):
        return f'http://127.0.0.1:8000/media/{obj.purple_velvet}'

    def get_black_leather(self,obj):
        return f'http://127.0.0.1:8000/media/{obj.white_crushed_velvet}'
    def get_champagne_crushed_velvet(self,obj):
        return f'http://127.0.0.1:8000/media/{obj.champagne_crushed_velvet}'
    def get_gun_grey_crushed_velvet(self,obj):
        return f'http://127.0.0.1:8000/media/{obj. gun_grey_crushed_velvet}'

   




class Add_Variant_Serializer(serializers.ModelSerializer):
    #type=serializers.CharField(required=False)
    #id=serializers.CharField(required=False)
    color=Color_Serializers(many=True)
    Storage_color=Color_Serializers(many=True)
    # color2=Color_Serializers(many=True)
    Feet_color=Color_Serializers(many=True)
    Headboard_color=Color_Serializers(many=True)
    Mattress_color=Color_Serializers(many=True)
    
    # Headboard_images=serializers.SerializerMethodField()
    # Storage_images=serializers.SerializerMethodField()
    # mattresses_images=serializers.SerializerMethodField()
    # grey_linen=serializers.SerializerMethodField()
    # silver_crushed_velvet=serializers.SerializerMethodField()
    # white_crushed_velvet=serializers.SerializerMethodField()
    # Blue_plus_velvet=serializers.SerializerMethodField()
    # # black_crushed_velvet=serializers.SerializerMethodField()
    # grey_seude=serializers.SerializerMethodField()
    # charcoal_chenille=serializers.SerializerMethodField()
    price=serializers.SerializerMethodField()
    # Headboard_Price=serializers.SerializerMethodField()
    # Storage_Price=serializers.SerializerMethodField()
    # mattresses_Price=serializers.SerializerMethodField()



    def get_price(self,obj):
        total= obj.base_price+obj.Headboard_Price+obj.Storage_Price+obj.mattresses_Price
        return total
    class Meta:
        model =Add_Variation
        fields= ['size','color','Headboard_images','Headboard_Price','Headboard_color','Storage_images','Storage_color','Storage_Price','mattresses_images','mattresses_Price','Mattress_color','Feet_color','price']
       # depth=1

    read_only_fields = (
        'type',
        'color1'
    )
    
    # def get_color1(self,obj):
    #     return {obj.color}

    def get_Headboard_images(self,obj):
        return f'http://127.0.0.1:8000/media/{obj.Headboard_images}'

    def get_Storage_images(self,obj):
        return f'http://127.0.0.1:8000/media/{obj.Storage_images}'
    def get_mattresses_images(self,obj):
        return f'http://127.0.0.1:8000/media/{obj.mattresses_images}'
    def get_grey_linen(self,obj):
        return f'http://127.0.0.1:8000/media/{obj.grey_linen}'

    def get_silver_crushed_velvet(self,obj):
        return f'http://127.0.0.1:8000/media/{obj.silver_crushed_velvet}'

    def get_white_crushed_velvet(self,obj):
        return f'http://127.0.0.1:8000/media/{obj.white_crushed_velvet}'
    def get_Blue_plus_velvet(self,obj):
        return f'http://127.0.0.1:8000/media/{obj.Blue_plus_velvet}'
    # def get_black_crushed_velvet(self,obj):
    #     return f'http://127.0.0.1:8000/media/{obj.black_crushed_velvet}'

    def get_grey_seude(self,obj):
        return f'http://127.0.0.1:8000/media/{obj.grey_seude}'
    def get_charcoal_chenille(self,obj):
        return f'http://127.0.0.1:8000/media/{obj.charcoal_chenille}'

    

class Add_New_Prduct_serializer(serializers.ModelSerializer):
    type=Add_Variant_Serializer(many=True)
    product_images  =serializers.SerializerMethodField()
    #type=serializers.StringRelatedField(many=True,read_only=True)

    class Meta:
        model=Add_New_Products
        fields=['product_name','product_images','Description','compare_Price','price','type']

    def get_product_images(self,obj):
        return f'http://127.0.0.1:8000/media/{obj.product_images}'


    #=====================
    def create(self, validated_data):
        type_data = validated_data.pop('type')
        add_new_product_data = Add_New_Products.objects.create(**validated_data)
        # choice_set_serializer = self.fields['type']
        for types_data in type_data:
            
            Add_Variant.objects.create(type=add_new_product_data,**types_data)
        return add_new_product_data

    






class Add_Bedsvariant_Serializer(serializers.ModelSerializer):
    #type=serializers.CharField(required=False)
    #id=serializers.CharField(required=False)
    Headboard_images=serializers.SerializerMethodField()
    Storage_images=serializers.SerializerMethodField()
    mattresses_images=serializers.SerializerMethodField()
    grey_linen=serializers.SerializerMethodField()
    silver_crushed_velvet=serializers.SerializerMethodField()
    white_crushed_velvet=serializers.SerializerMethodField()
    Blue_plus_velvet=serializers.SerializerMethodField()
    black_crushed_velvet=serializers.SerializerMethodField()
    grey_seude=serializers.SerializerMethodField()
    charcoal_chenille=serializers.SerializerMethodField()
    purple_velvet=serializers.SerializerMethodField()
    champagne_crushed_velvet=serializers.SerializerMethodField()
    #base_price=serializers.SerializerMethodField()

    # def get_base_price(self,obj):
    #     total= obj.base_price+obj.Headboard_Price+obj.Storage_Price+obj.mattresses_Price
    #     return total

    # base_price=serializers.SerializerMethodField()

    # def get_base_price(self,obj):
    #     Exception Value:	




    class Meta:
        #model=Add_Variant
        model =Add_BedsVariant
        fields= ['size','base_price','grey_linen','silver_crushed_velvet','white_crushed_velvet','Blue_plus_velvet','grey_seude','charcoal_chenille',
    'pattern_cream','purple_velvet','black_leather','black_crushed_velvet',
    'champagne_crushed_velvet','gun_grey_crushed_velvet','Headboard_images','Headboard_Price','Storage_images','Storage_Price','mattresses_images','mattresses_Price']
       # depth=1
    # def get_base_price(self,obj):
    #     total= obj.base_price+obj.Headboard_Price+obj.Storage_Price+obj.mattresses_Price
    #     return total

    # def get_price(self,obj):
    #     total = obj.base_price+obj.Headboard_price+obj.storage_price+obj.mattresses_price
    #     return total

    # def get_base_price(self,obj):
    #     total = obj.base_price+obj.Headboard_Price +obj.Storage_Price+obj.mattresses_Price 
    #     return total


   

    def get_Headboard_images(self,obj):
        return f'http://127.0.0.1:8000/media/{obj.Headboard_images}'

    def get_Storage_images(self,obj):
        return f'http://127.0.0.1:8000/media/{obj.Storage_images}'
    def get_mattresses_images(self,obj):
        return f'http://127.0.0.1:8000/media/{obj.mattresses_images}'
    def get_grey_linen(self,obj):
        return f'http://127.0.0.1:8000/media/{obj.grey_linen}'

    def get_silver_crushed_velvet(self,obj):
        return f'http://127.0.0.1:8000/media/{obj.silver_crushed_velvet}'

    def get_white_crushed_velvet(self,obj):
        return f'http://127.0.0.1:8000/media/{obj.white_crushed_velvet}'
    def get_Blue_plus_velvet(self,obj):
        return f'http://127.0.0.1:8000/media/{obj.Blue_plus_velvet}'
    def get_black_crushed_velvet(self,obj):
        return f'http://127.0.0.1:8000/media/{obj.black_crushed_velvet}'

    def get_grey_seude(self,obj):
        return f'http://127.0.0.1:8000/media/{obj.grey_seude}'
    def get_charcoal_chenille(self,obj):
        return f'http://127.0.0.1:8000/media/{obj.charcoal_chenille}'

    def get_purple_velvet(self,obj):
        return f'http://127.0.0.1:8000/media/{obj.purple_velvet}'
    def get_champagne_crushed_velvet(self,obj):
        return f'http://127.0.0.1:8000/media/{obj.champagne_crushed_velvet}'

#================================= Add product 5 july =================
class Add_Bedsdivanbed_serializer(serializers.ModelSerializer):
    #type=Add_Variant_Serializer(many=True)
    product_images=serializers.SerializerMethodField()
    #type=serializers.StringRelatedField(many=True,read_only=True)
    
    class Meta:
       # model=Add_Product
        model=Add_Divanbeds
        fields=['product_name','product_images','Description','compare_Price','price']

    # def get_price(self,obj):
    #     total= obj.base_price+obj.Headboard_Price+obj.Storage_Price+obj.mattresses_Price
        # return total

    def get_product_images(self,obj):
        return f'http://127.0.0.1:8000/media/{obj.product_images}'


#=================================== Add variant serializer=====





#============= latest Add product serializer=======

class Add_Variant_Serializer(serializers.ModelSerializer):
    #type=serializers.CharField(required=False)
    #id=serializers.CharField(required=False)
    Headboard_images=serializers.SerializerMethodField()
    Storage_images=serializers.SerializerMethodField()
    mattresses_images=serializers.SerializerMethodField()
    grey_linen=serializers.SerializerMethodField()
    silver_crushed_velvet=serializers.SerializerMethodField()
    white_crushed_velvet=serializers.SerializerMethodField()
    Blue_plus_velvet=serializers.SerializerMethodField()
    black_crushed_velvet=serializers.SerializerMethodField()
    grey_seude=serializers.SerializerMethodField()
    charcoal_chenille=serializers.SerializerMethodField()
    purple_velvet=serializers.SerializerMethodField()
    champagne_crushed_velvet=serializers.SerializerMethodField()
    #base_price=serializers.SerializerMethodField()

    # def get_base_price(self,obj):
    #     total= obj.base_price+obj.Headboard_Price+obj.Storage_Price+obj.mattresses_Price
    #     return total

    # base_price=serializers.SerializerMethodField()

    # def get_base_price(self,obj):
    #     total = obj.base_price +obj.Headboard_Price +obj.Storage_Price +obj.mattresses_Price
    #     return total





    class Meta:
        model =Add_Variant
        fields= ['size','base_price','grey_linen','silver_crushed_velvet','white_crushed_velvet','Blue_plus_velvet','grey_seude','charcoal_chenille',
    'pattern_cream','purple_velvet','black_leather','black_crushed_velvet',
    'champagne_crushed_velvet','gun_grey_crushed_velvet','Headboard_images','Headboard_Price','Storage_images','Storage_Price','mattresses_images','mattresses_Price']
       # depth=1
    # def get_base_price(self,obj):
    #     total= obj.base_price+obj.Headboard_Price+obj.Storage_Price+obj.mattresses_Price
    #     return total

    # def get_price(self,obj):
    #     total = obj.base_price+obj.Headboard_price+obj.storage_price+obj.mattresses_price
    #     return total

    # def get_base_price(self,obj):
    #     total = obj.base_price+obj.Headboard_Price +obj.Storage_Price+obj.mattresses_Price 
    #     return total


   

    def get_Headboard_images(self,obj):
        return f'http://127.0.0.1:8000/media/{obj.Headboard_images}'

    def get_Storage_images(self,obj):
        return f'http://127.0.0.1:8000/media/{obj.Storage_images}'
    def get_mattresses_images(self,obj):
        return f'http://127.0.0.1:8000/media/{obj.mattresses_images}'
    def get_grey_linen(self,obj):
        return f'http://127.0.0.1:8000/media/{obj.grey_linen}'

    def get_silver_crushed_velvet(self,obj):
        return f'http://127.0.0.1:8000/media/{obj.silver_crushed_velvet}'

    def get_white_crushed_velvet(self,obj):
        return f'http://127.0.0.1:8000/media/{obj.white_crushed_velvet}'
    def get_Blue_plus_velvet(self,obj):
        return f'http://127.0.0.1:8000/media/{obj.Blue_plus_velvet}'
    def get_black_crushed_velvet(self,obj):
        return f'http://127.0.0.1:8000/media/{obj.black_crushed_velvet}'

    def get_grey_seude(self,obj):
        return f'http://127.0.0.1:8000/media/{obj.grey_seude}'
    def get_charcoal_chenille(self,obj):
        return f'http://127.0.0.1:8000/media/{obj.charcoal_chenille}'

    def get_purple_velvet(self,obj):
        return f'http://127.0.0.1:8000/media/{obj.purple_velvet}'
    def get_champagne_crushed_velvet(self,obj):
        return f'http://127.0.0.1:8000/media/{obj.champagne_crushed_velvet}'


    

class Add_Your_Prduct_serializer(serializers.ModelSerializer):
    type=Add_Variant_Serializer(many=True)
    product_images=serializers.SerializerMethodField()
    #type=serializers.StringRelatedField(many=True,read_only=True)
    
    class Meta:
        model=Add_Product
        fields=['product_name','product_images','Description','compare_Price','price','type']

    # def get_price(self,obj):
    #     price= obj.base_price+obj.Headboard_Price+obj.Storage_Price+obj.mattresses_Price
    #     return price

    def get_product_images(self,obj):
        return f'http://127.0.0.1:8000/media/{obj.product_images}'

    def create(self, validated_data):
        type_data = validated_data.pop('type')
        add_new_product_data = Add_Product.objects.create(**validated_data)
        # choice_set_serializer = self.fields['type']
        for types_data in type_data:
            
            Add_Variant.objects.create(type=add_new_product_data,**types_data)
        return add_new_product_data
   




#==============================old serializers===================


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


########################################################### All_beds serializers     ##################################################

#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&>>>>>>>>>>>>>>>>Ottoman serializer<<<<<<<<<<<<<<<<<#####$$$$$$$$$$$$$$$$$$$

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


