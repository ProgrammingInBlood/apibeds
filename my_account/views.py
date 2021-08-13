from django.shortcuts import render

# Create your views here.

from .serializers import MyTokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework.response import Response



class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer



############################### Registration View ########################

from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework import generics


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

##############################>>>>>>>>>>>>>Change PAssword View>>>>>>>>>>>>>>#####################
from rest_framework.permissions import IsAuthenticated
from .serializers import *

class ChangePasswordView(generics.UpdateAPIView):

    queryset = User.objects.all()
    #permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer


##############################>>>>>>>>>>>>>Update profile View>>>>>>>>>>>>>>#####################

class UpdateProfileView(generics.UpdateAPIView):
    queryset=User.objects.all()
    #permission_classes=(IsAuthenticated)
    serializer_class=UpdateUserSerializer

####################################>>>>>>>>>>>>>> Logout view   <<<<<<<<<<<<<<<<<<<<< #######################

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status



class LogoutView(APIView):
    #permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
