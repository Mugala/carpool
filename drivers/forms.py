from django import forms
from .models import Car,Destination,Driver,Pickup_location

class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')

class DriverProfile(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ['first_name', 'last_name', 'profile_pic', 'phone_number',]
        exclude = ['user', ]


class CarDetails(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['Car_model', 'number_plate', 'number_seats',]
        exclude = ['user', 'car']
     

class SheduleForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['Car_model', 'number_plate', 'number_seats',]
        exclude = ['user',]
    
        model = Destination
        fields = ['name',]
        exclude = ['user',]