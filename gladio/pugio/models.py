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

         
