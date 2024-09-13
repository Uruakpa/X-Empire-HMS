from django.urls import path
from .views import *


urlpatterns = [
    path('menu/<int:pk>/', menu_views,name="menu"),
    path("add-menu/", add_menu, name="add-menu"),
    path("delete-menu/<str:foo>/",delete_menu, name="delete-menu"),
    path("add-menuitems", add_menuitem, name="add-menuitem"),
    path("menu-list/<str:foo>/", menulist, name="menulist"),
]
