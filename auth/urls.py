from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login_page, name="login"),
    path('logout/', logout_user, name="logout"),
    path('register/', register_page, name="register"),
    
    path('guests/', guests, name="guests"),
    path('employees/', employees, name="employees"),
    path('tasks/', tasks, name="tasks"),
    path('employee-profile/<str:pk>/', employee_details, name="employee-profile"),
    path('employee-edit/<str:pk>/', employee_details_edit, name="employee-edit"),
    path('employee-add/', add_employee, name="add-employee"),
    path('guest-edit/<str:pk>', guest_edit, name="guest-edit"),
    path('guest-profile/<str:pk>', guest_profile, name="guest-profile"),
    path('completeTask/<str:pk>/', completeTask, name="completeTask"),

]
