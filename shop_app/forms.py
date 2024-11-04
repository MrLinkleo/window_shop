from django import forms

from .models import Film


class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = [
            'name', 'description', 'quantity', 'price', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control', 'name':'image'}),
        } 