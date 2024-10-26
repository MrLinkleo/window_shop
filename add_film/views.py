from django.shortcuts import render, redirect, get_object_or_404
from .forms import SunFilmForm

def add_film(request):
    if request.method == 'POST':
        form = SunFilmForm(request.POST, request.FILES)  # Обработка загружаемых файлов
        if form.is_valid():
            form.save()  # Сохранение нового объекта в базе данных
            return redirect('shop_app:home')  # Перенаправление на другую страницу (например, на список фильмов)
    else:
        form = SunFilmForm()

    return render(request, 'add_film/add_film.html', {'form': form})
