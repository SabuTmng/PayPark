from django.urls import path
from django.urls import include


urlpatterns = [
    path("public", include("apps.users.urls")),
]