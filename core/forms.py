from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Imagen, Publication

class UnetUserCreationForm(UserCreationForm):
    """
    Este formulario hereda todo lo del UserCreationForm normal,
    pero le añadimos una validación personalizada para el correo.
    """
    email = forms.EmailField(required=True, help_text="Obligatorio. Por favor, usa tu correo institucional.")

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ( "username", "email", "first_name", "last_name")

    def clean_email(self):
        email = self.cleaned_data.get("email")

        if not email.endswith('@unet.edu.ve'):
            raise forms.ValidationError("Este correo no es válido. Solo se permiten correos del dominio @unet.edu.ve.")
        return email

class SearchUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']
        labels = {
            'username': 'Nombre del usuario a buscar',
        }
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Buscar usuario'}),
        }

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

class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = ['contenido']
        labels = {
            'contenido': '¿Qué estás pensando?',
        }
        widgets = {
            'contenido': forms.Textarea(attrs={'placeholder': 'Escribe tu publicación aquí...'}),
        }
