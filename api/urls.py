from django.urls import path
from django.contrib import admin
from .views import RoomView

urlpatterns = [
    path('room/',RoomView.as_view())
]