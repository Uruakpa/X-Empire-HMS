from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import *
from django.contrib import messages

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
def menulist(request, foo):
    role = str(request.user.groups.all()[0])
    path = role + "/"
    # user = User.objects.get(id=pk)
    foo = foo.replace('-', '')
    menu = Menu.objects.get(name=foo)
    menuitems = MenuItem.objects.filter(category=menu)
    
    context = {
        "menu":menu,
        "menuitems":menuitems
    }
    return render(request, path + "menulist.html", context)


def add_menu(request):
    role = str(request.user.groups.all()[0])
    path = role + "/"
    
    form = MenuForm()
    if request.method == "POST":
        form = MenuForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, f"Menu added")
    
    context = {
        "form":form,
        "role":role
    }        
    return render(request,path + "add-menu.html", context)
           

def add_menuitem(request):
    role = str(request.user.groups.all()[0])
    path = role + "/"
    form = MenuItemForm()
    if request.method == "POST":
        form = MenuItemForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, f"Menu added")
            
        else:
            form = MenuItemForm()
            
    context = {
        "form":form,
        "role":role
    }    

    return render(request,path + "add-menuitem.html", context)


def delete_menu(request, foo):
    role = str(request.user.groups.all()[0])
    path = role + '/'
    menu = Menu.objects.get(id=foo)
    if request.method == "POST":
        menu.delete()
        return redirect(to="menu", pk=request.user.id)
        
    my_dict = {
        "menu":menu,
    }
    return render(request, path + "delete-menu.html", context=my_dict)