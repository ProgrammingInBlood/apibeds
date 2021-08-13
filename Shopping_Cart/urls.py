from django.contrib import admin
from django.urls import path,include
from .views import * 
#from rest_framework_simplejwt import views as jwt_views
#from rest_framework_simplejwt import views as jwt_views
from rest_framework.routers import DefaultRouter,SimpleRouter
#router=DefaultRouter()
router=DefaultRouter()

router.register('cart',Cart_view,basename='cart')


urlpatterns=router.urls