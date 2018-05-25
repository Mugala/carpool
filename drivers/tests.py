from django.test import TestCase
from .models import Car,Destination,Pickup_location,Driver

# Create your tests here.

class DriverTestClass(TestCase):
    def setUp(self):
        self.pickup_point = Pickup_location(longitude = 36.00000, latitude = 1.00000 )
        self.pickup_point.save()
        self.car = Car (Car_model = "Lambo",number_plate = "KAA 001B",number_seats = 2)
        self.car.save()
        self.destination = Destination (name = "Westlands")
        self.destination.save()
        self.driver1 = Driver(first_name = 'Frank', last_name = 'Fr', pickup_point = self.pickup_point, destination = self.destination, car = self.car, profile_pic = '2018-05-06',phone_number = 7259854123)
        self.driver1.save_Driver()
        

    # def tearDown(self):
    #     Driver.objects.all().delete()
    #     Car.objects.all().delete()
    #     Destination.objects.all().delete()
    #     Pickup_location.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.driver1,Driver))

#     def test_instance(self):
#         self.assertTrue(isinstance(self.img1,Image))