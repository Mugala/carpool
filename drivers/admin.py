from django.contrib import admin
from .models import Destination, Car, Pickup_location,Driver

# Register your models here.

admin.site.register(Destination)
admin.site.register(Car)
admin.site.register(Driver)
admin.site.register(Pickup_location)
