# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class User(AbstractUser):
    full_name = models.CharField(
        'Имя',
        max_length=50,
        blank=True,
        null=True
    )
    phone_number = PhoneNumberField(
        'Номер телефона',
        unique=True
    )
    image = models.ImageField(
        'Аватарка',
        upload_to='users/',
        blank=True
    )
