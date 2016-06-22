from django import forms
from django.forms import ModelForm
from django.db import models
from control_interno.models import client
from localflavor.mx.models import MXStateField, MXZipCodeField, MXRFCField
from django.contrib.auth.models import User
#from django.contrib.auth.forms import UserCreationForm



class AddClientForm(ModelForm):
    nombre_cliente = models.CharField(max_length=100)
    nombre_personal = models.CharField(max_length=100)
    rfc = MXRFCField()
    direccion_calle = models.CharField(max_length=30)
    numero_interior = models.CharField(max_length=50)
    numero_exterior = models.IntegerField(blank=True)
    codigo_postal = MXZipCodeField()
    entidad_federativa = MXStateField()
    municipio = models.CharField(max_length=30)
    nombre_usuario = models.CharField(max_length=100 )
    telefono = models.IntegerField(blank=True)
    correo_electronico = models.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = client
        fields = ("nombre_cliente", "nombre_personal", "rfc", "direccion_calle", "numero_interior", "numero_exterior",
            "codigo_postal", "entidad_federativa", "municipio", "nombre_usuario", "telefono", "correo_electronico", "password",)
#     def compare(self):
#         cleaned_data = super(AddClientForm, self).clean()
#         correo_electronico = cleaned_data.get("correo_electronico")
#         p = UserInfo.objects.all()


# try:
#     p = UserInfo.objects.get(id=correo_electronico)
# except UserInfo.DoesNotExist:
#     raise forms.ValidationError("User not exist.")

# class NameForm(forms.Form):
#   your_id = forms.CharField(label='Your id', max_length=100)
#   def clean(self):
#      cleaned_data = super(NameForm, self).clean()
#      your_id = cleaned_data.get("your_id")
#      p = UserInfo.objects.all()
#      if your_id:
#         for i in p:
#            if i.usrId not in your_id:
#               raise forms.ValidationError(
#                    "User not exist."
#                   )