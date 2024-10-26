from django.urls import path
from . import views

app_name = 'shop_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('sun/', views.view_sun_film, name='view_sun_film'),
    path('security/', views.view_security_film, name='view_security_film'),
    path('decoration/', views.view_decoration_film, name='view_decoration_film'),
]