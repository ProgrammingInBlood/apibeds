from django.contrib import admin
from django.urls import path,include
from .views import * 
#from rest_framework_simplejwt import views as jwt_views
#from rest_framework_simplejwt import views as jwt_views
from rest_framework.routers import DefaultRouter,SimpleRouter
#router=DefaultRouter()
router=DefaultRouter()

router.register('rate',Customercomment_view,basename='rate')
urlpatterns=router.urls
