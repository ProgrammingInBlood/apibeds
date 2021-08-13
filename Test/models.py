from django.db import models

# Create your models here.


from functools import total_ordering
from django.conf import settings
from django.core.validators import ProhibitNullCharactersValidator
from django.db.models.deletion import CASCADE
from django.shortcuts import reverse
from django.db import models
from django.db.models.enums import Choices
from django.db.models.fields import NullBooleanField
from colorfield.fields import ColorField
from multiselectfield import MultiSelectField
from django.db.models import Avg, Max, Min, Sum
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType




#Create your models here.

owner = models.ForeignKey('auth.User', related_name='dashboard', on_delete=models.CASCADE)
highlighted = models.TextField()

#class MyModel(models.Model):

COLOR_CHOICES = [
        ("#FFFFFF", "white"),
        ("#000000", "black"),
        ("#FFB978","Red" ),
        ("#950F2F", "Yellow"),
        ("#BEE093", "Blue"),
        ("#28803A", "Green"),
        ("#806F1A", "Golden"),
        ("#7A804F", "Silver"),
        ("#2F806D", "Sky"),
        ("#447A80", "Cream-Color"),
        ("#80514C", "gun-gray"),
        ("#107780", "champagne-white"),
        ("#778026", "k"),
        ("#000000", "l"),
    ]
COLOR=[
    ('grey linen','grey linen'),
    ('silver crushed velvet','silver crushed velvet'),
    ('white crushed velvet','white crushed velvet'),
    ('Blue plus velvet','Blue plus velvet'),
    ('grey seude ','grey seude'),
    ('charcoal chenille','charcoal chenille'),
    ('pattern cream','pattern cream'),
    ('purple velvet','purple velvet'),
    ('white crushed velvet','white crushed velvet'),
    ('black leather','black leather'),
    ('black crushed velvet','black crushed velvet'),
    ('champagne crushed velvet ','champagne crushed velvet'),
    ('gun grey crushed velvet ','gun grey crushed velvet'),
    

]
Color1=(
     ('grey linen','grey linen'),
     ('grey seude ','grey seude'),
     ('charcoal chenille','charcoal chenille'),
     ('black crushed velvet','black crushed velvet'),

)



option=(('1', 'A'),('2', 'B'),('3', 'C'),)

size=(
    ("2FT 6",'2FT 6"-small'),
   
    ("3FT",'3FT-single'),
    ("4FT","4FT-Small-double"),
    ("4FT 6",'4FT 6"-Double'),
    ("5FT","5FT-king"),
    ("6FT","6FT-super-king"),
    ("extra","extra"),
    ("extra","extra")
)

beds_category=(
    ('Divan Beds','Divan Beds'),
    ('Ottoman Beds','Ottoman Beds'),
    ('Kids Beds','Kids Beds'),
    ('Leather Beds','Leather Beds'),
    ('Nevada Beds','Nevada Beds'),
    ('Storage Beds','Storage Beds'),
    ('Sleigh Beds',(
        ('Florida Bed Range','Florida Bed Range'),
        ('Ambassador Range','Ambassador Range'),
        ('Kendall Bed','Kendal Bed'),
        ('Manoco Range','Manoco Range'),
        ('Royal Beds Range','Royal Beds Range'),
        ('Swan Bed Range','Swan Bed Range'),
        ('Wing Bed Range','Wing Bed Range'),
        ('Winchester Bed','Winchester Bed'),
        
    )),

)


divanbeds_type=(
    ('Linen Fabric Divan Beds'),
    ('Valvet Fabric Divan Beds'),
    ('Seude Fabric Divan Beds'),
    ('Low Divan Beds'),
    ('Leather Divan Beds'),
   
)

Mattress_type=(
    ('No Mattress','No Mattress'),
    ('Orthopedic Mattress','Orthopedic Mattress'),
    ('1500 Pocket Pillow Top Mattress','1500 Pocket Pillow Top Mattress'),
    ('1500 Pocket (tinsel Top)','1500 Pocket (tinsel Top)'),
)

Drawers_type=(
    ('no-drawers','no-drawers'),
    ('Two Drawer Same Side','Two Drawer Same Side'),
    ('Two-Drawer Foot end','wo-Drawer Foot end'),
    ('4 Drawers','4 Drawers'),
)




product_types = (
    ('BEDS','BEDS'),
    ('OTHER','OTHER'),
    ('Rating','Rating')
)

headboard_type=(
    ('No Headboard','No Headboard'),
    ('26 Inch Diamond Button Cube Headboard','26 Inch Diamond Button Cube Headboard'),
    ('26 Inch Matching Button Cube Headboard','26 Inch Matching Button Cube Headboard'),
    ('48 Inch Floor Standing Diamond Cube Headboard','48 Inch Floor Standing Diamond Cube Headboard'),
    ('48 Inch Floor Standing Matching Button Cube Headboard','48 Inch Floor Standing Matching Button Cube Headboard'),
)


feet_caster=(
    ('free Caster wheel','free Caster wheel'),
    ('chrome Gliders ','Chrome Gliders'),
   
)

class category(models.Model):
    title=models.CharField(max_length=50)

    def __str__(self):
        return self.title

    
    class Meta:
        verbose_name_plural='Categories'



    



  
#==================================================================new product model =========================================================Focus ===========

class My_DivanBeds(models.Model):
    
    product_name    = models.CharField(max_length=50,default='divanbeds',null=True,blank=True)
   # size=models.CharField(choices=size,blank=True,null=True,max_length=200)
    Description      = models.TextField(max_length=500,null=True,blank=True)


    def __str__(self):
        return f"{self.product_name}"

class My_Variant(models.Model):
    
    product = models.ForeignKey(My_DivanBeds,on_delete=models.CASCADE)
    size=models.CharField(choices=size,blank=True,null=True,max_length=200)
   
    #compare_Price = models.DecimalField(decimal_places=2,max_digits=50,default=00.00)
    price = models.DecimalField(decimal_places=2,max_digits=50,default=00.00)
    color= MultiSelectField(choices=Color1,null=True,blank=True)
    def __str__(self):
        return f"{self.size}-{self.product.product_name}£{self.price}"

class My_Drawers(models.Model):
    size = models.ForeignKey(My_Variant,on_delete=models.CASCADE,default="no Drawer")
    type=models.CharField(choices=Drawers_type,max_length=200)
    color= MultiSelectField(choices=Color1,null=True,blank=True)
    price = models.IntegerField(null=True,blank=True)
    def __str__(self):
        return f"{self.type}-£{self.price}"

class My_FeetCastor(models.Model):
    size = models.ForeignKey(My_Variant,on_delete=models.CASCADE,blank=True,null=True)
    type = models.CharField(choices=feet_caster,max_length=200)
    price = models.IntegerField(null=True,blank=True)
    def __str__(self):
        return f"{self.type}-{self.price}"



class My_Headboard(models.Model):
    size=models.ForeignKey(My_Variant,on_delete=models.CASCADE,blank=True,null=True)
    type = models.CharField(choices=headboard_type,max_length=300,blank=True,null=True)
    price = models.IntegerField(null=True,blank=True)
    color= MultiSelectField(choices=Color1,null=True,blank=True)
   
    def __str__(self):
        return f"{self.type}-£{self.price}"

class My_Mattress(models.Model):
    size=models.ForeignKey(My_Variant,on_delete=models.CASCADE,default="No Mattress")
    mattaress_type = models.CharField(choices=Mattress_type,max_length=500)
    #mattresses_image = models.ImageField(upload_to='mattaress',blank=True, null=True,default='no image')
    price = models.IntegerField(null=True,blank=True)
  
    color= MultiSelectField(choices=Color1,null=True,blank=True)
    def __str__(self):
        return f"{self.size}-{self.mattaress_type}-£{self.price}"


# class Color1(models.Model):

#     variant=models.ForeignKey(My_Variant,on_delete=models.CASCADE,default=False,related_name='variant')
#    # mybeds=models.ForeignKey(My_DivanBeds,on_delete=models.CASCADE,default=False,related_name='my_beds')
#     drawer=models.ForeignKey(My_Drawers,on_delete=models.CASCADE,default=False,related_name='drawer')
#     head=models.ForeignKey(My_Headboard,on_delete=models.CASCADE,default=False,related_name='head')
#     mattres=models.ForeignKey(My_Mattress,on_delete=models.CASCADE,default=False,related_name='mattres')




#     grey_linen=models.ImageField(upload_to='Bedsdivan/grey_linen/',null=True,blank=True)
#    # silver_crushed_velvet=models.ImageField(upload_to='Bedsdivan/silver_crushed_velvet/',null=True,blank=True)
#    # white_crushed_velvet=models.ImageField(upload_to='Bedsdivan/white_crushed_velvet/',null=True,blank=True)
#     #Blue_plus_velvet=models.ImageField(upload_to='Bedsdivan/Blue_plus_velvet/',null=True,blank=True)
#     grey_seude =models.ImageField(upload_to='Bedsdivan/grey_seude/',null=True,blank=True)
#     charcoal_chenille=models.ImageField(upload_to='Bedsdivan/charcoal_chenille/',null=True,blank=True)
#    # pattern_cream=models.ImageField(upload_to='Bedsdivan/pattern_cream/',null=True,blank=True)
#     #purple_velvet=models.ImageField(upload_to='Bedsdivan/purple_velvet/',null=True,blank=True)
#     #white_crushed_velvet=models.ImageField(upload_to='Bedsdivan/white_crushed_velvet/',null=True,blank=True)
#     #black_leather=models.ImageField(upload_to='Bedsdivan/black_leather/',null=True,blank=True)
#     black_crushed_velvet=models.ImageField(upload_to='Bedsdivan/black_crushed_velvet/',null=True,blank=True)
#    # champagne_crushed_velvet=models.ImageField(upload_to='Bedsdivan/champagne_crushed_velvet/',null=True,blank=True)
#   #  gun_grey_crushed_velvet=models.ImageField(upload_to='Bedsdivan/gun_grey_crushed_velve/',null=True,blank=True)

