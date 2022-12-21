from rest_framework import routers
from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView,TokenVerifyView,)
from .views import GetUsers, SignUpView,LoginView
 
router_user = routers.DefaultRouter()
router_user.register('', GetUsers)

urlpatterns = [
    path("signup/",SignUpView.as_view(),name="signup"), 
    path("login/", LoginView.as_view(), name="login"), #PONER EL ACCES TOKEN EN ESE BODY
    path("jwt/create/", TokenObtainPairView.as_view(), name="jwt_create"),
    path("jwt/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("jwt/verify/", TokenVerifyView.as_view(), name="token_verify"),
]

urlpatterns += router_user.urls 