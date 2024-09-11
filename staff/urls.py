from django.urls import path
from .views import *


urlpatterns = [
    path('menu/', menu_views,name=""),
    path("add-menu", add_menu, name="add-menu"),
    path("add-menuitems", add_menuitem, name="add-menuitem"),
]
