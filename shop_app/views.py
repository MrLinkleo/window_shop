import json
from django.shortcuts import render, get_object_or_404
from .models import Film, CartItem, Cart, CartItem
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.db.models import Sum
from django.conf import settings
from weasyprint import HTML
from django.http import HttpResponse
from django.template.loader import render_to_string



def home(request):
    return render(request, 'shop_app/home.html', {'MEDIA_URL': settings.MEDIA_URL})  # Показываем шаблон 'home.html'

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

@require_POST
@login_required
def add_to_cart(request, product_id):
    # Получаем данные из POST-запроса
    data = json.loads(request.body)
    product_id = data.get('productId')
    quantity = int(data.get('quantity'))  # Преобразуем quantity в целое число

    # Получаем товар по ID
    product = get_object_or_404(Film, id=product_id)
    
    # Проверяем, есть ли уже корзина у пользователя
    cart, created = Cart.objects.get_or_create(user=request.user)
    
    # Проверяем, есть ли уже товар в корзине
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    
    # Если товар уже есть, увеличиваем его количество
    if not created:
        cart_item.quantity += quantity  # Увеличиваем количество на заданное значение
        cart_item.save()
    
    # Ответ с информацией о корзине
    return JsonResponse({'message': 'Товар добавлен в корзину', 'cart_count': cart.items.count()})


@login_required
def view_cart(request):
    # Получаем корзину текущего пользователя
    cart = Cart.objects.filter(user=request.user).first()

    if cart:
        # Получаем все товары в корзине
        cart_items = cart.items.all()

        # Считаем общую сумму
        total_price = sum(item.get_total_price() for item in cart_items)
    else:
        cart_items = []
        total_price = 0

    # Передаем в шаблон данные о корзине
    return render(request, 'shop_app/cart.html', {
        'cart_items': cart_items,
        'total_price': total_price,
    })

# Обновление количества товара в корзине
def update_cart_item(request):
    if request.method == "POST":
        cart_item_id = request.POST.get('cart_item_id')
        quantity = int(request.POST.get('quantity'))
        
        # Получаем элемент корзины
        cart_item = get_object_or_404(CartItem, id=cart_item_id)
        
        # Обновляем количество
        cart_item.quantity = quantity
        cart_item.save()
        
        # Возвращаем обновленную информацию о корзине
        total_price = sum(item.get_total_price() for item in cart_item.cart.items.all())
        return JsonResponse({'success': True, 'total_price': total_price, 'quantity': cart_item.quantity})
    return JsonResponse({'success': False})

# Удаление товара из корзины
def delete_cart_item(request):
    if request.method == 'POST':
        cart_item_id = request.POST.get('cart_item_id')  # Получаем ID товара, который нужно удалить
        try:
            cart_item = CartItem.objects.get(id=cart_item_id)  # Находим товар в корзине
            cart_item.delete()  # Удаляем товар
            # Пересчитываем общую сумму корзины
            total_price = sum(item.get_total_price() for item in CartItem.objects.all())
            return JsonResponse({'success': True, 'total_price': total_price})
        except CartItem.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Товар не найден'})
    return JsonResponse({'success': False, 'message': 'Ошибка при удалении товара'})

def contacts(request):
    return render(request, 'shop_app/contacts.html')

@login_required
def generate_invoice(request):
    # Получаем корзину для текущего пользователя
    try:
        cart = Cart.objects.get(user=request.user)
    except Cart.DoesNotExist:
        cart = None

    if cart:
        # Получаем все товары из корзины
        cart_items = CartItem.objects.filter(cart=cart)
        total_price = sum(item.get_total_price() for item in cart_items)

        return render(request, 'shop_app/invoice_template.html', {
            'cart_items': cart_items,
            'total_price': total_price,
        })
    else:
        return render(request, 'shop_app/invoice_template.html', {
            'error': "У вас нет корзины или корзина пуста.",
        })