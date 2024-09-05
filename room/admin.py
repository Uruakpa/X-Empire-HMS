from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Room)
admin.site.register(Booking)
admin.site.register(Dependees)
admin.site.register(RoomServices)
admin.site.register(Refund)
admin.site.register(RoomType)
admin.site.register(Rooms)
admin.site.register(RoomDetails)
admin.site.register(GuestDetails)
admin.site.register(ContactDetails)
admin.site.register(IdentityDetails)
admin.site.register(ReservationDetails)
admin.site.register(Payment)

