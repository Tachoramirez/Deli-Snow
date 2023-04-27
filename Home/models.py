from django.db import models

# Create your models here.

class CategoriaProd(models.Model):
    nombre = models.CharField(max_length = 50)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name = "categoríaProd"
        verbose_name_plural = "categoriasProd"

    def __str__(self):
        return self.nombre
    
class Temporada(models.Model):
    nombre = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name = "Temporada"
        verbose_name_plural = "Temporadas"

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length = 50)
    categoria = models.ForeignKey(CategoriaProd, on_delete = models.CASCADE)
    imagen = models.ImageField(upload_to = "static/img/tienda", null = True, blank = True)
    descripcion = models.CharField(max_length=100)
    temporada = models.ForeignKey(Temporada, on_delete=models.CASCADE)
    precio = models.FloatField()
    cantidad = models.IntegerField(null = True, blank = True)
    disponibilidad = models.BooleanField(default = True)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.nombre
    

class Ingrediente(models.Model):
    nombre = models.TextField(max_length = 50)
    cantidad = models.FloatField(max_length = 5)
    unidad = models.TextField(max_length = 3)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name = "Ingrediente"
        verbose_name_plural = "Ingredientes"

    def __str__(self):
        return self.nombre
    
class Receta(models.Model):
    nombre = models.TextField(max_length = 50)
    descripcion = models.TextField(max_length = 250)
    tiempoPrep = models.IntegerField()
    instrucciones = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name = "Receta"
        verbose_name_plural = "Recetas"

    def __str__(self):
        return self.nombre
    
class IngredienteReceta(models.Model):
    idReceta = models.ForeignKey(Receta, on_delete= models.CASCADE)
    idIngrediente = models.ForeignKey(Ingrediente, on_delete= models.CASCADE)
    cantidad = models.FloatField(max_length = 5)
    unidad = models.TextField(max_length=3)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name = "Detalle receta"
        verbose_name_plural = "Detalle recetas"