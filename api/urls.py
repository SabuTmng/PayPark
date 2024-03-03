from .views import *
from django.urls import path

urlpatterns = [
    path("member/", Member.as_view()),
    path("parking/", Parking.as_view()),
    path("booking/", Booking.as_view()),
    path("payment/", Payment.as_view()),
    path("roles/", Roles.as_view()),
]