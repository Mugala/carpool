from django.db import models
import datetime as dt
from django.contrib.auth.models import User
# Create your models here.


class Drivertag(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Car (models.Model):
    Car_model = models.CharField(max_length = 30)
    number_plate = models.CharField(max_length = 30)
    number_seats = models.IntegerField()

class Pickup_location(models.Model):
    longitude = models.FloatField()
    latitude = models.FloatField()

class Driver (models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    pickup_point = models.ForeignKey(Pickup_location)
    destination = models.CharField(max_length = 50)
    tags = models.ManyToManyField(Drivertag)
    car = models.ForeignKey(Car)
    profile_pic = models.ImageField(upload_to = 'driversdp/',null=True)
    phone_number = models.IntegerField()


    