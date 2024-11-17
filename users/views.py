import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseNotAllowed
from django.shortcuts import render
from users.models import User
from django.contrib.auth.forms import UserCreationForm

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Сохраняем пользователя
            login(request, user)  # Автоматический вход после регистрации
            return JsonResponse({"status": "success", "message": "Регистрация прошла успешно"})
        else:
            return JsonResponse({"status": "error", "message": "Неверные данные"})
    else:
        return JsonResponse({"status": "error", "message": "Неверный метод запроса"})

def login_view(request):
    if request.method == "POST":
        try:
            # Получаем данные из тела запроса в формате JSON
            data = json.loads(request.body)
            username = data.get("username")
            password = data.get("password")

            # Аутентификация пользователя
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return JsonResponse({"status": "success", "message": "Вход успешен."}, status=200)
            else:
                return JsonResponse({"status": "error", "message": "Неверное имя пользователя или пароль."}, status=400)

        except KeyError:
            return JsonResponse({"status": "error", "message": "Некорректные данные."}, status=400)
        except Exception as e:
            return JsonResponse({"status": "error", "message": f"Ошибка: {str(e)}"}, status=500)

    return JsonResponse({"status": "error", "message": "Неверный метод запроса."}, status=405)

@login_required
def profile_view(request):
    return render(request, 'users/profile.html', {'user': request.user})

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return JsonResponse({"status": "success", "message": "Выход успешен."}, status=200)
    return JsonResponse({"status": "error", "message": "Метод не разрешен."}, status=405)

def home_view(request):
    return render(request, 'shop_app/home.html')
