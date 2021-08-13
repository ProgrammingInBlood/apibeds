from django.contrib import admin
from django.db.models import fields
from .models import *

# Register your models here.
# @admin.register(Add_new_product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('__all__')
#     list_filter = ('category', )
# class ExitAdmin(admin.ModelAdmin):
#      list_display =['description','price','total_exit']

def total_exit(self, request): 
    total = Add_new_product.objects.all().aggregate(tot=Sum('price'))['tot']
    return total
class ImageAdmin(admin.ModelAdmin):
    list_display=['id','image']

from nested_admin import NestedModelAdmin, NestedStackedInline, NestedTabularInline
#import nested_admin



#============================================= test2 admin =============================
# class ColorTabularInline(NestedTabularInline):
#     model = Color
#     extra = 1




# class VariantTabularInline(NestedTabularInline):
#     model = Add_Variation
#     extra = 6
#     inlines = [ColorTabularInline]


# class My_BedsdivanAdmin(NestedModelAdmin):
#     model=Add_New_Products
#     extra = 1
#     inlines = [VariantTabularInline, ]
#     #extra = 6

# admin.site.register(Add_New_Products, My_BedsdivanAdmin)




# class ColorInline(admin.StackedInline):
#     model = Color
#     #sortable_field_name =('color',)
#     #extra=1
  

# class VariationInline(admin.StackedInline):
#     model = Add_Variation
#     #sortable_field_name = "size"
#     inlines = [ColorInline]
#     extra=5


# class ProductInline(admin.ModelAdmin):
#     inlines = [VariationInline]
    

# admin.site.register(Add_New_Products, ProductInline)
# admin.site.register(Color)
#admin.site.register(VariationInline)
#admin.site.register(Add_Variation,VariationInline)
#============================================================Add_New_Products================================


# class DrawerTabularInline(NestedStackedInline):
#     model = My_Drawers
#     extra = 1

# class MattressTabularInline(NestedTabularInline):
#     model = My_Mattress
#     extra = 1

# class FeetTabularInline(NestedTabularInline):
#     model = My_FeetCastor
#     extra = 1

# class HeadboardTabularInline(NestedTabularInline):
#     model = My_Headboard
#     extra = 1




# class VariantTabularInline(NestedTabularInline):
#     model = My_Variant
#     extra = 6
#     inlines = [DrawerTabularInline,MattressTabularInline,FeetTabularInline,HeadboardTabularInline ]


# class My_BedsdivanAdmin(NestedModelAdmin):
#     model=My_DivanBeds
#     extra = 1
#     inlines = [VariantTabularInline, ]
#     #extra = 6

# admin.site.register(My_DivanBeds, My_BedsdivanAdmin)

# class ColorInline(NestedTabularInline):
#     model = Color
#     #fields=('color','color1')
#     fk_name = "color"
#     extra=1

# class Storage_color_Inline(NestedTabularInline):
#     model = Color
#     #fields=('color','color1')
#     fk_name = "Storage_color"
#     extra=1

# class Feet_color_Inline(NestedTabularInline):
#     model = Color
#     #fields=('color','color1')
#     fk_name = "Feet_color"
#     extra=1
# class Headboard_color_Inline(NestedTabularInline):
#     model = Color
#     #fields=('color','color1')
#     fk_name = "Headboard_color"
#     extra=1
# class Mattress_color_Inline(NestedTabularInline):
#     model = Color
#     #fields=('color','color1')
#     fk_name = "Mattress_color"
#     extra=1

# class VariationInline(NestedStackedInline):
#     model = Add_Variation
   
#     inlines = [ColorInline,Storage_color_Inline,Feet_color_Inline,Headboard_color_Inline,Mattress_color_Inline,]
#     extra=6


# class ProductInline(NestedModelAdmin):
#     inlines = [VariationInline]
    

# admin.site.register(Add_New_Products, ProductInline)



#========================================== test admin ====================

class ColorInline(NestedStackedInline):
    model = Color
    #fields=('color','color1')
    fk_name = "color"
    extra=1

class Storage_color_Inline(NestedStackedInline):
    model = Color
    #fields=('color','color1')
    fk_name = "Storage_color"
    extra=1

class Feet_color_Inline(NestedStackedInline):
    model = Color
    #fields=('color','color1')
    fk_name = "Feet_color"
    extra=1
class Headboard_color_Inline(NestedStackedInline):
    model = Color
    #fields=('color','color1')
    fk_name = "Headboard_color"
    extra=1
class Mattress_color_Inline(NestedStackedInline):
    model = Color
    #fields=('color','color1')
    fk_name = "Mattress_color"
    extra=1

class VariationInline(NestedStackedInline):
    model = Add_Variation
   
    inlines = [ColorInline,Storage_color_Inline,Feet_color_Inline,Headboard_color_Inline,Mattress_color_Inline,]
    extra=6


class ProductInline(NestedModelAdmin):
    inlines = [VariationInline]
    

admin.site.register(Add_New_Products, ProductInline)



#=========================== Add  =================================================================================

# class Admin_Color(admin.StackedInline):
#     model=Color
#     extra=5
#     fields = ['color','color1','grey_linen','silver_crushed_velvet','white_crushed_velvet','Blue_plus_velvet','grey_seude','charcoal_chenille','pattern_cream','purple_velvet',
#         'black_leather','black_crushed_velvet','champagne_crushed_velvet','gun_grey_crushed_velvet']
    

# class Admin_variation(admin.StackedInline):
#     model=Add_Variation
#     extra=5
#     fields = ['type','size','base_price','grey_linen','silver_crushed_velvet','white_crushed_velvet','Blue_plus_velvet','grey_seude','charcoal_chenille','Headboard_images','Headboard_Price','Feet_images','Feet_Price','Storage_images',
#                  'Storage_Price','mattresses_images','mattresses_Price']
#     # list_filter = [
                   
                   
                   
#     #                'size']
#     inlines=[Admin_Color]





# @admin.register(Add_New_Products)
# class Admin_Add_New_Product(admin.ModelAdmin):
#     #model=Add_new_product
#     fields= ['product_name','product_images','Description','compare_Price','price']

#     # list_filter = ['product_type',
                   
#     #                'compare_Price',
                   
#     #                'price']
#     # search_fields = [
        
#     #     'product_type'
#     # ]
#     # actions = []
#     inlines=[Admin_variation]
    #extra=1





class Admin_variant(admin.StackedInline):
    model=Add_Variant
    extra=5
    fields = ['size','base_price','grey_linen','silver_crushed_velvet','white_crushed_velvet','Blue_plus_velvet','grey_seude','charcoal_chenille',
    'pattern_cream','purple_velvet','black_leather','black_crushed_velvet',
    'champagne_crushed_velvet','gun_grey_crushed_velvet','Headboard_images','Headboard_Price','Storage_images',
                 'Storage_Price','mattresses_images','mattresses_Price']
    list_filter = [
                   'product_images',
                   
                   
                   'size','color']
@admin.register(Add_Product)
class Admin_Add_product(admin.ModelAdmin):
    #model=Add_new_product
    fields= ['product_name','product_images','Description','compare_Price','price']

    # list_filter = ['product_type',
                   
    #                'compare_Price',
                   
    #                'price']
    # search_fields = [
        
    #     'product_type'
    # ]
    # actions = []
    inlines=[Admin_variant]




    
    





# @admin.register(Add_product)
# class Admin_Add_product(admin.ModelAdmin):
#     #model=Add_new_product
#     fields= ['product_name','Description','compare_Price','price']

    # list_filter = ['product_type',



#admin.site.register(Add_new_product)
admin.site.register(Add_new_product)
admin.site.register(category)
admin.site.register(Headboard)
admin.site.register(Mattress)
admin.site.register(Drawers)
admin.site.register(FeetCastor)
admin.site.register(Add_Basket)
admin.site.register(All_Beds)
admin.site.register(OTHERS)
admin.site.register(Image,ImageAdmin)
