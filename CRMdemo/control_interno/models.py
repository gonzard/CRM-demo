from __future__ import unicode_literals

from django.db import models
from django.core.validators import RegexValidator
from localflavor.mx.models import MXStateField, MXZipCodeField, MXRFCField
from django.contrib.auth.models import User


# Create your models here.


class client(models.Model):
    nombre_cliente = models.CharField(max_length=100 )
    nombre_personal = models.CharField(max_length=100)
    #rfc_regex = RegexValidator(regex=r'^\+?1?\d{9,9}$', message="El RFC parece ser invalido")
    #rfc = models.CharField(max_length=13,  blank=False, validators=[rfc_regex])
    rfc = MXRFCField()
    direccion_calle = models.CharField(max_length=30)
    numero_interior = models.CharField(max_length=50)
    numero_exterior = models.CharField(max_length=50, blank=True)
    #cp_regex = RegexValidator(regex=r'^\+?1?\d{9,5}$', message="El Codigo Postal es invalido")
    #codigo_postal = models.IntegerField(max_length=5, validators=[cp_regex])
    codigo_postal = MXZipCodeField()
    entidad_federativa = MXStateField()
    municipio = models.CharField(max_length=30)
    nombre_usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono_regex = RegexValidator(regex=r'^\+?1?\d{9,10}$', message="El numero telefonico debe de ser de diez digitos")
    telefono = models.CharField(max_length=10, validators=[telefono_regex])
    correo_electronico = models.EmailField()
    password = models.CharField(max_length=50)

    def __unicode__(self):
    	return self.nombre_cliente


         

