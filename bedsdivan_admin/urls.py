"""bedsdivan_admin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt import views as jwt_views
from Orders import views as login_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin_site/', include('admin_site.urls')),
    path('',include('Product.urls')),
    path('api/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/',include('my_account.urls')),
    path('abc/',login_views.Login),
    path('shop/',include('MyShop.urls')),
    path('cart/',include('Shopping_Cart.urls')),
    path('ratings/', include('Comment.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

