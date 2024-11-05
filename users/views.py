from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm
from django.contrib.auth import logout

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Автоматический вход после регистрации
            return redirect('home')  # Перенаправление на домашнюю страницу
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    error_message = None  # Инициализируем переменную
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Перенаправление на домашнюю страницу
        else:
            error_message = "Неверное имя пользователя или пароль."  # Устанавливаем сообщение об ошибке
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form, 'error_message': error_message})

def logout_view(request):
    logout(request)
    return redirect('home')
