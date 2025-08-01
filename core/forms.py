from django import forms
from .models import Imagen

class ImagenForm(forms.ModelForm):

    class Meta:
        model = Imagen

        fields = ['titulo', 'imagen']

        labels = {
            'titulo': 'Ponle un título a tu imagen',
            'imagen': 'Selecciona el archivo de la imagen',
        }

        widgets = {
            'titulo': forms.TextInput(attrs={'placeholder': 'Ej: Mi foto en la playa'}),
        }
