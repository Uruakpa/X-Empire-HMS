from django.urls import  path
from .views import *

urlpatterns = [
    path("about/", about_page, name="about")
]
