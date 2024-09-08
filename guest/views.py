from django.shortcuts import render
from hotel.forms import *
# Create your views here.
def create_reservations(request):
    form = ReservationForm