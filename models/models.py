from django.db import models
from django.contrib.auth.models import AbstractUser
from djangoProject.mangaers import CustomUserManager
# Create your models her
class User(AbstractUser):
    username = None
    role = models.ForeignKey("Role", on_delete=models.CASCADE, null=True)
    is_admin = models.BooleanField(default=False)
    first_name =models.CharField(max_length=255)
    last_name =models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    contact = models.CharField(max_length=15)
    district = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)
    zip_code = models.CharField(max_length=255)

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'
    objects = CustomUserManager()

    def __str__(self):
        return str(self.id)


class Role(models.Model):
    role_name = models.CharField(max_length=255)

    def __str__(self):
        return self.role_name


class Booking(models.Model):
    user = models.ManyToManyField("User", "user")
    parking = models.ForeignKey("Parking", on_delete=models.CASCADE)
    parking_from = models.TimeField()
    parking_to = models.TimeField()


class Parking(models.Model):
    user = models.ManyToManyField("User")
    location = models.CharField(max_length=255)
    latitude = models.CharField(max_length=255)
    longitude = models.CharField(max_length=255)


class ParkingDetail(models.Model):
    parking = models.ForeignKey("Parking", on_delete=models.CASCADE)
    vechicle_type = models.CharField(max_length=255)
    price_hour = models.CharField(max_length=255)

class Payment(models.Model):
    booking = models.ForeignKey("Booking", on_delete=models.DO_NOTHING)
    total_price = models.CharField(max_length=255)