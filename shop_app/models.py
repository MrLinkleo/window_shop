from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Film(models.Model):
    CATEGORY_CHOICES = [
        ('sun', 'Sun Film'),
        ('security', 'Security Film'),
        ('decoration', 'Decoration Film'),
    ]
    
    name = models.CharField(max_length=100, default='Нет названия')
    description = models.TextField(default='Нет описания')
    quantity = models.PositiveBigIntegerField(default=0)  # Количество должно быть числом
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    image = models.ImageField(upload_to='films/', default='films/default_image.jpg')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='sun')
    
    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"
    
    def delete(self, *args, **kwargs):
        if self.image:
            self.image.delete()
        super().delete(*args, **kwargs)