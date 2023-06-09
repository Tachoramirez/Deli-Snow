from django.shortcuts import render,redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.

class UserRegister(View):

    def get(self, request):
        form = UserCreationForm()
        return render(request, 'registro/registro.html', {"form": form})

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():

            usuario = form.save()
            login(request, usuario)
            return redirect('Inicio')

        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            return render(request, 'registro/registro.html', {"form":form})

def CerrarSesion(request):
    logout(request)
    return redirect('Inicio')

def Loguear(request):
#Validación de formulario una vez dando clic en iniciar sesión
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            usuario = authenticate(username = nombre_usuario, password = contra)
            if usuario is not None:
                login(request, usuario)
                messages.info(request, 'Bienvenido')
                return redirect('Inicio')
            else:
                messages.error(request, "Usuario no válido")
        else:
            messages.error(request, "Información incorrecta")

#Muestra el formulario por primera vez en la vista
    form = AuthenticationForm()
    return render(request, 'login/login.html', {"form":form})