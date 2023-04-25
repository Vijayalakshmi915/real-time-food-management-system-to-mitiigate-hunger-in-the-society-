from django.db import models
from django.conf import settings 
from email.policy import default
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    userId = models.CharField(max_length=300)
    email = models.EmailField(max_length=5000, unique=True)
    mobNo = models.CharField(max_length=13)
    address = models.TextField(max_length=2000)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(null=True)
    #types of users
    is_superadmin=models.BooleanField('is superadmin', default=False)
    is_admin=models.BooleanField('is admin', default=False)
    is_restaurant=models.BooleanField('is restaurant', default=False)
    is_orphanage=models.BooleanField('is orphanage', default=False)
    is_people=models.BooleanField('is people', default=False)
    
class People(models.Model):
    Id=models.IntegerField(primary_key=True)
    username=models.CharField(max_length=100, blank=True, null=True)
    #people details
    peopleMobileNo=models.CharField(max_length=100, blank=True, null=True)
    peopleMail=models.CharField(max_length=100, blank=True, null=True)
    peopleLocation=models.CharField(max_length=100, blank=True, null=True)
    peopleFoodDescription=models.CharField(max_length=100, blank=True, null=True)
    peopleQuantity=models.CharField(max_length=100, blank=True, null=True)

    def __int__(self):
        return self.username


class Orphanage(models.Model):
    Id=models.IntegerField(primary_key=True)
    username=models.CharField(max_length=100, blank=True, null=True)
    #orphange details
    orphanageMobileNo=models.CharField(max_length=100, blank=True, null=True)
    orphanageMail=models.CharField(max_length=100, blank=True, null=True)
    orphanageLocation=models.CharField(max_length=100, blank=True, null=True)
    orphanageDescription=models.CharField(max_length=100, blank=True, null=True)
    orphanageQuantity=models.CharField(max_length=100, blank=True, null=True)
    orphavailable_date=models.DateField(blank=True, null=True)


    def __str__(self):
        return self.username

class Admin(models.Model):
    Id=models.IntegerField(primary_key=True)
    username=models.CharField(max_length=100, blank=True, null=True)
    #admin details
    adminMobileNo=models.CharField(max_length=100, blank=True, null=True)
    adminMail=models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.username

class Restaurant(models.Model):
    Id=models.IntegerField(primary_key=True)
    username=models.CharField(max_length=100, blank=True, null=True)
    #restaurant details
    restaurantMobileNo=models.CharField(max_length=100, blank=True, null=True)
    restaurantMail=models.CharField(max_length=100, blank=True, null=True)
    available_date=models.DateField(blank=True, null=True)
    restaurantLocation=models.CharField(max_length=100, blank=True, null=True)
    restaurantFoodDescription=models.CharField(max_length=100, blank=True, null=True)
    restaurantQuantity=models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.username