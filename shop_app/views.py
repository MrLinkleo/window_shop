from django.shortcuts import render, redirect
from .models import Film, CartItem, Cart
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

def home(request):
    return render(request, 'shop_app/home.html')  # Показываем шаблон 'home.html'

def view_sun_film(request):
    sun_films = Film.objects.filter(category='sun')
    context = {
        "view_sun_film": sun_films  # Передаём список пленок в контекст с именем "view_sun_film"
    }
    return render(request, "shop_app/view_sun_film.html", context=context)


def view_security_film(request):
    security_films = Film.objects.filter(category='security')
    context = {
        "security_films": security_films  # Передаём список защитных пленок в контекст
    }
    return render(request, 'shop_app/view_security_film.html', context=context)

def view_decoration_film(request):
    decoration_films = Film.objects.filter(category='decoration')
    context = {
        "decoration_films": decoration_films  # Передаём список декоративных пленок в контекст
    }
    return render(request, 'shop_app/view_decoration_film.html', context=context)

@login_required
def add_to_cart(request, product_id):
    # Получаем товар по ID
    product = Film.objects.get(id=product_id)
    
    # Проверяем, есть ли уже корзина у пользователя
    cart, created = Cart.objects.get_or_create(user=request.user)
    
    # Проверяем, есть ли уже товар в корзине
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    
    # Если товар уже есть, увеличиваем его количество
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    return JsonResponse({'message': 'Товар добавлен в корзину', 'cart_count': cart.items.count()})

@login_required
def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, 'shop_app/cart.html', {'cart': cart})