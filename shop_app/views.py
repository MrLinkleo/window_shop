from django.shortcuts import render
from .models import Film

def home(request):
    return render(request, 'shop_app/home.html')  # Показываем шаблон 'home.html'

def view_sun_film(request):
    sun_films = Film.objects.all()  # Получаем все пленки из базы данных
    context = {
        "view_sun_film": sun_films  # Передаём список пленок в контекст с именем "view_sun_film"
    }
    return render(request, "shop_app/view_sun_film.html", context=context)


def view_security_film(request):
    security_films = Film.objects.all()  # Получаем все защитные пленки из базы данных
    context = {
        "security_films": security_films  # Передаём список защитных пленок в контекст
    }
    return render(request, 'shop_app/view_security_film.html', context=context)

def view_decoration_film(request):
    decoration_films = Film.objects.all()  # Получаем все декоративные пленки из базы данных
    context = {
        "decoration_films": decoration_films  # Передаём список декоративных пленок в контекст
    }
    return render(request, 'shop_app/view_decoration_film.html', context=context)

