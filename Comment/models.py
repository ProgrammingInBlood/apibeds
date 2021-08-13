from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from star_ratings.models import Rating
# from settings.AUTH_USER_MODEL import User


# Create your models here.

class Customer(models.Model):
    Customer=models.CharField(max_length=20)
    ratings=GenericRelation(Rating, related_query_name='customer')
    review=models.TextField()



# Customer.objects.filter(ratings__isnull=False).order_by('ratings__average')
