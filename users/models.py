from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models


class User(AbstractUser):
    full_name = models.CharField('Имя', max_length=50, blank=True, null=True)
    phone_number = PhoneNumberField('Номер телефона', unique=True, blank=True, null=True)
    image = models.ImageField('Аватарка', upload_to='users/', blank=True, null=True)

    def __str__(self):
        return self.username

