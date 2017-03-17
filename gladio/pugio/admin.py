from django.contrib import admin
from pugio.models import provincia, poblacion, moneda, impuesto, empresa, sucursal
from pugio.models import cliente, departamento, empleado
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
      
admin.site.register(provincia)
admin.site.register(poblacion, PoblacionAdmin)
admin.site.register(moneda)
admin.site.register(impuesto)
admin.site.register(empresa)
admin.site.register(sucursal, SucursalAdmin)
admin.site.register(cliente, ClienteAdmin)
admin.site.register(departamento, DepartamentoAdmin)
admin.site.register(empleado, EmpleadoAdmin)

