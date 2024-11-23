from django.contrib import admin
from .models import Film


admin.site.register(Film)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')
    list_editable = ('stock',)
