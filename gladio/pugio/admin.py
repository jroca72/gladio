from django.contrib import admin
from pugio.models import provincia, poblacion, moneda, impuesto, empresa, sucursal
from pugio.models import cliente, departamento, empleado, pago, proveedor, familia, subfamilia
from pugio.models import condicion_compra, condicion_marcaje, catalogo, articulo

# Register your models here.
class PoblacionAdmin(admin.ModelAdmin):
   list_display = ('poblacion', 'provincia')
   search_fields = ('poblacion', 'provincia__provincia')
   list_filter = ('provincia__provincia',)
   ordering = ('provincia__provincia', 'poblacion')

class ClienteAdmin(admin.ModelAdmin):
   list_display = ('apellidos', 'nombre', 'telefono', 'movil', 'empresa', 'sucursal')
   ordering = ('apellidos', 'nombre')

class EmpleadoAdmin(admin.ModelAdmin):
   list_display = ('empresa', 'sucursal', 'apellidos', 'nombre', 'departamento')
   ordering = ('empresa', 'sucursal')
   list_filter = ('departamento',)

class DepartamentoAdmin(admin.ModelAdmin):
   list_display = ('empresa', 'sucursal', 'departamento')

class SucursalAdmin(admin.ModelAdmin):
   list_display = ('empresa', 'sucursal')

class FamiliaAdmin(admin.ModelAdmin):
	list_display = ('letra', 'nombre')

class SubfamiliaAdmin(admin.ModelAdmin):
	list_display = ('familia','letra', 'nombre')
	ordering = ('familia', 'letra')

class Condicion_compraAdmin(admin.ModelAdmin):
	list_display = ('proveedor', 'nombre')
	ordering = ('proveedor', 'nombre')

class Condicion_marcajeAdmin(admin.ModelAdmin):
	list_display = ('proveedor', 'nombre')
	ordering = ('proveedor', 'nombre')

class CatalogoAdmin(admin.ModelAdmin):
	list_display = ('proveedor', 'nombre')
	ordering = ('proveedor', 'nombre')

admin.site.register(provincia)
admin.site.register(poblacion, PoblacionAdmin)
admin.site.register(moneda)
admin.site.register(impuesto)
admin.site.register(empresa)
admin.site.register(sucursal, SucursalAdmin)
admin.site.register(cliente, ClienteAdmin)
admin.site.register(departamento, DepartamentoAdmin)
admin.site.register(empleado, EmpleadoAdmin)
admin.site.register(pago)
admin.site.register(proveedor)
admin.site.register(familia, FamiliaAdmin)
admin.site.register(subfamilia, SubfamiliaAdmin)
admin.site.register(condicion_compra, Condicion_compraAdmin)
admin.site.register(condicion_marcaje, Condicion_marcajeAdmin)
admin.site.register(catalogo, CatalogoAdmin)
admin.site.register(articulo)
