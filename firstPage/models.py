from django.db import models

# Create your models here.
class Ride(models.Model):
    ride_id = models.IntegerField()
    user_id = models.IntegerField()
    vehicle_id=models.IntegerField()
    package_id = models.FloatField()
    travel_type_id=models.IntegerField()
    from_area_id = models.FloatField()
    to_area_id=models.FloatField()
    from_city_id= models.FloatField()
    to_city_id=models.FloatField()
    from_date=models.TextField()
    to_date = models.TextField()
    online_booking = models.BooleanField()
    mobile_site_booking=models.BooleanField()
    booking_created = models.TextField()
    from_lat = models.FloatField()
    from_long= models.FloatField()
    to_lat=models.FloatField()
    to_long = models.FloatField()
    car_cancellation=models.BooleanField()

class Dummy(models.Model):
    x = models.IntegerField()
