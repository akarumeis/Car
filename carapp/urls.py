from django.urls import path
from .views import *

urlpatterns = [
    path('', show_registration, name='reg_form'),
    path('login/', show_login, name='log_form'),
    path('car/', show_car, name='car')
]

