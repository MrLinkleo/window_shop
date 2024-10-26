from django.urls import path
from .views import add_film

app_name = 'add_film'

urlpatterns = [
    path('add_film/', add_film, name='add_film'),  # URL для добавления пленки

]