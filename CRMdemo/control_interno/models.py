from __future__ import unicode_literals

from django.db import models

# Create your models here.


class client(models.Model):
    nombre_cliente = models.CharField(max_length=100 )
    nombre_personal = models.CharField(max_length=100)
    rfc = models.CharField(max_length=13, blank=False)
    direccion_calle = models.CharField(max_length=30)
    numero_interior = models.CharField(max_length=50)
    numero_exterior = models.IntegerField(blank=True)
    codigo_postal = models.IntegerField()
    entidad_federativa = models.CharField(max_length=30)
    municipio = models.CharField(max_length=30)
    nombre_usuario = models.CharField(max_length=100 )
    telefono = models.IntegerField(blank=True)
    correo_electronico = models.EmailField()
    password = models.CharField(max_length=50)

    def __unicode__(self):
    	return self.nombre_cliente

