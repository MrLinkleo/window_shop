from django import forms
from shop_app.models import SunFilm  # Импортируйте вашу модель SunFilm

class SunFilmForm(forms.ModelForm):
    class Meta:
        model = SunFilm
        fields = ['name', 'description', 'price', 'image']  # Поля для формы