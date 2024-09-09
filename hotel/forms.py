from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from .models import *
from room.models import *


class editFoodMenu(ModelForm):
    class Meta:
        model = FoodMenu
        fields = ["menuItems", "startDate", "endDate"]


class editEvent(ModelForm):
    class Meta:
        model = Event
        fields = ["eventType", "location",
                  "startDate", "endDate", "explanation"]


class createEventForm(ModelForm):
    class Meta:
        model = Event
        fields = ["eventType", "location",
                  "startDate", "endDate", "explanation"]


class createAnnouncementForm(ModelForm):
    class Meta:
        model = Announcement
        fields = '__all__'


class createItem(ModelForm):
    class Meta:
        model = Storage
        fields = ["itemName", "itemType", "quantitiy"]


class ReservationForm(ModelForm):
    class Meta:
        model = ReservationDetails
        fields = ['check_in','check_out','arrival_from']
        
class PaymentForm(ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'

class AdditionalPaymentForm(ModelForm):
    class Meta:
        model = AdditionalPayment
        fields = ['title', 'amount', 'payments']
        
class GuestForm(ModelForm):
    class Meta:
        model = GuestDetails
        fields = '__all__'
        
class RoomdetailsForm(ModelForm):
    class Meta:
        model = RoomDetails
        fields = '__all__'
        
class ContactForm(ModelForm):
    class Meta:
        model = ContactDetails
        fields = '__all__'

class IdentityForm(ModelForm):
    class Meta:
        model = IdentityDetails
        fields = '__all__'