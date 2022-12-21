from rest_framework.viewsets import ModelViewSet
from .models import Services, Payment_user, Expired_payments
from .serializers import ServicesSerializer, Payment_userSerializer, Expired_paymentSerializer
from django.shortcuts import get_object_or_404
from rest_framework import filters, status
from datetime import datetime
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
import random
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated 

from rest_framework.throttling import UserRateThrottle
#CRUD SERVICCES VIEWSET
class ServicesViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ServicesSerializer
    throttle_scope = 'view_others'

    def get_queryset(self):
        return Services.objects.all()
   
    def get_object(self, queryset=None, **kwargs):
        item_services= self.kwargs.get('pk')
        return get_object_or_404(Services, id=item_services)
       

       
#CRUD PAYMENT USER VIEWSET se trabaja con cada metodo uno para admin y user respectivamente
class Payment_userViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Payment_user.objects.all()
    serializer_class = Payment_userSerializer
    filter_backends =  [filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['paymentDate','expirationDate']
    search_fields = ['paymentDate','expirationDate']
    ordering = ('-id')
    throttle_scope = 'user'


    def get_serializer_class(self, *args, **kwargs):
        return Payment_userSerializer

    def list(self, request, *args):
        page = self.paginate_queryset(self.queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(self.queryset, many=True)
        return Response(serializer.data)  
    
    def create(self, request, *args, **kwargs):
        new_user_payment = super().create(request, *args, **kwargs)
        payment_date = datetime.strptime(request.data['paymentDate'], '%Y-%m-%d')
        expiration_date = datetime.strptime(request.data['expirationDate'], '%Y-%m-%d')

        #cuando la fecha de pago es mayor que la fecha de expiracion se agrgara una penalidad random
        if payment_date > expiration_date:
            new_expired_payment = Expired_payments()
            new_expired_payment.penalty_fee_amount = random.randint(15, 150)
            new_expired_payment.payment_user_id_id= new_user_payment.data['id']
            new_expired_payment.save()
        return new_user_payment

    def retrieve(self, request, pk=None):
        todo = get_object_or_404(self.queryset, pk=pk)
        serializer = Payment_userSerializer(todo)
        return Response(serializer.data)

    def update(self, request, pk=None):
        todo = get_object_or_404(self.queryset, pk=pk)
        serializer = Payment_userSerializer(todo, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        todo = get_object_or_404(self.queryset, pk=pk)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



#CRUD EXPIRED PAYMENTS VIEWSET
class Expired_paymentsViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = Expired_paymentSerializer
    throttle_scope = 'anon'
    def get_queryset(self):
        return Expired_payments.objects.all()

    def get_object(self, queryset=None, **kwargs):
        item_expiredpay= self.kwargs.get('pk')
        return get_object_or_404(Expired_payments, id=item_expiredpay)
     