from django.db import models
from django.utils import timezone
from django.http import HttpResponseForbidden
from accounts.models import Guest
# Create your models here.


class Room(models.Model):
    ROOM_TYPES = (
        ('King', 'King'),
        ('Luxury', 'Luxury'),
        ('Normal', 'Normal'),
        ('Economic', 'Economic'),

    )
    number = models.IntegerField(primary_key=True)
    capacity = models.SmallIntegerField()
    numberOfBeds = models.SmallIntegerField()
    roomType = models.CharField(max_length=20, choices=ROOM_TYPES)
    price = models.FloatField()
    statusStartDate = models.DateField(null=True)
    statusEndDate = models.DateField(null=True)

    def __str__(self):
        return str(self.number)


class Booking(models.Model):
    roomNumber = models.ForeignKey(Room, on_delete=models.CASCADE)
    guest = models.ForeignKey(Guest, null=True, on_delete=models.CASCADE)
    dateOfReservation = models.DateField(default=timezone.now)
    startDate = models.DateField()
    endDate = models.DateField()

    def numOfDep(self):
        return Dependees.objects.filter(booking=self).count()

    def __str__(self):
        return str(self.roomNumber) + " " + str(self.guest)


class Dependees(models.Model):
    booking = models.ForeignKey(Booking,   null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def str(self):
        return str(self.booking) + " " + str(self.name)


class Refund(models.Model):
    guest = models.ForeignKey(Guest,   null=True, on_delete=models.CASCADE)
    reservation = models.ForeignKey(Booking, on_delete=models.CASCADE)
    reason = models.TextField()

    def __str__(self):
        return str(self.guest)


class RoomServices(models.Model):
    SERVICES_TYPES = (
        ('Food', 'Food'),
        ('Cleaning', 'Cleaning'),
        ('Technical', 'Technical'),
    )

    curBooking = models.ForeignKey(
        Booking,   null=True, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    createdDate = models.DateField(default=timezone.now)
    servicesType = models.CharField(max_length=20, choices=SERVICES_TYPES)
    price = models.FloatField()

    def str(self):
        return str(self.curBooking) + " " + str(self.room) + " " + str(self.servicesType)


    
class RoomType(models.Model):
    image = models.ImageField(upload_to='media/roomimages', null=True, blank=True)
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Rooms(models.Model):
    STATUS = (
        ('Available', 'Available'),
        ('Booked', 'Booked'),
    )
    room_number = models.IntegerField(primary_key=True)
    roomType = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    roomPrice = models.FloatField()
    status = models.CharField(max_length=50, choices=STATUS, null=True, blank=True)
    checkout = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return str(f"Room {self.room_number}")    


class RoomDetails(models.Model):
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    roomNumber = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    adults = models.IntegerField()
    children = models.IntegerField()
    
    
    
class GuestDetails(models.Model):
    GENDER_CHOICES = (
        ('M','male'),
        ('F', 'female'),
        ('O', 'other'),
    )
    TITLE_CHOICES = (
        ('Mr', 'Mr'),
        ('Ms', 'Ms'),
        ('Mrs', 'Mrs'),
        ('Dr', 'Dr'),
    )
    phone_number = models.CharField(max_length=14)
    title = models.CharField(max_length=15, choices=TITLE_CHOICES)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    occupation = models.TextField()
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True, blank=True)
    dob = models.DateField()
    nationality = models.CharField(max_length=50, null=True, blank=True)
    contact_det = models.ForeignKey('ContactDetails', on_delete=models.CASCADE, null=True, blank=True)
    
    
class ContactDetails(models.Model):
    CONTACT_TYPE = (
        ('Home', 'Home'),
        ('Personal', 'Personal'),
        ('Official', 'Official'),
        ('Business', 'Business'),
    )
    contact_type = models.CharField(max_length=50, choices=CONTACT_TYPE)
    email = models.EmailField()
    country = models.CharField(max_length=50, default='')
    state = models.CharField(max_length=50, default='')
    city = models.CharField(max_length=50, default='')
    zipcode = models.CharField(max_length=50, default='')
    address = models.TextField()

    
class IdentityDetails(models.Model):
    
    IDENTITY_TYPE = (
        ('NIN', 'NIN'),
        ('PASSPORT', 'PASSPORT'),
        ('VOTER\'S CARD', 'VOTER\'S CARD'),
        ('DRIVER\'S LICENSE', 'DRIVER\'S LICENSE'),
    )
    
    id_type = models.CharField(max_length=60, choices=IDENTITY_TYPE)
    id_number = models.CharField(max_length=255, default='')
    
    # class 
    
class Payment(models.Model):
    PAYMENT_MODE = (
        ('Cash payment','Cash payment'),
        ('Card Payment','Card Payment'),
        ('Bank Transfer', 'Bank Transfer'),
    )
    PAYMENT_STATUS = (
        ('Completed','Completed'),
        ('Pending','Pending'),
    )
    payment_mode = models.CharField(max_length=100, choices=PAYMENT_MODE)
    amount = models.FloatField()
    payment_status = models.CharField(max_length=50, choices=PAYMENT_STATUS)
    date = models.DateField(auto_now=True,null=True, blank=True)
    
    
    
class AdditionalPayment(models.Model):
    title=models.CharField(max_length=255)
    amount=models.IntegerField()
    date_added=models.DateTimeField(auto_now=True)
    date_updated=models.DateTimeField(auto_now=True)
    payments=models.ForeignKey(Payment, on_delete=models.CASCADE)
    
class ReservationDetails(models.Model):
    check_in = models.DateField()
    check_out = models.DateField()
    arrival_from = models.CharField(max_length=255)
    # purpose = models.TextField()
    # remarks = models.TextField()
    reservation_date = models.DateField(auto_now=True)
    date_edited = models.DateTimeField(auto_now=True)
    room_det = models.ForeignKey(RoomDetails, on_delete=models.CASCADE, null=True, blank=True)
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE, null=True, blank=True)
    guest = models.ForeignKey(GuestDetails, on_delete=models.CASCADE, null=True, blank=True)
    payment_det = models.ForeignKey(Payment, on_delete=models.CASCADE, null=True, blank=True)
    # additional_payments = models.ForeignKey()
    
    class Meta:
        ordering = ['-reservation_date', '-date_edited']

    def number_of_days(self):
        check = (self.check_out - self.check_in).days
        if check < 1:
            check = 0
        return check
    
    def total_rent(self):
        return (self.room.roomPrice * ReservationDetails.number_of_days(self))
    
    def payable_amount(self):
        return self.total_rent() - self.payment_det.amount