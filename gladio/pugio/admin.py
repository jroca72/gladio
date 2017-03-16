from django.contrib import admin
from pugio.models import provincia, poblacion, moneda, impuesto, cliente, empresa
from pugio.models import departamento, empleado
# Register your models here.
class PoblacionAdmin(admin.ModelAdmin):
   list_display = ('poblacion', 'provincia')
   search_fields = ('poblacion', 'provincia__provincia')
   list_filter = ('provincia__provincia',)
   ordering = ('provincia__provincia', 'poblacion')

class ClienteAdmin(admin.ModelAdmin):
   list_display = ('apellidos', 'nombre', 'telefono', 'movil')
   ordering = ('apellidos', 'nombre')

class EmpleadoAdmin(admin.ModelAdmin):
   list_display = ('empresa', 'apellidos', 'nombre', 'departamento')
   
admin.site.register(provincia)
admin.site.register(poblacion, PoblacionAdmin)
admin.site.register(moneda)
admin.site.register(impuesto)
admin.site.register(cliente, ClienteAdmin)
admin.site.register(empresa)
admin.site.register(departamento)
admin.site.register(empleado, EmpleadoAdmin)

