from django.shortcuts import render
from .models import SunFilm, SecurityFilm, DecorationFilm

def home(request):
    return render(request, 'shop_app/home.html')  # Показываем шаблон 'home.html'

def view_sun_film(request):
    sun_films = SunFilm.objects.all()  # Получаем все пленки из базы данных
    context = {
        "sun_films": sun_films  # Передаём список пленок в контекст
    }
    return render(request, "shop_app/view_sun_film.html", context=context)

def view_security_film(request):
    security_films = SecurityFilm.objects.all()  # Получаем все защитные пленки из базы данных
    context = {
        "security_films": security_films  # Передаём список защитных пленок в контекст
    }
    return render(request, 'shop_app/view_security_film.html', context=context)

def view_decoration_film(request):
    decoration_films = DecorationFilm.objects.all()  # Получаем все декоративные пленки из базы данных
    context = {
        "decoration_films": decoration_films  # Передаём список декоративных пленок в контекст
    }
    return render(request, 'shop_app/view_decoration_film.html', context=context)