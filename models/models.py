from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# Create your models her
class Users(AbstractBaseUser):
    role = models.ForeignKey("Roles", on_delete=models.CASCADE)
    contact = models.CharField(max_length=15)
    district = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255)
    password = models.CharField(max_length=255)


class Roles(models.Model):
    role_name = models.CharField(max_length=255)


class Booking(models.Model):
    user = models.ManyToManyField("Users", "user")
    parking = models.ForeignKey("Parking", on_delete=models.CASCADE)
    parking_from = models.TimeField()
    parking_to = models.TimeField()


class Parking(models.Model):
    user = models.ManyToManyField("Users")
    location = models.CharField(max_length=255)
    latitude = models.CharField(max_length=255)
    longitude = models.CharField(max_length=255)


class ParkingDetails(models.Model):
    parking = models.ForeignKey("Parking", on_delete=models.CASCADE)
    vechicle_type = models.CharField(max_length=255)
    price_hour = models.CharField(max_length=255)

class Payment(models.Model):
    booking = models.ForeignKey("Booking", on_delete=models.DO_NOTHING)
    total_price = models.CharField(max_length=255)