import json
from django.shortcuts import render, get_object_or_404
from .models import Film, CartItem, Cart, CartItem
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.db.models import Sum
from django.conf import settings



def home(request):
    return render(request, 'shop_app/home.html', {'MEDIA_URL': settings.MEDIA_URL})

def view_sun_film(request):
    sun_films = Film.objects.filter(category='sun')
    context = {
        "view_sun_film": sun_films
    }
    return render(request, "shop_app/view_sun_film.html", context=context)


def view_security_film(request):
    security_films = Film.objects.filter(category='security')
    context = {
        "security_films": security_films
    }
    return render(request, 'shop_app/view_security_film.html', context=context)

def view_decoration_film(request):
    decoration_films = Film.objects.filter(category='decoration')
    context = {
        "decoration_films": decoration_films
    }
    return render(request, 'shop_app/view_decoration_film.html', context=context)

@require_POST
@login_required
def add_to_cart(request, product_id):
    data = json.loads(request.body)
    product_id = data.get('productId')
    quantity = int(data.get('quantity'))

    product = get_object_or_404(Film, id=product_id)
    
    cart, created = Cart.objects.get_or_create(user=request.user)
    
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    
    if not created:
        cart_item.quantity += quantity
        cart_item.save()
    
    return JsonResponse({'message': 'Товар добавлен в корзину', 'cart_count': cart.items.count()})


@login_required
def view_cart(request):
    cart = Cart.objects.filter(user=request.user).first()

    if cart:
        cart_items = cart.items.all()

        total_price = sum(item.get_total_price() for item in cart_items)
    else:
        cart_items = []
        total_price = 0

    return render(request, 'shop_app/cart.html', {
        'cart_items': cart_items,
        'total_price': total_price,
    })

def update_cart_item(request):
    if request.method == "POST":
        cart_item_id = request.POST.get('cart_item_id')
        quantity = int(request.POST.get('quantity'))
        
        cart_item = get_object_or_404(CartItem, id=cart_item_id)
        
        cart_item.quantity = quantity
        cart_item.save()
        
        total_price = sum(item.get_total_price() for item in cart_item.cart.items.all())
        return JsonResponse({'success': True, 'total_price': total_price, 'quantity': cart_item.quantity})
    return JsonResponse({'success': False})

def delete_cart_item(request):
    if request.method == 'POST':
        cart_item_id = request.POST.get('cart_item_id') 
        try:
            cart_item = CartItem.objects.get(id=cart_item_id)
            cart_item.delete()
            total_price = sum(item.get_total_price() for item in CartItem.objects.all())
            return JsonResponse({'success': True, 'total_price': total_price})
        except CartItem.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Товар не найден'})
    return JsonResponse({'success': False, 'message': 'Ошибка при удалении товара'})

def contacts(request):
    return render(request, 'shop_app/contacts.html')

@login_required
def generate_invoice(request):
    try:
        cart = Cart.objects.get(user=request.user)
    except Cart.DoesNotExist:
        cart = None

    if cart:
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
    
def view_services(request):
    return render(request, 'shop_app/services.html')

def view_online_store(request):
    return render(request, 'shop_app/online_store.html')