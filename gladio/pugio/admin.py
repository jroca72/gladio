from django.contrib import admin
from pugio.models import provincia, poblacion, moneda, impuesto
# Register your models here.

admin.site.register(provincia)
admin.site.register(poblacion)
admin.site.register(moneda)
admin.site.register(impuesto)

