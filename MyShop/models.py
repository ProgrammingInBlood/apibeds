from django.db import models
from Product.models import *

# Create your models here.


countries=(
    ('England','England'),
    ('Scotland','Scotland'),
    ('Wales','Wales'),
    ('Northern Ireland','Northern Ireland'),
   
)





class BillingDetails(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    company_name=models.CharField(max_length=200,null=True,blank=True)
    region=models.CharField(max_length=100,default='United Kingdom (UK)')
    Street_address=models.CharField(max_length=500)
    city=models.CharField(max_length=200)
    country=models.CharField(choices=countries,max_length=200)
    postcode=models.CharField(max_length=200)
    Phone=models.BigIntegerField()
    email=models.EmailField(max_length=200)
    