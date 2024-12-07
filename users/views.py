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

@require_POST
def register_view(request):
    try:
        data = json.loads(request.body)

        username = data.get('username')
        email = data.get('email')
        password1 = data.get('password1')
        password2 = data.get('password2')

        if password1 != password2:
            return JsonResponse({"status": "error", "message": "Пароли не совпадают"}, status=400)

        if User.objects.filter(username=username).exists():
            return JsonResponse({"status": "error", "message": "Пользователь с таким именем уже существует"}, status=400)

        if User.objects.filter(email=email).exists():
            return JsonResponse({"status": "error", "message": "Пользователь с таким email уже существует"}, status=400)

        user = User.objects.create_user(username=username, email=email, password=password1)

        login(request, user)

        return JsonResponse({"status": "success", "message": "Регистрация успешна"})
    except Exception as e:
        return JsonResponse({"status": "error", "message": f"Ошибка на сервере: {str(e)}"}, status=500)

@require_POST
def login_view(request):
    try:
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

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
    print("Рендеринг страницы профиля")
    return render(request, 'users/profile.html')

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return JsonResponse({"status": "success", "message": "Выход успешен."}, status=200)
    return JsonResponse({"status": "error", "message": "Метод не разрешен."}, status=405)

def home_view(request):
    return render(request, 'shop_app/home.html')
