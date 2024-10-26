from django.db import models

class SunFilm(models.Model):
    name = models.CharField(max_length=100, default='Нет названия')
    description = models.TextField(default='Нет описания')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    image = models.ImageField(upload_to='sun_films/', default='default_image.jpg')
    # Добавьте другие необходимые поля

class SecurityFilm(models.Model):
    name = models.CharField(max_length=100, default='Нет названия')
    description = models.TextField(default='Нет описания')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    image = models.ImageField(upload_to='security_films/', default='default_image.jpg')
    # Добавьте другие необходимые поля

class DecorationFilm(models.Model):
    name = models.CharField(max_length=100, default='Нет названия')
    description = models.TextField(default='Нет описания')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    image = models.ImageField(upload_to='decoration_films/', default='default_image.jpg')
    # Добавьте другие необходимые поля

    def __str__(self):
        return self.name