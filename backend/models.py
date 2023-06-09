from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Client(User):

    phone_number = models.IntegerField()
    address = models.CharField(max_length=50, null=True, blank=True)
    profile_image = models.ImageField(upload_to="images/", default='user.png')
    date_of_birth = models.DateField(null=True, blank=True)
    is_online = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Membership(models.Model):

    name = models.CharField(max_length=250)
    description = models.TextField()
    price = models.FloatField()
    tier = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ClientMembership(models.Model):

    membership = models.ForeignKey(Membership, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    auto_renewal = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Queries(models.Model):
    text = models.TextField(null=True, blank=True)
    name = models.CharField(max_length=250, null=True, blank=True)
    email = models.EmailField(max_length=250)
    read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
