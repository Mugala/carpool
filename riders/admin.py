from django.contrib import admin
from .models import Ridertag, Rider, Pickup_location

# Register your models here.

admin.site.register(Ridertag)
admin.site.register(Rider)
admin.site.register(Pickup_location)