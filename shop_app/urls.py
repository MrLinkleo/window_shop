from django.urls import path
from . import views

app_name = 'shop_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('sun/', views.view_sun_film, name='view_sun_film'),
    path('security/', views.view_security_film, name='view_security_film'),
    path('decoration/', views.view_decoration_film, name='view_decoration_film'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='cart'),
    path('update-cart-item/', views.update_cart_item, name='update_cart_item'),
    path('delete-cart-item/', views.delete_cart_item, name='delete_cart_item'),
    path('contacts/', views.contacts, name='contacts'),
    path('invoice/', views.generate_invoice, name='invoice'),
    path('services/', views.view_services, name='services'),
    path('online_store/', views.view_online_store, name='online_store'),
]