from django.db import models
import datetime as dt
from django.contrib.auth.models import User
# Create your models here.


class NewsLetterRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()

class Destination(models.Model):
    name = models.CharField(max_length =30,null=True)

    def __str__(self):
        return self.name

    def save_Destination(self):
        self.save()

class Car (models.Model):
    Car_model = models.CharField(max_length = 30)
    number_plate = models.CharField(max_length = 30)
    number_seats = models.IntegerField()

    def __str__(self):
        return self.number_plate

    def save_Car(self):
        self.save()

class Pickup_location(models.Model):
    longitude = models.FloatField()
    latitude = models.FloatField()

    def __str__(self):
        return self.longitude

    def save_Pickup_location(self):
        self.save()

class Driver (models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    pickup_point = models.ForeignKey(Pickup_location, null=True)
    destination = models.OneToOneField(Destination, null = True)
    car = models.ForeignKey(Car, null =True)
    profile_pic = models.ImageField(upload_to = 'driversdp/',null=True)
    phone_number = models.IntegerField()

    def __str__(self):
        return self.first_name

    def save_Driver (self):
        self.save()

    def delete_Driver(self):
        self.delete()

    @classmethod
    def driver_details(cls):
        details = cls.objects.all()
        return details

    @classmethod
    def search_by_destination(cls,search_term):
        dest = cls.objects.filter(image_category__name__icontains=search_term)
        return dest


    