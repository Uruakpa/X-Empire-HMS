"""HMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views


    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin as django_admin
from django.urls import path, include
from django.conf.urls.static import static
from authapp.views import *
from room.views import *
from django.conf import settings
# from hotel.views import *

urlpatterns = [
    path('admin-site/', django_admin.site.urls),
    path('', include("hotel.urls")),
    path('room/', include("room.urls")),
    path('auth/', include("authapp.urls")),
    path('staff/', include("staff.urls")),
    path('guest/', include("guest.urls")),
    
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)