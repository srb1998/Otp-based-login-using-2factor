from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager

# Create your models here.

class User(AbstractUser):
    username = None
    phone_number = models.CharField(max_length=12, unique=True)
    name = models.CharField(max_length=100 ,null=True)   
    password = models.CharField(max_length=50)
    is_phone_verified = models.BooleanField(default=False)
    otp = models.CharField(max_length=6)
    
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []
    objects = UserManager()