from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

# Register your models here.
# @admin.register(Add_new_product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('__all__')
#     list_filter = ('category', )
# class ExitAdmin(admin.ModelAdmin):
#      list_display =['description','price','total_exit']

# def total_exit(self, request): 
#     total = Add_new_product.objects.all().aggregate(tot=Sum('price'))['tot']
#     return total
# class ImageAdmin(admin.ModelAdmin):
#     list_display=['id','image']


#=============================== my beds admin ------------------------------------============================


from django.contrib import admin
from .models import *
from nested_admin import NestedModelAdmin, NestedStackedInline, NestedTabularInline


class DrawerTabularInline(NestedStackedInline):
    model = My_Drawers
    extra = 1

class MattressTabularInline(NestedTabularInline):
    model = My_Mattress
    extra = 1

class FeetTabularInline(NestedTabularInline):
    model = My_FeetCastor
    extra = 1

class HeadboardTabularInline(NestedTabularInline):
    model = My_Headboard
    extra = 1




class VariantTabularInline(NestedTabularInline):
    model = My_Variant
    extra = 6
    inlines = [DrawerTabularInline,MattressTabularInline,FeetTabularInline,HeadboardTabularInline ]


class My_BedsdivanAdmin(NestedModelAdmin):
    model=My_DivanBeds
    extra = 1
    inlines = [VariantTabularInline, ]
    #extra = 6

admin.site.register(My_DivanBeds, My_BedsdivanAdmin)







