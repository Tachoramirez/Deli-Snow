from django.contrib import admin
from .models import CategoriaProd, Producto, Temporada, Ingrediente, IngredienteReceta, Receta

# Register your models here.

class CategoriraProdAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

class ProductoAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

class TemporadaAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

class IngredienteAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

class IngredienteRecetaAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

class RecetaAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

admin.site.register(CategoriaProd, CategoriraProdAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Temporada, TemporadaAdmin)
admin.site.register(Ingrediente, IngredienteAdmin)
admin.site.register(IngredienteReceta, IngredienteRecetaAdmin)
admin.site.register(Receta, RecetaAdmin)



