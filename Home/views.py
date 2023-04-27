from django.shortcuts import render
from .models import Producto, CategoriaProd, Temporada

# Create your views here.

def index(request):
    categorias = CategoriaProd.objects.all()
    productos = Producto.objects.all()
    temporadas = Temporada.objects.all()
    context = {'categorias': categorias, 'productos': productos, 'temporadas':temporadas}
    return render(request, 'index.html', context)
