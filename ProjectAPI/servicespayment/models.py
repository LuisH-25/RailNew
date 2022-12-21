from django.db import models
from users.models import User


#MODELO  SERVICES
class Services(models.Model):
    name = models.CharField(max_length=100) 
    description = models.TextField()
    logo = models.CharField(max_length=100)
     
    def __str__(self):
        return self.name

    class Meta:
        db_table = "services"
    

#MODELO  PAYMENTS USER
class Payment_user(models.Model):
    @property
    def username(self):
        return self.user_id.username
    
    @property
    def servicename(self):
        return self.service_id.name

    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    service_id = models.ForeignKey(Services,on_delete=models.CASCADE)
    amount = models.IntegerField()
    paymentDate = models.DateField()
    expirationDate = models.DateField()
    paymentDate = models.DateField()
    expirationDate = models.DateField()
    
    class Meta:
        db_table = "payment_user"

    def __str__(self):

        return self.user_id.username + " - " + self.service_id.name

#MODELO EXPIRED PAYMENTS
class Expired_payments(models.Model):
    @property
    def username(self):
        return self.payment_user_id.user_id.username

    @property
    def servicename(self):
        return self.payment_user_id.service_id.name

    payment_user_id = models.ForeignKey(Payment_user,on_delete=models.CASCADE)
    penalty_fee_amount= models.IntegerField()

    def user_id(self):
        return self.payment_user_id.pk

    def __str__(self):
        return str(self.payment_user_id.user_id.username)

    class Meta:
        db_table = "expired_payments"