from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(MenuItem)
admin.site.register(Order)
admin.site.register(OrderItem)

class MenuAdmin(admin.ModelAdmin):
    list_display =['name']
    
admin.site.register(Menu, MenuAdmin)
