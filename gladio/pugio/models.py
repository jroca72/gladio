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

# empresas ----------------------------------------------------
class empresa(models.Model):
   razon_social = models.CharField(max_length=100, null=False, blank=False)
   cif = models.CharField(max_length=15, null=False, blank=False)
   direccion_social = models.CharField(max_length=150, null=False, blank=False)
   provincia_social = models.ForeignKey(provincia, default=None, null=False, blank=False)
   poblacion_social = models.ForeignKey(poblacion, default=None, null=False, blank=False)
   cp_social = models.CharField(max_length=10, null=True, blank=True)
   pais = models.CharField(max_length=50, default='Espana', null=True, blank=True)
   telefono_social = models.CharField(max_length=15, null=True, blank=True)
   movil_social = models.CharField(max_length=15, null=True, blank=True)
   fax_social = models.CharField(max_length=15, null=True, blank=True)
   mail_social = models.EmailField(max_length=125, blank=True)
   web = models.URLField(max_length=150, blank=True)
   logotipo = models.ImageField(upload_to='imagenes', blank=True)
   nombre_comercial = models.CharField(max_length=100, null=False, blank=False)

   class Meta:
      verbose_name_plural = "Empresas"

   def __unicode__(self):
      return self.razon_social

# sucursal ----------------------------------------------------
class sucursal(models.Model):
   empresa = models.ForeignKey(empresa, default=None, null=False, blank=False)
   sucursal = models.CharField(max_length=50, default=None, null=False, blank=False)
   direccion = models.CharField(max_length=100, null=False, blank=False)
   codigopostal = models.CharField(max_length=10, null=True, blank=True)
   poblacion = models.ForeignKey(poblacion, default=None, null=False, blank=False)
   provincia = models.ForeignKey(provincia, default=None, null=False, blank=False)
   pais = models.CharField(max_length=25, default='Espana', null=True, blank=True)
   telefono = models.CharField(max_length=15, null=True, blank=True)
   movil = models.CharField(max_length=15, null=True, blank=True)
   fax = models.CharField(max_length=15, null=True, blank=True)
   mail = models.EmailField(max_length=125, blank=True)
   responsable = models.CharField(max_length=75, null=True, blank=True)

   class Meta:
      verbose_name_plural = "Sucursales"

   def __unicode__(self):
      return self.sucursal

# clientes ----------------------------------------------------
class cliente(models.Model):
   empresa = models.ForeignKey(empresa, default=None, null=False, blank=False)
   sucursal = models.ForeignKey(sucursal, default=None, null=False, blank=False)
   nombre = models.CharField(max_length=100, null=False, blank=False)
   apellidos = models.CharField(max_length=100, null=True, blank=True)
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

# departamento -------------------------------------------------
class departamento(models.Model):
   empresa = models.ForeignKey(empresa, default=None, null=False, blank=False)
   sucursal = models.ForeignKey(sucursal, default=None, null=False, blank=False)
   departamento = models.CharField(max_length=75, null=False, blank=False)

   class Meta:
      verbose_name_plural = "Departamentos"

   def __unicode__(self):
      return self.departamento

# empleados -----------------------------------------------------
class empleado(models.Model):
   empresa = models.ForeignKey(empresa, default=None, null=False, blank=False)
   sucursal = models.ForeignKey(sucursal, default=None, null=False, blank=False)
   nombre = models.CharField(max_length=75, null=False, blank=False)
   apellidos = models.CharField(max_length=75, null=False, blank=False)
   direccion = models.CharField(max_length=150, null=False, blank=False)
   provincia = models.ForeignKey(provincia, default=None, null=False, blank=None)
   poblacion = models.ForeignKey(poblacion, default=None, null=False, blank=None)
   cp = models.CharField(max_length=10, null=True, blank=True)
   pais = models.CharField(max_length=50, default='Espana', null=True, blank=True)
   telefono = models.CharField(max_length=15, null=True, blank=True)
   movil = models.CharField(max_length=15, null=True, blank=True)
   mail = models.EmailField(max_length=125, blank=True)
   fotografia = models.ImageField(upload_to='imagenes', blank=True)
   nif = models.CharField(max_length=15, null=False, blank=False)
   nss = models.CharField(max_length=50, null=False, blank=False)
   departamento = models.ForeignKey(departamento, default=None, null=False, blank=None)
   fecha_alta = models.DateField(default=datetime.now, blank=True)
   baja = models.BooleanField(default=False, null=False, blank=True)
   fecha_baja = models.DateField(default=datetime.now, blank=True)

   class Meta:
      verbose_name_plural = "Empleados"

   def __unicode__(self):
      return self.nombre

# pago -------------------------------------------------------------
class pago(models.Model):
   nombre = models.CharField(max_length=50, default=None, null=False, blank=False)
   dia_1 = models.PositiveIntegerField(null=True, blank=True)
   dia_2 = models.PositiveIntegerField(null=True, blank=True)
   dia_3 = models.PositiveIntegerField(null=True, blank=True)
   dia_4 = models.PositiveIntegerField(null=True, blank=True)
   dia_5 = models.PositiveIntegerField(null=True, blank=True)
   dia_6 = models.PositiveIntegerField(null=True, blank=True)

   class Meta:
      verbose_name_plural = "Pagos"

   def __unicode__(self):
      return self.nombre

# proveedor ---------------------------------------------------------
class proveedor(models.Model):
   empresa = models.ForeignKey(empresa, default=None, null=False, blank=False)
   razon_social = models.CharField(max_length=100, default=None, null=False, blank=False)
   cif = models.CharField(max_length=15, null=False, blank=False)
   direccion_social = models.CharField(max_length=150, null=False, blank=False)
   provincia_social = models.ForeignKey(provincia, default=None, null=False, blank=False)
   poblacion_social = models.ForeignKey(poblacion, default=None, null=False, blank=False)
   cp_social = models.CharField(max_length=10, null=True, blank=True)
   pais_social = models.CharField(max_length=50, default='Espana', null=True, blank=True)
   telefono_social = models.CharField(max_length=15, null=True, blank=True)
   movil_social = models.CharField(max_length=15, null=True, blank=True)
   fax_social = models.CharField(max_length=15, null=True, blank=True)
   mail_social = models.EmailField(max_length=125, blank=True)
   web = models.URLField(max_length=150, blank=True)
   logotipo = models.ImageField(upload_to='imagenes', blank=True)
   nombre_comercial = models.CharField(max_length=100, null=False, blank=False)
   direccion_comercial = models.CharField(max_length=150, null=False, blank=False)
   provincia_comercial = models.ForeignKey(provincia, related_name='provincia_c', default=None, null=False, blank=False)
   poblacion_comercial = models.ForeignKey(poblacion, related_name='poblacion_c', default=None, null=False, blank=False)
   cp_comercial = models.CharField(max_length=10, null=True, blank=True)
   pais_comercial = models.CharField(max_length=50, default='Espana', null=True, blank=True)
   telefono_comercial = models.CharField(max_length=15, null=True, blank=True)
   movil_comercial = models.CharField(max_length=15, null=True, blank=True)
   fax_comercial = models.CharField(max_length=15, null=True, blank=True)
   mail_comercial = models.EmailField(max_length=125, blank=True)
   portal = models.URLField(max_length=150, blank=True)
   fecha_alta = models.DateField(default=datetime.now, blank=True)
   baja = models.BooleanField(default=False, null=False)
   fecha_baja = models.DateField(default=datetime.now, blank=True)
   persona_contacto = models.CharField(max_length=50, null=True, blank=True)
   telefono_contacto = models.CharField(max_length=15, null=True, blank=True)
   mail_contacto = models.EmailField(max_length=125, blank=True)
   observaciones = models.CharField(max_length=255, null=True, blank=True)
   pago = models.ForeignKey(pago, default=None, null=False, blank=False)
   impuesto = models.ForeignKey(impuesto, default=None, null=False, blank=False)

   class Meta:
      verbose_name_plural = "Proveedores"

   def __unicode__(self):
      return self.razon_social

# familia ---------------------------------------------------------
class familia(models.Model):
   letra = models.CharField(max_length=2, null=False, blank=False)
   nombre = models.CharField(max_length=70, null=False, blank=False)

   class Meta:
      verbose_name_plural = "Familias"

   def __unicode__(self):
      return self.nombre

# subfamilia ------------------------------------------------------
class subfamilia(models.Model):
	letra = models.CharField(max_length=2, null=False, blank=False)      
	familia = models.ForeignKey(familia, default= None, null=False, blank=False)
	nombre = models.CharField(max_length=70, null=False, blank=False)
	
	class Meta:
		verbose_name_plural = "SubFamilias"
	
	def __unicode__(self):
		return self.nombre

			
					
