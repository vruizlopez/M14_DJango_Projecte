from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

class Usuario(models.Model):
    nombre = models.CharField(max_length=15)
    password = models.CharField(max_length=20)
    apellido1 = models.CharField(max_length=15)
    apellido2 = models.CharField(max_length=15)
    fechaNacimiento = models.DateField()
    correo = models.EmailField(max_length=50)
    telefono = models.IntegerField(max_length=9, unique=True, validators=[RegexValidator(regex='^\d{9}$', message='La longitud tiene que ser de 9 numeros', code='Invalid number')])
    def __str__(self):
        return self.nombre
class Vehiculo(models.Model):
    modelo = models.CharField(max_length=100)
    version = models.CharField(max_length=100)
    motor = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10,decimal_places=2)
    def __str__(self):
        return self.modelo
class Ventas(models.Model):
    usuario = models.ForeignKey(Usuario)
    vehiculo = models.ForeignKey(Vehiculo)
    precioTotal = models.DecimalField(max_digits=10,decimal_places=2)