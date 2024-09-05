from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseForbidden
from django.db.models import Q, Count
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.models import Group, User

from datetime import datetime, date, timedelta
import random
# Create your views here.
from accounts.models import *
from room.models import *
from hotel.models import *
from .forms import *
from django.core.serializers import serialize
import json
from django.utils import timezone
from django.db.models import Sum




def index(request):
    return render(request, 'guest/index.html')

@login_required(login_url='login')
def accounts_page(request, pk):
    role = str(request.user.groups.all()[0])
    path = role + "/"
    
    user = User.objects.get(id=pk)   
    
    context = {'user':user, "role":role,}
    return render(request, path + "hotels.html", context)

@login_required(login_url='login')
def index_page(request, pk):
    role = str(request.user.groups.all()[0])
    path = role + "/"
    today = timezone.now().date()
    total_amount = Payment.objects.filter(date=today).aggregate(total=Sum("amount"))['total']
    if total_amount is None:
        total_amount = 0
    reserve = ReservationDetails.objects.filter(reservation_date=today).count()
    reservation = ReservationDetails.objects.filter(reservation_date=today).all()
    total_booking = ReservationDetails.objects.all()
    # today
    payment = Payment.objects.all()
    customers = GuestDetails.objects.all()
    
    user = User.objects.get(id=pk)
    context = {
        "user":user,
        "role":role,
        "reserve":reserve,
        "payment":payment,
        "customers":customers,
        "total_booking":total_booking,
        "reservation":reservation,
        "total_amount":total_amount
               }
    return render(request, path + "index.html", context)

@login_required(login_url='login')
def transaction_page(request, pk):
    role = str(request.user.groups.all()[0])
    path = role + "/"
    
    user = User.objects.get(id=pk)
    context = {"user":user, "role":role}
    return render(request, path + "transaction.html", context)


@login_required(login_url='login')
def room_booking_list(request, pk):
    role = str(request.user.groups.all()[0])
    path = role + "/"
    
    user = User.objects.get(id=pk)
    reservation = ReservationDetails.objects.all()
    context = {
        "user":user,
        "role":role,
        "reservation":reservation
        }
    return render(request, path + "room-booking-list.html", context)

@login_required(login_url='login')
def room_booking(request, pk):
    role = str(request.user.groups.all()[0])
    path = role + "/"
    
    user = User.objects.get(id=pk)
    roomtypes = RoomType.objects.all()
    rooms = list(Rooms.objects.values())
    guest_details_instance = GuestDetails()
    contact_details_instance =ContactDetails()
    identity_details_instance = IdentityDetails()
    payment_instance = Payment()
    if request.method == "POST":
        fcheckin = request.POST.get('checkin')
        fcheckout = request.POST.get('checkout')
        farrivalfrom = request.POST.get('arrivalfrom')
        # fpurpose = request.POST.get('purpose')
        # fremarks = request.POST.get('remarks')
        froomtypeid = request.POST.get('roomtype')
        froomnum = request.POST.get('roomnum')
        fadults = request.POST.get('adults')
        fchildren = request.POST.get('children')
        fnumber = request.POST.get('number')
        ftitle = request.POST.get('title')
        fname = request.POST.get('fname')
        flname = request.POST.get('flname')
        foccupation = request.POST.get('occupation')
        fgender = request.POST.get('gender')
        fdob = request.POST.get('dob')
        fnationality = request.POST.get('nationality')
        fcon_type = request.POST.get('con_type')
        femail = request.POST.get('email')
        fcountry = request.POST.get('country')
        fstate = request.POST.get('state')
        fcity = request.POST.get('city')
        fzipcode = request.POST.get('zipcode')
        faddress = request.POST.get('address')
        fidtype = request.POST.get('idtype')
        fidnumber = request.POST.get('idnumber')
        fmode = request.POST.get('pmode')
        fstatus = request.POST.get('pstatus')
        famount = request.POST.get('pamount')
        roomtype = get_object_or_404(RoomType, id=froomtypeid)
        # Fetch the Rooms instance based on the room number
        room_instance = get_object_or_404(Rooms, room_number=froomnum)
        
        reserve =  ReservationDetails(
            check_in = fcheckin,
            check_out = fcheckout,
            arrival_from = farrivalfrom,
            # purpose = fpurpose,
            # remarks = fremarks,
        )
        
        reserve.room = room_instance
        reserve.save()
        room_instance.status = "Booked"
        room_instance.save()
        roomdet = RoomDetails.objects.create(
            room_type = roomtype,
            roomNumber = room_instance,
            adults = fadults,
            children = fchildren,
        )
        roomdet.save()
        reserve.room_det = roomdet
        reserve.save()
        guestdet = GuestDetails(
            phone_number = fnumber,
            title = ftitle,
            first_name = fname,
            last_name = flname,
            occupation = foccupation,
            gender =fgender,
            dob = fdob,
            nationality = fnationality,
          
        )
        guestdet.room = room_instance
        guestdet.save()
        reserve.guest = guestdet
        reserve.save()
        
        con_det = ContactDetails.objects.create(
            contact_type = fcon_type,
            email = femail,
            country = fcountry,
            state = fstate,
            city = fcity,
            zipcode = fzipcode,
            address = faddress
        )
        con_det.save()
        guestdet.contact_det = con_det
        guestdet.save()
        id_det = IdentityDetails.objects.create(
            id_type = fidtype,
            id_number = fidnumber,
        )
        id_det.save()
        payment = Payment(
            payment_mode = fmode,
            payment_status = fstatus,
            amount= famount
            
        )
        payment.save()
        reserve.payment_det = payment
        reserve.save()
        
        # payment
        return redirect("checkin-out", pk=request.user.id)
    context = {
        "user":user,
        "role":role,
        "guest_details_instance":guest_details_instance,
        "roomtypes":roomtypes,
        "payment_instance":payment_instance,
        # "payment":payment,
        "contact_details_instance":contact_details_instance,
        "identity_details_instance":identity_details_instance,
        'rooms': json.dumps(list(rooms)),
        
        }
    return render(request, path + "room-booking.html", context)

@login_required
def checkin_payment(request,pk):
    role = str(request.user.groups.all()[0])
    path = role + '/'

    context ={
        "role":role
    }
    return render(request, path + "check.html", context)

@login_required(login_url='login')
def reservations(request, pk):
    
    role = str(request.user.groups.all()[0])
    path = role + "/"
    
    rooms = Rooms.objects.all()
    reserve = ReservationDetails.objects.all()
    
    user = User.objects.get(id=pk)
    context = {"user":user, "role":role, "rooms": rooms, "reserve":reserve}
    # return render(request, path + "checkin-out.html", context)
    return render(request, path + "reserve.html", context)
    
@login_required(login_url='login')

def checkin_out(request, pk):
    role = str(request.user.groups.all()[0])
    path = role + "/"
    reservation = ReservationDetails.objects.get(id=pk)
    my_dict = {"reservation":reservation, "role":role}
    return render(request, path + "checkin-out.html", context=my_dict)
    
@login_required(login_url='login')
def room_status(request, pk):
    role = str(request.user.groups.all()[0])
    path = role + "/"
    user = User.objects.get(id=pk)
    context = {"user":user, "role":role, }
    return render(request, path + "room-status.html", context)

@login_required(login_url='login')
def item_unit_list(request, pk):
    role = str(request.user.groups.all()[0])
    path = role + "/"
    
    user = User.objects.get(id=pk)
    context = {"user":user, "role":role}
    return render(request, path + "items-unit-list.html", context)

@login_required(login_url='login')
def item_list(request, pk):
    role = str(request.user.groups.all()[0])
    path = role + "/"
    
    user = User.objects.get(id=pk)
    context = {"user":user, "role":role}
    return render(request, path + "items-list.html", context)

@login_required(login_url='login')
def item_destroyed_list(request, pk):
    role = str(request.user.groups.all()[0])
    path = role + "/"
    
    user = User.objects.get(id=pk)
    context = {"user":user, "role":role}
    return render(request, path + "items-destroyed-list.html", context)

@login_required(login_url='login')
def item_category_list(request, pk):
    role = str(request.user.groups.all()[0])
    path = role + "/"
    
    user = User.objects.get(id=pk)
    context = {"user":user, "role":role}
    return render(request, path + "items-category-list.html", context)

@login_required(login_url='login')
def item_suppliers_list(request, pk):
    role = str(request.user.groups.all()[0])
    path = role + "/"
    
    user = User.objects.get(id=pk)
    context = {"user":user, "role":role}
    return render(request, path + "items-suppliers-list.html", context)

@login_required(login_url='login')
def booking_report(request, pk):
    role = str(request.user.groups.all()[0])
    path = role + "/"
    
    user = User.objects.get(id=pk)
    context = {"user":user, "role":role}
    return render(request, path + "booking-report.html", context)

@login_required(login_url='login')
def financial(request, pk):
    role = str(request.user.groups.all()[0])
    path = role + "/"
    
    user = User.objects.get(id=pk)
    context = {"user":user, "role":role}
    return render(request, path + "Financial.html", context)

@login_required(login_url='login')
def financial_ending(request, pk):
    role = str(request.user.groups.all()[0])
    path = role + "/"
    
    user = User.objects.get(id=pk)
    context = {"user":user, "role":role}
    return render(request, path + "Financial_ending.html", context)


@login_required(login_url='login')
def chart_of_account(request, pk):
    role = str(request.user.groups.all()[0])
    path = role + "/"
    
    user = User.objects.get(id=pk)
    context = {"user":user, "role":role}
    return render(request, path + "chart_of_account.html", context)


@login_required(login_url='login')
def opening_balance(request, pk):
    role = str(request.user.groups.all()[0])
    path = role + "/"
    
    user = User.objects.get(id=pk)
    context = {"user":user, "role":role}
    return render(request, path + "opening_balance.html", context)


@login_required(login_url='login')
def debit_voucher(request, pk):
    role = str(request.user.groups.all()[0])
    path = role + "/"
    
    user = User.objects.get(id=pk)
    context = {"user":user, "role":role}
    return render(request, path + "debit_voucher.html", context)

@login_required(login_url='login')
def credit_voucher(request, pk):
    role = str(request.user.groups.all()[0])
    path = role + "/"
    
    user = User.objects.get(id=pk)
    context = {"user":user, "role":role}
    return render(request, path + "credit_voucher.html", context)

@login_required(login_url='login')
def contra_voucher(request, pk):
    role = str(request.user.groups.all()[0])
    path = role + "/"
    
    user = User.objects.get(id=pk)
    context = {"user":user, "role":role}
    return render(request, path + "contra_voucher.html", context)


@login_required(login_url='login')
def journal_voucher(request, pk):
    role = str(request.user.groups.all()[0])
    path = role + "/"
    
    user = User.objects.get(id=pk)
    context = {"user":user, "role":role}
    return render(request, path + "journal_voucher.html", context)

@login_required(login_url='login')
def voucher_approval(request, pk):
    role = str(request.user.groups.all()[0])
    path = role + "/"
    
    user = User.objects.get(id=pk)
    context = {"user":user, "role":role}
    return render(request, path + "voucher_approval.html", context)


@login_required(login_url='login')
def voucher_report(request, pk):
    role = str(request.user.groups.all()[0])
    path = role + "/"
    
    user = User.objects.get(id=pk)
    context = {"user":user, "role":role}
    return render(request, path + "voucher_report.html", context)


@login_required(login_url='login')
def cash_book(request, pk):
    role = str(request.user.groups.all()[0])
    path = role + "/"
    
    user = User.objects.get(id=pk)
    context = {"user":user, "role":role}
    return render(request, path + "cash_book.html", context)

@login_required(login_url='login')
def general_ledger(request, pk):
    role = str(request.user.groups.all()[0])
    path = role + "/"
    
    user = User.objects.get(id=pk)
    context = {"user":user, "role":role}
    return render(request, path + "general_ledger.html", context)


@login_required(login_url='login')
def trial_balance(request, pk):
    role = str(request.user.groups.all()[0])
    path = role + "/"
    
    user = User.objects.get(id=pk)
    context = {"user":user, "role":role}
    return render(request, path + "trial_balance.html", context)


@login_required(login_url='login')
def profit_loss(request, pk):
    role = str(request.user.groups.all()[0])
    path = role + "/"
    
    user = User.objects.get(id=pk)
    context = {"user":user, "role":role}
    return render(request, path + "profit_loss.html", context)


@login_required(login_url='login')
def coa_print(request, pk):
    role = str(request.user.groups.all()[0])
    path = role + "/"
    
    user = User.objects.get(id=pk)
    context = {"user":user, "role":role}
    return render(request, path + "coa_print.html", context)


@login_required(login_url='login')
def balance_sheet(request, pk):
    role = str(request.user.groups.all()[0])
    path = role + "/"
    
    user = User.objects.get(id=pk)
    context = {"user":user, "role":role}
    return render(request, path + "balance_sheet.html", context)



@login_required(login_url='login')
def purchase_report(request, pk):
    role = str(request.user.groups.all()[0])
    path = role + "/"
    
    user = User.objects.get(id=pk)
    context = {"user":user, "role":role}
    return render(request, path + "purchase-report.html", context)

@login_required(login_url='login')
def stuck_report(request, pk):
    role = str(request.user.groups.all()[0])
    path = role + "/"
    
    user = User.objects.get(id=pk)
    context = {"user":user, "role":role}
    return render(request, path + "stock-report.html", context)



@login_required(login_url='login')
def home(request):
    
    if request.user.groups.exists():
        role = str(request.user.groups.all()[0])
    else:
        return HttpResponseForbidden("lolllzzzzz")
    if role != "guest":
        return redirect("dashboard", pk=request.user.id) 
    else:
        return redirect("guest-profile", pk=request.user.id) 
    

@login_required(login_url='login')
def events(request):
    role = str(request.user.groups.all()[0])
    path = role + "/"

    events = Event.objects.all()

    # eventAttendees = EventAttendees.objects.filter(guest = request.user.guest, event = )

    attendedEvents = None
    if role == 'guest':
        attendedEvents = EventAttendees.objects.filter(
            guest=request.user.guest)

    if request.method == "POST":
        if "filter" in request.POST:
            if (request.POST.get("type") != ""):
                events = events.filter(
                    eventType__contains=request.POST.get("type"))

            if (request.POST.get("name") != ""):
                events = events.filter(
                    location__contains=request.POST.get("location"))

            if (request.POST.get("fd") != ""):
                events = events.filter(
                    startDate__gte=request.POST.get("fd"))

            if (request.POST.get("ed") != ""):
                events = events.filter(
                    endDate__lte=request.POST.get("ed"))

            context = {
                "role": role,
                "events": events,
                "type": request.POST.get("type"),
                "location": request.POST.get("location"),
                "fd": request.POST.get("fd"),
                "ed": request.POST.get("ed")
            }
            return render(request, path + "events.html", context)

        if 'Save' in request.POST:
            n = request.POST.get('id-text')
            temp = EventAttendees.objects.get(id=request.POST.get('id-2'))
            temp.numberOfDependees = n
            temp.save()

        if 'attend' in request.POST:  # attend button clicked
            attendedEvents = EventAttendees.objects.filter(
                guest=request.user.guest)
            tempEvent = events.get(id=request.POST.get('id'))
            # print("query set**",attendedEvents)
            # print("**object***",tempEvent)
            # print(tempEvent in attendedEvents)
            check = False
            for t in attendedEvents:
                if t.event.id == tempEvent.id:
                    check = True
                    break
            if not check:  # event not in the query set
                a = EventAttendees(event=tempEvent, guest=request.user.guest)
                a.save()
                return redirect('events')  # refresh page

        elif 'remove' in request.POST:  # remove button clicked
            tempEvent = events.get(id=request.POST.get('id'))
            EventAttendees.objects.filter(
                event=tempEvent, guest=request.user.guest).delete()
            return redirect('events')  # refresh page

    context = {
        "role": role,
        'events': events,
        'attendedEvents': attendedEvents,
        "type": request.POST.get("type"),
        "location": request.POST.get("location"),
        "fd": request.POST.get("fd"),
        "ed": request.POST.get("ed")
    }
    return render(request, path + "events.html", context)


@login_required(login_url='login')
def createEvent(request):
    role = str(request.user.groups.all()[0])
    path = role + "/"

    form = createEventForm()
    if request.method == "POST":
        form = createEventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('events')

    context = {
        'form': form,
        "role": role
    }
    return render(request, path + "createEvent.html", context)


@login_required(login_url='login')
def deleteEvent(request, pk):
    role = str(request.user.groups.all()[0])
    path = role + "/"

    event = Event.objects.get(id=pk)
    if request.method == "POST":
        event.delete()
        return redirect('events')

    context = {
        "role": role,
        'event': event

    }
    return render(request, path + "deleteEvent.html", context)


@ login_required(login_url='login')
def event_profile(request, id):
    role = str(request.user.groups.all()[0])
    path = role + "/"

    tempEvent = Event.objects.get(id=id)
    attendees = EventAttendees.objects.filter(event=tempEvent)

    context = {
        "role": role,
        "attendees": attendees,
        "event": tempEvent
    }
    return render(request, path + "event-profile.html", context)


@ login_required(login_url='login')
def event_edit(request, pk):
    role = str(request.user.groups.all()[0])
    path = role + "/"

    event = Event.objects.get(id=pk)
    form1 = editEvent(instance=event)

    context = {
        "role": role,
        "event": event,
        "form": form1,
    }

    if request.method == "POST":
        form1 = editEvent(request.POST, instance=event)
        if form1.is_valid:
            form1.save()
            return redirect("events")

    return render(request, path + "event-edit.html", context)


@ login_required(login_url='login')
def announcements(request):
    role = str(request.user.groups.all()[0])
    path = role + "/"

    announcements = Announcement.objects.all()
    context = {
        "role": role,
        'announcements': announcements
    }

    if request.method == "POST":
        if 'sendAnnouncement' in request.POST:  # send button clicked
            sender = request.user.employee

            announcement = Announcement(
                sender=sender, content=request.POST.get('textid'))

            announcement.save()
            return redirect('announcements')

        if "filter" in request.POST:
            if (request.POST.get("id") != ""):
                announcements = announcements.filter(
                    id__contains=request.POST.get("id"))

            if (request.POST.get("content") != ""):
                announcements = announcements.filter(
                    content__contains=request.POST.get("content"))

            if (request.POST.get("name") != ""):
                users = User.objects.filter(
                    Q(first_name__contains=request.POST.get("name")) | Q(last_name__contains=request.POST.get("name")))
                employees = Employee.objects.filter(user__in=users)
                announcements = announcements.filter(sender__in=employees)

            if (request.POST.get("date") != ""):
                announcements = announcements.filter(
                    date=request.POST.get("date"))

        context = {
            "role": role,
            'announcements': announcements,
            "id": request.POST.get("id"),
            "name": request.POST.get("name"),
            "content": request.POST.get("content"),
            "date": request.POST.get("date")
        }
        return render(request, path + "announcements.html", context)

    return render(request, path + "announcements.html", context)


@login_required(login_url='login')
def deleteAnnouncement(request, pk):
    role = str(request.user.groups.all()[0])
    path = role + "/"

    announcement = Announcement.objects.get(id=pk)
    if request.method == "POST":
        announcement.delete()
        return redirect('announcements')

    context = {
        "role": role,
        'announcement': announcement

    }
    return render(request, path + "deleteAnnouncement.html", context)


@ login_required(login_url='login')
def storage(request):
    role = str(request.user.groups.all()[0])
    path = role + "/"

    storage = Storage.objects.all()
    context = {
        "role": role,
        'storage': storage
    }
    if request.method == "POST":
        if 'add' in request.POST:
            item = Storage(itemName=request.POST.get("itemName"), itemType=request.POST.get(
                "itemType"), quantitiy=request.POST.get("quantitiy"))
            item.save()
            storage = Storage.objects.all()

        elif 'save' in request.POST:
            id = request.POST.get("id")
            storages = Storage.objects.get(id=id)
            storages.quantitiy = request.POST.get("quantitiy")
            storages.save()

        if "filter" in request.POST:
            if (request.POST.get("id") != ""):
                storage = storage.filter(
                    id__contains=request.POST.get("id"))

            if (request.POST.get("name") != ""):
                storage = storage.filter(
                    itemName__contains=request.POST.get("name"))

            if (request.POST.get("type") != ""):
                storage = storage.filter(
                    itemType__contains=request.POST.get("type"))

        context = {
            "role": role,
            "storage": storage,
            "id": request.POST.get("id"),
            "name": request.POST.get("name"),
            "type": request.POST.get("type"),
            "q": request.POST.get("q"),

        }
        return render(request, path + "storage.html", context)

    return render(request, path + "storage.html", context)


@login_required(login_url='login')
def deleteStorage(request, pk):
    role = str(request.user.groups.all()[0])
    path = role + "/"

    storage = Storage.objects.get(id=pk)
    if request.method == "POST":
        storage.delete()
        return redirect('storage')

    context = {
        "role": role,
        'storage': storage

    }
    return render(request, path + "deleteStorage.html", context)


@login_required(login_url='login')
def food_menu(request):
    role = str(request.user.groups.all()[0])
    path = role + "/"
    print(request.POST)
    if request.method == "POST":
        if 'add' in request.POST:
            foodmenu = FoodMenu(menuItems=request.POST.get("menuItems"), startDate=request.POST.get(
                "startDate"), endDate=request.POST.get("endDate"))
            foodmenu.save()

    food_menu = FoodMenu.objects.all()
    context = {
        "role": role,
        'food_menu': food_menu
    }
    return render(request, path + "food-menu.html", context)


@login_required(login_url='login')
def deleteFoodMenu(request, pk):
    role = str(request.user.groups.all()[0])
    path = role + "/"

    food_menu = FoodMenu.objects.get(pk=pk)
    if request.method == "POST":
        food_menu.delete()
        return redirect('food-menu')

    context = {
        "role": role,
        'food_menu': food_menu

    }
    return render(request, path + "deleteFoodMenu.html", context)


@login_required(login_url='login')
def food_menu_edit(request, pk):
    role = str(request.user.groups.all()[0])
    path = role + "/"
    print(request.POST)
    food_menu = FoodMenu.objects.get(pk=pk)
    form1 = editFoodMenu(request.POST, instance=food_menu)
    if request.method == "POST":
        if form1.is_valid():
            form1.save()
            return redirect("food-menu")

    context = {
        "role": role,
        'food_menu': food_menu
    }
    return render(request, path + "food-menu-edit.html", context)


@ login_required(login_url='login')
def error(request):
    role = str(request.user.groups.all()[0])
    path = role + "/"

    context = {
        "role": role
    }
    return render(request, path + "error.html", context)


@login_required(login_url='login')
def payment(request):
    role = str(request.user.groups.all()[0])
    path = role

    # create random string:
    # generating the random code to be sent to the email
    import random
    import string
    code = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase)
                   for _ in range(10))

    context = {
        "role": role,
        "code": code

    }

    def send(request, receiver, code):
        subject = "Payment Verification"
        text = """ 
            Dear {guestName},
            Please Copy Paste This Code in the verification Window:

            {code}

            Please ignore this email, if you didn't initiate this transaction!
        """
        # placing the code and user name in the email bogy text
        email_text = text.format(
            guestName=receiver.user.first_name + " " + receiver.user.last_name, code=code)

        # seting up the email
        message_email = 'hms@support.com'
        message = email_text
        receiver_name = receiver.user.first_name + " " + receiver.user.last_name

        # send email
        send_mail(
            receiver_name + " " + subject,  # subject
            message,  # message
            message_email,  # from email
            [receiver.user.email],  # to email
            fail_silently=False,  # for user in users :
            # user.email
        )

        messages.success(
            request, 'Verification email Was Successfully Sent')

        # do something ???
        return render(request, path + "/verify.html", context)
    if role == "guest":
        send(request, request.user.guest, code)
    elif role == "receptionist":
        send(request, Booking.objects.all().last().guest, code)

    return render(request, path + "/payment.html", context)


@login_required(login_url='login')
def verify(request):
    role = str(request.user.groups.all()[0])
    path = role + "/"
    if request.method == "POST":
        tempCode = request.POST.get("tempCode")
        if "verify" in request.POST:
            realCode = request.POST.get("realCode")

            if realCode == tempCode:
                messages.success(request, "Successful Booking")
            else:
                Booking.objects.all().last().delete()
                messages.warning(request, "Invalid Code")

            return redirect("rooms")
    context = {
        "role": role,
        "code": tempCode

    }
    return render(request, path + "verify.html", context)
