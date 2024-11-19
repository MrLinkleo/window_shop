import json
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from users.models import User
from django.views.decorators.csrf import csrf_exempt
from .forms import UserCreationForm
from django.views.decorators.http import require_POST
from django.contrib.auth import authenticate, login

User = get_user_model()

@csrf_exempt  # Отключаем CSRF-проверку, если это нужно
def register_view(request):
    try:
        # Чтение JSON-данных из тела запроса
        data = json.loads(request.body)

        # Передаем данные в форму для валидации
        form = UserCreationForm(data)

        if form.is_valid():
            # Сохраняем пользователя, если форма валидна
            user = form.save()

            # Логиним пользователя
            login(request, user)

            # Отправляем успешный ответ
            return JsonResponse({"status": "success", "message": "Регистрация прошла успешно"})
        else:
            # Возвращаем ошибку, если форма не валидна
            return JsonResponse({"status": "error", "message": form.errors.as_json()})

    except json.JSONDecodeError:
        # Возвращаем ошибку, если JSON-формат некорректен
        return JsonResponse({"status": "error", "message": "Ошибка в формате JSON"})

@require_POST
def login_view(request):
    try:
        # Получаем данные из тела запроса в формате JSON
        data = json.loads(request.body)

        username = data.get('username')
        password = data.get('password')

        # Проверяем данные пользователя
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({"status": "success", "message": "Успешный вход"})
        else:
            return JsonResponse({"status": "error", "message": "Неверные данные для входа"})
    except json.JSONDecodeError:
        return JsonResponse({"status": "error", "message": "Ошибка обработки данных"})

@login_required
def profile_view(request):
    print("Рендеринг страницы профиля")  # Отладочная информация
    return render(request, 'users/profile.html')

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return JsonResponse({"status": "success", "message": "Выход успешен."}, status=200)
    return JsonResponse({"status": "error", "message": "Метод не разрешен."}, status=405)

def home_view(request):
    return render(request, 'shop_app/home.html')
