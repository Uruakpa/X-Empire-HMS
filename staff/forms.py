from django.forms import ModelForm
from .models import *

class MenuForm(ModelForm):
    class Meta:
        model = Menu
        fields = ["name"]

class MenuItemForm(ModelForm):
    class Meta:
        model = MenuItem
        fields = "__all__"