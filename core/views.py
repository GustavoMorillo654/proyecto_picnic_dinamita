from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import ImagenForm, UnetUserCreationForm
from .models import Imagen


def registro_view(request):
    """
    Esta función ahora usa nuestro formulario personalizado UnetUserCreationForm.
    """
    if request.method == 'POST':
        form = UnetUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UnetUserCreationForm()

    return render(request, 'registration/registro.html', {'form': form})


@login_required
def home_view(request):
    if request.method == 'POST':
        form = ImagenForm(request.POST, request.FILES)
        if form.is_valid():
            nueva_imagen = form.save(commit=False)
            nueva_imagen.usuario = request.user
            nueva_imagen.save()
            return redirect('home')
    else:
        form = ImagenForm()

    imagenes_del_usuario = Imagen.objects.filter(usuario=request.user)

    context = {
        'form': form,
        'imagenes': imagenes_del_usuario
    }
    return render(request, 'home.html', context)
