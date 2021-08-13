


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






#==================================================================== USing foreign key Add Product Models 02/aug/2021 =======================

class Add_New_Products(models.Model):
    # product_type     = models.ForeignKey(category,related_name='Add_new_product' ,on_delete=models.CASCADE,default=False)
    product_name    = models.CharField(max_length=50,default='divanbeds')
    product_images     = models.ImageField(upload_to='mypic/',null=True,blank=True)
    Description      = models.TextField()
   # HeadBoard=models.ForeignKey(Headboard)
    compare_Price = models.DecimalField(decimal_places=2,max_digits=50,default=00.00)
    #cost_per_price   = models.DecimalField(decimal_places=2,max_digits=50,default=False)
    price = models.DecimalField(decimal_places=2,max_digits=50,default=00.00)

    # product_tags      = models.CharField(max_length=200,null=True,blank=True)
    


    #rating     = models.DecimalField(decimal_places=2,max_digits=5)
    def __str__(self):
        return str(self.product_name)
    # @property
    # def add_variants(self):
    #     return self.add_variant_set.all()


class Add_Variation(models.Model):
    type     = models.ForeignKey(Add_New_Products,related_name='type' ,on_delete=models.CASCADE,default=False)
    size=models.CharField(choices=size,blank=True,null=True,max_length=200)
    # color            =MultiSelectField(choices=COLOR_CHOICES,null=True,blank=True)
    base_price = models.DecimalField(decimal_places=2,max_digits=50,default=00.00)
    #color            =models.ForeignKey(ProductImage,on_delete=models.CASCADE,null=True,blank=True)
   
    #size=MultiSelectField(choices=size,max_length=255,null=True,blank=True)
    Headboard_images   = models.FileField(upload_to='Headboard/',blank=True, null=True)
    Headboard_Price = models.DecimalField(decimal_places=2,max_digits=50,default=00.00)
    Feet_images   = models.FileField(upload_to='Headboard/',blank=True, null=True)
    Feet_Price = models.DecimalField(decimal_places=2,max_digits=50,default=00.00)
    Storage_images   = models.FileField(upload_to='storage/',blank=True, null=True)
    Storage_Price = models.DecimalField(decimal_places=2,max_digits=50,default=00.00)
    mattresses_images   = models.FileField(upload_to='beds/',blank=True, null=True,default=0)
    mattresses_Price = models.DecimalField(decimal_places=2,max_digits=50,default=00.00)

    fun=Add_New_Products.__str__

    def __str__(self):
        return f"{self.size} -£{self.base_price}"






class Color(models.Model):

    color=models.ForeignKey(Add_Variation,on_delete=models.CASCADE,default=False,related_name='color',null=True,blank=True)
    Headboard_color=models.ForeignKey(Add_Variation,on_delete=models.CASCADE,default=False,related_name='Headboard_color',null=True,blank=True)
    Storage_color=models.ForeignKey(Add_Variation,on_delete=models.CASCADE,default=False,related_name='Storage_color',null=True,blank=True)
    Mattress_color=models.ForeignKey(Add_Variation,on_delete=models.CASCADE,default=False,related_name='Mattress_color',null=True,blank=True)
    Feet_color=models.ForeignKey(Add_Variation,on_delete=models.CASCADE,default=False,related_name='Feet_color',null=True,blank=True)
    #Headboard_color=models.ForeignKey(Add_Variation,on_delete=models.CASCADE,default=False,related_name='color1',null=True,blank=True)
    # color2=models.ForeignKey(Add_Variation,on_delete=models.CASCADE,default=False,related_name='color2')
    # mybeds=models.ForeignKey(My_DivanBeds,on_delete=models.CASCADE,default=False,related_name='my_beds')
    # drawer=models.ForeignKey(My_DivanBeds,on_delete=models.CASCADE,default=False,related_name='drawer')
    # head=models.ForeignKey(My_DivanBeds,on_delete=models.CASCADE,default=False,related_name='head')
    # mattres=models.ForeignKey(My_DivanBeds,on_delete=models.CASCADE,default=False,related_name='mattres')




    grey_linen=models.ImageField(upload_to='Bedsdivan/grey_linen/',null=True,blank=True)
    silver_crushed_velvet=models.ImageField(upload_to='Bedsdivan/silver_crushed_velvet/',null=True,blank=True)
    white_crushed_velvet=models.ImageField(upload_to='Bedsdivan/white_crushed_velvet/',null=True,blank=True)
    Blue_plus_velvet=models.ImageField(upload_to='Bedsdivan/Blue_plus_velvet/',null=True,blank=True)
    grey_seude =models.ImageField(upload_to='Bedsdivan/grey_seude/',null=True,blank=True)
    charcoal_chenille=models.ImageField(upload_to='Bedsdivan/charcoal_chenille/',null=True,blank=True)
    pattern_cream=models.ImageField(upload_to='Bedsdivan/pattern_cream/',null=True,blank=True)
    purple_velvet=models.ImageField(upload_to='Bedsdivan/purple_velvet/',null=True,blank=True)
    white_crushed_velvet=models.ImageField(upload_to='Bedsdivan/white_crushed_velvet/',null=True,blank=True)
    black_leather=models.ImageField(upload_to='Bedsdivan/black_leather/',null=True,blank=True)
    black_crushed_velvet=models.ImageField(upload_to='Bedsdivan/black_crushed_velvet/',null=True,blank=True)
    champagne_crushed_velvet=models.ImageField(upload_to='Bedsdivan/champagne_crushed_velvet/',null=True,blank=True)
    gun_grey_crushed_velvet=models.ImageField(upload_to='Bedsdivan/gun_grey_crushed_velve/',null=True,blank=True)

    # def __str__(self):
    #     return str[self.grey_linen,self.silver_crushed_velvet,self.white_crushed_velvet,self.Blue_plus_velvet,self.grey_seude,self.charcoal_chenille,self.pattern_cream,self.purple_velvet,self.white_crushed_velvet,self.black_leather]
    


    # def __str__(self):
    #     return str(self.color)
   







class Add_Divanbeds(models.Model):
    # product_type     = models.ForeignKey(category,related_name='Add_new_product' ,on_delete=models.CASCADE,default=False)
    product_name    = models.CharField(max_length=50,default='divanbeds')
    product_images     = models.ImageField(upload_to='bedsdivan/',null=True,blank=True)
    Description      = models.TextField()
   # HeadBoard=models.ForeignKey(Headboard)
    compare_Price = models.DecimalField(decimal_places=2,max_digits=50,default=00.00,null=True,blank=True)
    #cost_per_price   = models.DecimalField(decimal_places=2,max_digits=1000,default=False)
    price = models.DecimalField(decimal_places=2,max_digits=50,default=00.00,null=True,blank=True)
    # product_tags      = models.CharField(max_length=200,null=True,blank=True)
    


    #rating     = models.DecimalField(decimal_places=2,max_digits=5)
    
    def __str__(self):
        return str(self.product_name)

#======================= Add variant============

class Add_BedsVariant(models.Model):
   # type     = models.ForeignKey(Add_Product,related_name='type' ,on_delete=models.CASCADE,null=True,blank=True)
    size=models.CharField(choices=size,blank=True,null=True,max_length=200)
    # color            =MultiSelectField(choices=COLOR_CHOICES,null=True,blank=True)
    base_price = models.DecimalField(decimal_places=2,max_digits=50,default=00.00,null=True,blank=True)
    #color            =models.ForeignKey(ProductImage,on_delete=models.CASCADE,null=True,blank=True)

    grey_linen=models.ImageField(upload_to='Bedsdivan/grey_linen/',null=True,blank=True)
    silver_crushed_velvet=models.ImageField(upload_to='Bedsdivan/silver_crushed_velvet/',null=True,blank=True)
    white_crushed_velvet=models.ImageField(upload_to='Bedsdivan/white_crushed_velvet/',null=True,blank=True)
    Blue_plus_velvet=models.ImageField(upload_to='Bedsdivan/Blue_plus_velvet/',null=True,blank=True)
    grey_seude =models.ImageField(upload_to='Bedsdivan/grey_seude/',null=True,blank=True)
    charcoal_chenille=models.ImageField(upload_to='Bedsdivan/charcoal_chenille/',null=True,blank=True)
    pattern_cream=models.ImageField(upload_to='Bedsdivan/pattern_cream/',null=True,blank=True)
    purple_velvet=models.ImageField(upload_to='Bedsdivan/purple_velvet/',null=True,blank=True)
    white_crushed_velvet=models.ImageField(upload_to='Bedsdivan/white_crushed_velvet/',null=True,blank=True)
    black_leather=models.ImageField(upload_to='Bedsdivan/black_leather/',null=True,blank=True)
    black_crushed_velvet=models.ImageField(upload_to='Bedsdivan/black_crushed_velvet/',null=True,blank=True)
    champagne_crushed_velvet=models.ImageField(upload_to='Bedsdivan/champagne_crushed_velvet/',null=True,blank=True)
    gun_grey_crushed_velvet=models.ImageField(upload_to='Bedsdivan/gun_grey_crushed_velve/',null=True,blank=True)

    
    #size=MultiSelectField(choices=size,max_length=255,null=True,blank=True)
    Headboard_images   = models.FileField(upload_to='Headboard/',blank=True, null=True)
    Headboard_Price = models.DecimalField(decimal_places=2,max_digits=50,default=00.00,null=True,blank=True)
    Storage_images   = models.FileField(upload_to='storage/',blank=True, null=True)
    Storage_Price = models.DecimalField(decimal_places=2,max_digits=50,default=00.00,null=True,blank=True)
    mattresses_images   = models.FileField(upload_to='beds/',blank=True,null=True)
    mattresses_Price = models.DecimalField(decimal_places=2,max_digits=50,default=00.00,null=True,blank=True)

  


######============================================================  for nested  model =============


class Add_Product(models.Model):
    # product_type     = models.ForeignKey(category,related_name='Add_new_product' ,on_delete=models.CASCADE,default=False)
    product_name    = models.CharField(max_length=50,default='divanbeds')
    product_images     = models.ImageField(upload_to='bedsdivan/',null=True,blank=True)
    Description      = models.TextField()
   # HeadBoard=models.ForeignKey(Headboard)
    compare_Price = models.DecimalField(decimal_places=2,max_digits=50,default=00.00,null=True,blank=True)
    #cost_per_price   = models.DecimalField(decimal_places=2,max_digits=1000,default=False)
    price = models.DecimalField(decimal_places=2,max_digits=50,default=00.00,null=True,blank=True)
    # product_tags      = models.CharField(max_length=200,null=True,blank=True)
    


    #rating     = models.DecimalField(decimal_places=2,max_digits=5)
    
    def __str__(self):
        return str(self.product_name)
    # @property
    # def add_variants(self):
    #     return self.add_variant_set.all()

    # def save(self, *args, **kwargs):
    #     self. += 1
    #     return super(Add_product, self).save(*args, **kwargs) #


class Add_Variant(models.Model):
    type     = models.ForeignKey(Add_Product,related_name='type' ,on_delete=models.CASCADE,null=True,blank=True)
    size=models.CharField(choices=size,blank=True,null=True,max_length=200)
    # color            =MultiSelectField(choices=COLOR_CHOICES,null=True,blank=True)
    base_price = models.DecimalField(decimal_places=2,max_digits=50,default=00.00,null=True,blank=True)
    #color            =models.ForeignKey(ProductImage,on_delete=models.CASCADE,null=True,blank=True)

    grey_linen=models.ImageField(upload_to='Bedsdivan/grey_linen/',null=True,blank=True)
    silver_crushed_velvet=models.ImageField(upload_to='Bedsdivan/silver_crushed_velvet/',null=True,blank=True)
    white_crushed_velvet=models.ImageField(upload_to='Bedsdivan/white_crushed_velvet/',null=True,blank=True)
    Blue_plus_velvet=models.ImageField(upload_to='Bedsdivan/Blue_plus_velvet/',null=True,blank=True)
    grey_seude =models.ImageField(upload_to='Bedsdivan/grey_seude/',null=True,blank=True)
    charcoal_chenille=models.ImageField(upload_to='Bedsdivan/charcoal_chenille/',null=True,blank=True)
    pattern_cream=models.ImageField(upload_to='Bedsdivan/pattern_cream/',null=True,blank=True)
    purple_velvet=models.ImageField(upload_to='Bedsdivan/purple_velvet/',null=True,blank=True)
    white_crushed_velvet=models.ImageField(upload_to='Bedsdivan/white_crushed_velvet/',null=True,blank=True)
    black_leather=models.ImageField(upload_to='Bedsdivan/black_leather/',null=True,blank=True)
    black_crushed_velvet=models.ImageField(upload_to='Bedsdivan/black_crushed_velvet/',null=True,blank=True)
    champagne_crushed_velvet=models.ImageField(upload_to='Bedsdivan/champagne_crushed_velvet/',null=True,blank=True)
    gun_grey_crushed_velvet=models.ImageField(upload_to='Bedsdivan/gun_grey_crushed_velve/',null=True,blank=True)

    
    #size=MultiSelectField(choices=size,max_length=255,null=True,blank=True)
    Headboard_images   = models.FileField(upload_to='Headboard/',blank=True, null=True)
    Headboard_Price = models.DecimalField(decimal_places=2,max_digits=50,default=00.00,null=True,blank=True)
    Storage_images   = models.FileField(upload_to='storage/',blank=True, null=True)
    Storage_Price = models.DecimalField(decimal_places=2,max_digits=50,default=00.00,null=True,blank=True)
    mattresses_images   = models.FileField(upload_to='beds/',blank=True,null=True)
    mattresses_Price = models.DecimalField(decimal_places=2,max_digits=50,default=00.00,null=True,blank=True)

    # class Meta:
    #     ordering = (crea)

    # def __str__(self):
    #     return f"{self.base_price+self.Headboard_Price+self.mattresses_Price+self.Storage_Price }"

    # def __str__(self):
    #     return self.base_price+self.Headboard_Price +self.mattresses_Price +self.Storage_Price
   



#=========================================================================== Add new  =================


class Add_new_product(models.Model):
    product_type     = models.CharField(choices=beds_category,max_length=50,null=True,blank=True)
    product_name    = models.CharField(max_length=100,null=True,blank=True)
    Description      = models.TextField(max_length=200,null=True,blank=True)
    product_image=models.ImageField(upload_to='gallery/product',null=True,blank=True)
   # HeadBoard=models.ForeignKey(Headboard)
    compare_Price = models.DecimalField(decimal_places=2,max_digits=20,default=00,null=True,blank=True)
    #cost_per_price   = models.DecimalField(decimal_places=2,max_digits=1000,default=00,null=True,blank=True)
    price = models.DecimalField(decimal_places=2,max_digits=20,default=00,null=True,blank=True)
    #rating     = models.DecimalField(decimal_places=2,max_digits=5)
    active =models.BooleanField(default=True)
    #size=models.CharField(choices=size,max_length=20,null=True,blank=True)
    product_tags     = models.CharField(max_length=50,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    #Color=MultiSelectField(choices=COLOR_CHOICES,null=True,blank=True)
    size=models.CharField(choices=size,max_length=20,null=True,blank=True)
    Color=MultiSelectField(choices=COLOR_CHOICES,null=True,blank=True)
    storage_file=models.ImageField(upload_to='gallery/storage/',null=True)
    storage_price=models.DecimalField(decimal_places=2,max_digits=50,default=00.00,null=True)
  
    Headboard_image=models.ImageField(upload_to='gallery/headboard',null=True,blank=True)
    Headboard_price=models.DecimalField(decimal_places=2,max_digits=50,default=00.00,null=True,blank=True)
    mattresses_image=models.ImageField(upload_to="gallery/matress_image",null=True,blank=True)
    mattresses_price=models.DecimalField(decimal_places=2,max_digits=50,default=00.00,null=True,blank=True)

    # def get_total(self, request): 
    #     return Add_new_product.objects.aggregate(price=Sum('price','Headboard_price'))

    # def total_price(self):
    #     total = self.price+self.Headboard_price+self.storage_price+self.mattresses_price
    #     return total
    #price = models.PositiveIntegerField(total_price)
    class Meta:
     odering=['-created_at']

   

    



# def __init__(self,price,Headboard_price)
 
#        self.price=self.price+self.Headboard_price
#        return self.price

# obj=Add_new_product(price,Headboard_price)

    
    


    def __str__(self):
        return f"{self.base_price+self.Headboard_price+self.mattresses_price+self.storage_price}"


     
    class Meta:
        verbose_name_plural='Add_products'
        ordering =['-created_at']
    def create(self, validated_date):
        product_image = self.context['request'].FILES.getlist('product_image')
        for image in list(product_image):
              m1 = Post(id=id,image=image,)
              m1.save()
              
              m2 = post(post=m1, product_image= image)
              m2.save()

   
    
#  
    def __str__(self):
        return f"{self.size}-{self.product_name}-£{self.price}"

    # def __file__(self):
    #     return self.product_image

    #  def __str__(self):
    #     return self.title

    # def get_absolute_url(self):
    #     return reverse("core:product", kwargs={
    #         'slug': self.slug
    #     })

    # def get_add_to_cart_url(self):
    #     return reverse("core:add-to-cart", kwargs={
    #         'slug': self.slug
    #     })

    # def get_remove_from_cart_url(self):
    #     return reverse("core:remove-from-cart", kwargs={
    #         'slug': self.slug
    #     })

# class Image_File(models.Model):
#     images=models.ForeignKey(Add_new_product,on_delete=models.CASCADE)


###########################>>>>>>>>>>>>>>>>>>>>>>>>.HeadBoard Model <<<<<<<<<<<<##############################################

headboard_type=(
    ('Panel Headboard'),
    ('Cube Headboard'),
    ('Plain Headboard'),
)



class Headboard(models.Model):
    size=models.ForeignKey(Add_new_product,on_delete=models.CASCADE,blank=True,null=True)
    type = models.CharField(max_length=30,blank=True,null=True)
    headboard_image = models.ImageField(upload_to='Headboard/',blank=True, null=True)
    price = models.IntegerField(null=True,blank=True)
    
    color=ColorField(choices=COLOR_CHOICES)
    # def __str__(self):
    #     return self.type + ' '+self.size
    def __str__(self):
        return f"{self.type}-£{self.price}"


###########################>>>>>>>>>>>>>>>>>>>>>>>>.Mattress Model <<<<<<<<<<<<##############################################

Mattress_type=(
    ('Panel Headboard'),
    ('Cube Headboard'),
    ('Plain Headboard'),
)

class Mattress(models.Model):
    size=models.ForeignKey(Add_new_product,on_delete=models.CASCADE,default="No Mattress")
    mattaress_type = models.CharField(max_length=50)
    mattresses_image = models.ImageField(upload_to='mattaress',blank=True, null=True,default='no image')
    price = models.IntegerField(null=True,blank=True)
  
    color=ColorField(choices=COLOR_CHOICES)

    def __str__(self):
        return f"{self.mattaress_type}-£{self.price}"


###########################>>>>>>>>>>>>>>>>>>>>>>>>.FeetCAstor Model <<<<<<<<<<<<##############################################

class FeetCastor(models.Model):
    type = models.CharField(max_length=20)
    price = models.IntegerField(null=True,blank=True)
    def __str__(self):
        return f"{self.type}-{self.price}"


###########################>>>>>>>>>>>>>>>>>>>>>>>>.Drawers Model <<<<<<<<<<<<##############################################
        

class Drawers(models.Model):
    size = models.ForeignKey(Add_new_product,on_delete=models.CASCADE,default="no Drawer")
    type=models.CharField(max_length=30)
    price = models.IntegerField(null=True,blank=True)
    def __str__(self):
        return f"{self.type}-£{self.price}"



####################################======>>>>>>>>>>>>>>> Add to BAsket <<<<<<=====#########################################
from django.db.models import Avg, Max, Min, Sum

class Add_Basket(models.Model):
    select_color=models.CharField(choices=COLOR_CHOICES,verbose_name='select color',max_length=50)
    select_size=models.ForeignKey(Add_new_product,related_name='add_basket',on_delete=models.CASCADE,null=True)
    storage_option=models.ForeignKey(Drawers,related_name='add_basket',on_delete=models.CASCADE,default='no storage')
    select_feet=models.ForeignKey(FeetCastor,related_name='add_basket',on_delete=models.CASCADE)
    select_headboard=models.ForeignKey(Headboard,related_name='add_basket',on_delete=models.CASCADE,default='no-headboard')
    select_mattresses=models.ForeignKey(Mattress,related_name='add_basket',on_delete=models.CASCADE,default='no-mattress')

    # def __file__(self):
    #     return self.select_size.product_image
    def __int__(self):
        return f"{self.select_size.price+self.select_headboard.price+self.select_mattresses.price+self.storage_option.price+self.select_feet.price}"
    # def __str__(self):
    #     return f"{self.select_size.product_name+self.select_headboard.type+self.select_mattresses.mattaress_type}"


    # price=[select_size.price,storage_option.price,select_feet.price,select_headboard.price]
    # total=sum(price)



class All_Beds(models.Model):
    beds_category    = models.CharField(choices=beds_category,max_length=50,null=True,blank=True)
    product_name    = models.CharField(max_length=100,null=True,blank=True)
    size=models.CharField(choices=size,max_length=20,null=True,blank=True)
    Color=MultiSelectField(choices=COLOR_CHOICES,null=True,blank=True)
   
    beds_image=models.ImageField(upload_to='gallery/product',null=True,blank=True)
   # HeadBoard=models.ForeignKey(Headboard)
    compare_Price = models.DecimalField(decimal_places=2,max_digits=20,default=00,null=True,blank=True)
    #cost_per_price   = models.DecimalField(decimal_places=2,max_digits=1000,default=00,null=True,blank=True)
    price = models.DecimalField(decimal_places=2,max_digits=20,default=00,null=True,blank=True)
    #rating     = models.DecimalField(decimal_places=2,max_digits=5)
    active =models.BooleanField(default=True)
    Description      = models.TextField(max_length=200,null=True,blank=True)
    #size=models.CharField(choices=size,max_length=20,null=True,blank=True)
   # beds_tags     = models.CharField(max_length=50,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    #Color=MultiSelectField(choices=COLOR_CHOICES,null=True,blank=True)
    

    def __str__(self):
        return f"{self.size}-{self.product_name}-{self.price}"



# other_category=(
#     ('Sofa',(
#         ('Fabric Sofa',(
#             ('Champion Sofa','Champion Sofa'),
#             ('Chicago Sofa','Chicago Sofa'),
#         )),
#         ('Leather Sofa','Leather Sofa'),
#     )
#     ),
#     ('ChestDraws','ChestDraws'),
#     ('Chairs',(
#         ('Dinning sets','Dinning Set'),
#     )),
#     ('Shelfs','Shelfs'),
#     ('Wardrobes','Wardrobes'),
#     ('Tables',(
#         ('Coffee Table','Coffee Table'),
#         ('Dinning Table','Dinning Table'),
#     )),
#     ('Furniture',(
#         ('Gardener Furniture','Gardener Furniture'),
#     )),
# )

others_category=(
    ('Sofa',(
        ('Fabric Sofa','Fabric Sofa'),
           
        ('Leather Sofa','Leather Sofa'),
    )
    ),
    ('ChestDraws','ChestDraws'),
    ('Chairs',(
        ('Accent Chairs','Accent Chairs'),
        ('Arm Chairs','Arm Chairs'),
        ('Chesterfield Chairs','Chesterfield Chairs'),
        ('Dinning sets Chairs','Dinning sets Chairs'),
        ('Fireside Chairs','Fireside Chairs'),
        ('Lift Chairs','Lift Chairs'),
        ('Recycling Chairs','Recycling Chairs'),
    )),
    ('Shelf','Shelf'),
    ('WardRobes','WardRobes'),
    ('Tables',(
        ('Bar Tables','Bar Tables'),
        ('Coffee Tables', 'Coffee Tables'),
        ('Dinning Tables','Dinning Tables'),
        ('Dressing Tables','Dressing Tables'),
        ('Manicure Tables','Manicure Tables'),
        ('Side Tables','Side Tables'),
    )),
    ('Furniture','Furniture')
)
class OTHERS(models.Model):
    other_category    = models.CharField(choices=others_category,max_length=50,null=True,blank=True)
    product_type    = models.CharField(max_length=100,null=True,blank=True)
    size=models.CharField(max_length=20,null=True,blank=True)
    Color=MultiSelectField(choices=COLOR_CHOICES,null=True,blank=True)
   
    beds_image=models.ImageField(upload_to='gallery/product',null=True,blank=True)
   # HeadBoard=models.ForeignKey(Headboard)
    compare_Price = models.DecimalField(decimal_places=2,max_digits=20,default=00,null=True,blank=True)
    #cost_per_price   = models.DecimalField(decimal_places=2,max_digits=1000,default=00,null=True,blank=True)
    price = models.DecimalField(decimal_places=2,max_digits=20,default=00,null=True,blank=True)
    #rating     = models.DecimalField(decimal_places=2,max_digits=5)
    active =models.BooleanField(default=True)
    Description      = models.TextField(max_length=200,null=True,blank=True)
    #size=models.CharField(choices=size,max_length=20,null=True,blank=True)
   # beds_tags     = models.CharField(max_length=50,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    material_type=models.CharField(max_length=200, null=True,blank=True)
    def __str__(self):
        return f"{self.size}-{self.price}"
    
    



   
#==================================== multi image ==============================


class Image(models.Model):
    image=models.ImageField(upload_to='images')
    def __str__(self):
        return str(self.image)



















       
