from django.contrib import admin
from pugio.models import provincia, poblacion, moneda, impuesto
# Register your models here.
class PoblacionAdmin(admin.ModelAdmin):
   list_display = ('poblacion', 'provincia')
   search_fields = ('poblacion', 'provincia__provincia')
   list_filter = ('provincia__provincia',)
   ordering = ('provincia__provincia', 'poblacion')

admin.site.register(provincia)
admin.site.register(poblacion, PoblacionAdmin)
admin.site.register(moneda)
admin.site.register(impuesto)

