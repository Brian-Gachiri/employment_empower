from django.db import models
from django.contrib.auth.models import User
from .models import ClientMembership, Client


class PaymentMethod(models.Model):

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    card_holder_name = models.CharField(max_length=250)
    card_holder_number = models.CharField(max_length=100)
    expiration_date = models.CharField(max_length=10)
    security_code = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Coupon(models.Model):
    coupon_code = models.CharField(max_length=50)
    coupon_discount = models.FloatField() ##Percentage
    expiration_date = models.DateField(ull=True, blank=True)
    maximum_uses = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Order(models.Model):
    client = models.ForeignKey(ClientMembership, on_delete=models.SET_NULL, null=True, blank=True)
    payment_method = models.ForeignKey(PaymentMethod,on_delete=models.SET_NULL, null=True, blank=True)
    coupon_id = models.ForeignKey(Coupon, on_delete=models.SET_NULL, null=True, blank=True)
    tax = models.FloatField(null=True, blank=True)
    total = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)