#from bedsdivan_admin.Product.views import Add_Drawers_view, Add_FeetCastor_view, Add_Headboard_view, Add_Mattress_view, Add_product_view, Divanbeds_view, ProductListView
#from bedsdivan_admin.Product.views import Add_Drawers_view, Add_FeetCastor_view, Add_Headboard_view, Add_Mattress_view, Add_product_view, Divanbeds_view, ProductListView
from django.contrib import admin
from django.urls import path,include
from .views import * 
#from rest_framework_simplejwt import views as jwt_views
#from rest_framework_simplejwt import views as jwt_views
from rest_framework.routers import DefaultRouter,SimpleRouter
#router=DefaultRouter()
router=DefaultRouter()

router.register('product',Add_product_view,basename='product')
urlpatterns=router.urls
