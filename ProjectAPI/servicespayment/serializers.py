from rest_framework.serializers import ModelSerializer
from servicespayment.models import Services, Payment_user,Expired_payments
from rest_framework import serializers
from users.models import User
from .models import Services

class ServicesSerializer(ModelSerializer):
    class Meta:
        model = Services
        fields = "__all__"


class Payment_userSerializer(ModelSerializer):

    class Meta:
        model = Payment_user
        fields = ('id','amount','paymentDate','expirationDate','user_id','username','service_id','servicename' )
    

class Expired_paymentSerializer(ModelSerializer):
    class Meta:
        model = Expired_payments
        fields = ('id','payment_user_id','user_id','username','servicename','penalty_fee_amount', )