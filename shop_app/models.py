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
    stock = models.PositiveBigIntegerField(default=0)  # Количество должно быть числом
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=0)
    image = models.ImageField(upload_to='films/', default='films/default_image.jpg')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='sun')
    
    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"
    
    def delete(self, *args, **kwargs):
        if self.image:
            self.image.delete()
        super().delete(*args, **kwargs)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Корзина пользователя {self.user.username}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Film, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def get_total_price(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.product.name} ({self.quantity} шт.)"