from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Role)
admin.site.register(Booking)
admin.site.register(Parking)
admin.site.register(ParkingDetail)
admin.site.register(Payment)


