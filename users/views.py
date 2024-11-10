from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from django.urls import reverse


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Автоматический вход после регистрации
            return redirect('users:profile')  # Перенаправление в личный кабинет
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    error_message = None

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Перенаправление в личный кабинет
            return redirect(reverse('users:profile'))  # Используем имя маршрута
        else:
            error_message = "Неверное имя пользователя или пароль."
    else:
        form = AuthenticationForm()

    return render(request, 'users/login.html', {'form': form, 'error_message': error_message})


@login_required  # Требуется авторизация для доступа к личному кабинету
def profile_view(request):
    return render(request, 'users/profile.html')

def logout_view(request):
    logout(request)
    return redirect(reverse('home'))