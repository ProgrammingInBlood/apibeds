from django.contrib import admin
from django.urls import path,include
from .views import * 
#from rest_framework_simplejwt import views as jwt_views
#from rest_framework_simplejwt import views as jwt_views
from rest_framework.routers import DefaultRouter,SimpleRouter
#router=DefaultRouter()
router=DefaultRouter()
#==================== 2 aug 2021 ================== add product usig nested ser
router.register('add_beds',Add_New_Products_view,basename='add_beds')

#==================== latest % july Add product===================
router.register('add_ukbeds',UkDivanbeds_view,basename='add_ukbeds')
router.register('ukbeds_variant',UkBedsVariant_view,basename='ukbeds_variant')


#==================== latest Add product===================
router.register('add_your_product',add_Your_Product_view,basename='add_your_product')
router.register('divanbeds',divanbeds_view,basename='divanbeds')


#============================================old product=============
router.register('add_product',Add_product_view,basename='add_product')
router.register('add_Headboard',Add_Headboard_view,basename='add_Headboard')
router.register('add_Mattress',Add_Mattress_view,basename='add_Mattress')
router.register('add_Drawers',Add_Drawers_view,basename='add_Drawers')
router.register('add_FeetCaster',Add_FeetCastor_view,basename='add_FeetCaster')
router.register('productlist',ProductListView,basename='productlist')
router.register('divanbeds',Divanbeds_view,basename='divanbeds')

################# All Beds urls <<<<<<<<<<, ##################################

router.register('ottoman',Ottoman_view,basename='ottoman')
router.register('Kidsbed',Kids_view,basename='kidsbed')
router.register('leatherbeds',Leather_view,basename='leatherbeds')
router.register('nevadabeds',Nevada_view,basename='nevadabeds')
router.register('storage',Storage_view,basename='storage')

#======== Sleigh beds
router.register('florida',Florida_Beds_view,basename='florida')
router.register('ambassador',Ambassador_Beds_view,basename='ambassador')
router.register('kendal',Kendall_Beds_view,basename='kendal')
router.register('manocobeds',Manoco_Beds_view,basename='manocobeds')
router.register('royalbeds',Royal_Beds_view,basename='royalbeds')
router.register('swanbeds',Swan_Beds_view,basename='swanbeds')
router.register('wingbeds',Wing_Beds_view,basename='wingbeds')
router.register('winchester',Winchester_Beds_view,basename='winchester')

########################## Other pproduct urls  <<<$$$$$$$$$$$$$$$$$$$$$$$$$$$$

router.register('Fabric_sofa',Fabric_Sofa_view,basename='Fabric_sofa')
router.register('Leather_Sofa',Leather_Sofa_view,basename='Leather_sofa')
router.register('gardener_furniture',Funiture_view,basename='gardener_furniture')


#============ Tables urls
router.register('Tables',Table_view,basename='Tables')
router.register('bar-table',BarTable_view,basename='bar-table')
router.register('coffee-table',CoffeeTable_view,basename='coffee-table')
router.register('dinning-table',DinningTable_view,basename='dinning-table')
router.register('dressing-table',DressingTable_view,basename='dressing-table')
router.register('manicure-table',ManicureTable_view,basename='manicure-table')
router.register('side-table',SideTable_view,basename='side-table')




#=========================  all Chairs 
router.register('accent-chairs',AccentChairs_view,basename='accent-chairs')
router.register('arm-chairs',ArmChairs_view,basename='arm-chairs')
router.register('chesterfield',ChesterfieldChairs_view,basename='chesterfield')
router.register('fireside',FiresideChairs_view,basename='fireside')
router.register('lift-chairs',LiftChairs_view,basename='lift-chairs')
router.register('recycling-chairs',RecyclingChairs_view,basename='recycling-chairs')
router.register('dinning-chairs',DinningChairs_view,basename='dinning chairs')

router.register('Shelf',Shelf_view,basename='Shelf')
router.register('ChestDraws',ChestDraws_view,basename='ChestDraws')

router.register('WardRobes',WardRobes_view,basename='WardRobes')
# router.register('image',ImageView,basename='images')

#router.register('log',Login,basename='log')

# router.register('add_category',views.Add_Category_view,basename='add_category')
# router.register('add_variant',views.Add_Variant_view,basename='add_variant')
#router.register('api/token/', jwt_views.TokenObtainPairView.as_view(),basename='')

# router.register('',Login,basename='viewset')

#######################>>>>>>>>>>>>>>>>>>>>>>>>>For Add Basket <<<<<<<<<<<<<<<<<<<<
router.register('add_basket',Add_Basket_view,basename='Add_basket')

urlpatterns = [
    path('',Login,name='login'),
    # path(r'index', dash_board,name='index'),
    
]
urlpatterns=router.urls
