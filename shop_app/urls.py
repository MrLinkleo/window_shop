from django.urls import path
from . import views

app_name = 'shop_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('sun/', views.view_sun_film, name='view_sun_film'),
    path('security/', views.view_security_film, name='view_security_film'),
    path('decoration/', views.view_decoration_film, name='view_decoration_film'),
    path('add_to_cart/<str:product_name>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='cart'),
]