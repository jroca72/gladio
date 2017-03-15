from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from django.core.urlresolvers import reverse

# COMUN

# provncias -------------------------------------------------
class provincia(models.Model):
	numero = models.PositiveIntegerField(null=False, blank=False)
	provincia = models.CharField(max_length=50)

	class Meta:
		verbose_name_plural = "Provincias"

	def __unicode__(self):
		return self.provincia

# poblaciones -----------------------------------------------
class poblacion(models.Model):
   provincia = models.ForeignKey(provincia, default=None, null=True, blank=True)
   poblacion = models.CharField(max_length=125)
   
   class Meta:
		verbose_name_plural = "Poblaciones"

   def __unicode__(self):
	   return self.poblacion

# monedas ---------------------------------------------------
class moneda(models.Model):
	moneda = models.CharField(max_length=20, null=False, blank=False)
	
	class Meta:
	   verbose_name_plural = "Monedas"
	
	def __unicode__(self):
		return self.moneda

# impuestos --------------------------------------------------
class impuesto(models.Model):
   impuesto = models.CharField(max_length=25, null=False, blank=False)		   
   porcentaje = models.DecimalField(max_digits=5, decimal_places=2)
   
   class Meta:
      verbose_name_plural = "Impuestos"
      
   def __unicode__(self):
      return self.impuesto

# clientes ----------------------------------------------------
class cliente(models.Model):
   nombre = models.CharField(max_length=100, null=False, blank=False)
   direccion =models.CharField(max_length=100, null=False, blank=False)
   codigopostal = models.CharField(max_length=10, null=True, blank=True)
   poblacion = models.ForeignKey(poblacion, default=None, null=False, blank=False)
   provincia = models.ForeignKey(provincia, default=None, null=False, blank=False)
   pais = models.CharField(max_length=25, default='Espana', null=True, blank=True)
   cif = models.CharField(max_length=20, null=True, blank=True)
   telefono = models.CharField(max_length=15, null=True, blank=True)
   movil = models.CharField(max_length=15, null=True, blank=True)
   fax = models.CharField(max_length=15, null=True, blank=True)
   mail = models.EmailField(max_length=125, blank=True)
   fecha_alta = models.DateField(default=datetime.now, blank=True)
   baja = models.BooleanField(default=False, null=False)
   fecha_baja = models.DateField(default=datetime.now, blank=True)   
   
   class Meta:
      verbose_name_plural = "Clientes"
      
   def __unicode__(self):
      return self.nombre
            
   
