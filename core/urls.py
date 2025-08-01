from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Ruta para la página principal.
    # El path '' significa la raíz del sitio (ej: http://127.0.0.1:8000/).
    # Se conecta con nuestra 'home_view' y le damos el nombre 'home' para usarlo en el HTML.
    path('', views.home_view, name='home'),

    path('registro/', views.registro_view, name='registro'),

    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
