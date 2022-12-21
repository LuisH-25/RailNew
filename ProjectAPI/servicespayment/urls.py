from django.urls import path
from rest_framework.routers import DefaultRouter
#from .views import ServicesViewSet, Expired_paymentsViewSet
from .views import ServicesViewSet,Payment_userViewSet, Expired_paymentsViewSet
servicespayment_router = DefaultRouter()
servicespayment_router.register(r"services", ServicesViewSet, basename="services")
servicespayment_router.register(r"payment-user", Payment_userViewSet, basename="payment-user")
servicespayment_router.register(r"expired-payments", Expired_paymentsViewSet, basename="expired-payments")

urlpatterns = servicespayment_router.urls

