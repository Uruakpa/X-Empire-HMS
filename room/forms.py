from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import *


class editRoom(ModelForm):
    class Meta:
        model = Room
        fields = ["capacity", "numberOfBeds", "roomType", "price"]


class editBooking(ModelForm):
    class Meta:
        model = Booking
        fields = ["startDate", "endDate"]


class editDependees(ModelForm):
    class Meta:
        model = Dependees
        fields = ["booking", "name"]

class roomTypeForm(ModelForm):
    class Meta:
        model = RoomType
        fields = "__all__"
         
         
class roomForm(ModelForm):
    class Meta:
        model = Rooms
        fields = "__all__"         