from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import ImagenForm, UnetUserCreationForm, SearchUserForm
from .models import Imagen, Publication

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
    searchUser = SearchUserForm(request.GET or None)
    if request.method == 'POST':
        form = ImagenForm(request.POST, request.FILES)
        if form.is_valid():
            nueva_imagen = form.save(commit=False)
            nueva_imagen.usuario = request.user
            nueva_imagen.save()
            return redirect('home')
    else:
        form = ImagenForm()

    if searchUser.is_valid():
        username = searchUser.cleaned_data.get('username')
        if username:
            imagenes_del_usuario = Imagen.objects.filter(usuario__username=username)
        else:
            imagenes_del_usuario = Imagen.objects.filter(usuario=request.user)
    imagenes_del_usuario = Imagen.objects.filter(usuario=request.user)

    context = {
        'form': form,
        'imagenes': imagenes_del_usuario
    }
    return render(request, 'home.html', context)

@login_required
def feed_view(request):
    publicaciones = Publication.objects.all().order_by('-fecha_publicacion')
    context = {
        'publicaciones': publicaciones
    }
    return render(request, 'feed.html', context) 