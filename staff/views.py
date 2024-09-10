from django.shortcuts import render
from .models import *
# Create your views here.

def menuitem_views(request):
    role = str(request.user.groups.all()[0])
    path = role + "/"
    
    menuitem = MenuItem.objects.all()
    context = {"menuitem":menuitem}
    return render(request, path + "menuitems.html", context)

def menu_views(request):
    role = str(request.user.groups.all()[0])
    path = role + "/"
    
    menu = Menu.objects.all()
    context = {
        "role":role,
        "menu":menu
    }
    return render(request, path + "menulist.html", context)

