from django.urls import path
from .views import UserRegister, CerrarSesion, Loguear

urlpatterns = [
    path('', UserRegister.as_view(), name="Autenticacion"),
    path('CerrarSesion/', CerrarSesion, name="Salir"),
    path('loguear/', Loguear, name="Login"),


]