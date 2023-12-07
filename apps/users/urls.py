from django.urls import path
from apps.users import users

urlpatterns = [
    path('', users.Notes.as_view()),
    path('<str:pk>', users.NoteDetail.as_view())
]