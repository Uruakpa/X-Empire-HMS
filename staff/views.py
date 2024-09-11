from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

@login_required(login_url='login')
def menuitem_views(request, pk):
    role = str(request.user.groups.all()[0])
    path = role + "/"
    
    user = User.objects.get(id=pk)
    
    menuitem = MenuItem.objects.all()
    context = {"menuitem":menuitem}
    return render(request, path + "menuitems.html", context)

@login_required(login_url='login')
def menu_views(request,pk):
    role = str(request.user.groups.all()[0])
    path = role + "/"
    user = User.objects.get(id=pk)
    menu = Menu.objects.all()
    context = {
        "role":role,
        "menu":menu
    }
    return render(request, path + "menu.html", context)

@login_required(login_url='login')
def menulist(request, foo,pk):
    role = str(request.user.groups.all()[0])
    path = role + "/"
    user = User.objects.get(id=pk)
    foo = foo.replace('-', '')
    menu = Menu.objects.get(name=foo)
    menuitems = MenuItem.objects.filter(menu=menu)
    
    context = {
        "menu":menu,
        "menuitems":menuitems
    }
    return render(request, path + "menulist.html", context)


    
    
