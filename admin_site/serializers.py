#from bedsdivan_admin.Product.models import Add_new_product, Drawers, Headboard, Mattress
from .models import *
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
