from django.urls import path
from .views import *

urlpatterns = [
    path('bookings/', bookings, name="bookings"),
    path('rooms/', rooms, name="rooms"),
    path('room-services/', room_services, name="room-services"),
    path('refunds/', refunds, name="refunds"),

    path('current-room-services/', current_room_services,
         name="current-room-services"),
    path('request-refund/', request_refund, name="request-refund"),
    path('room-profile/<str:id>/', room_profile, name="room-profile"),
    path('room-edit/<str:pk>/', room_edit, name="room-edit"),

    path('booking-make/', booking_make, name="booking-make"),


    path('deleteBooking/<str:pk>/', deleteBooking, name="deleteBooking"),
]
