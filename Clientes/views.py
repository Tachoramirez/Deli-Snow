from django.shortcuts import render
from .models import Cliente


# Create your views here.
def clientes(request):
    clientes = Cliente.objects.all()
    context = {'clientes':clientes}
    return render(request, 'clientes.html', context)
