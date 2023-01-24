from django.urls import path
from .views import *

urlpatterns = [
    path('', login, name="login"),
    path('register', register, name="register"),
    path('otp', otp, name ="otp" ),
    path('dashboard',welcome, name="welcome"),
]