from django.urls import path
from .views import (register_view, login_view, logout_view, profile_view, home_view)

app_name = "users"

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
    path('home/', home_view, name='home'),

]
