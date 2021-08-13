from django.contrib import admin
from django.urls import path,include
from .views import * 
#from rest_framework_simplejwt import views as jwt_views
#from rest_framework_simplejwt import views as jwt_views
from rest_framework.routers import DefaultRouter,SimpleRouter
#router=DefaultRouter()
router=DefaultRouter()

router.register('billingaddress',Billing_view,basename='add_product')

router.register('bedsdivan',Divanbeds_view,basename='bedsdivan')




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


urlpatterns=router.urls