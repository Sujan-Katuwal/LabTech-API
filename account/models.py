from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    username = models.CharField(max_length=225, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)
    gender = models.CharField(max_length=10, choices=(('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')))
    address = models.TextField()
    role = models.CharField(max_length=20, choices=(('Admin', 'Admin'), ('User', 'User'), ('Doctor', 'Doctor')))

