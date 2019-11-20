from django.db import models

# Create your models here.


#sucursal 
#(codigo, nombreSucursal)

class Sucursal(models.Model):
	codigoSucursal = models.IntegerField(default=0)
	idSucursal = models.IntegerField
	nombreSucursal = models.CharField(max_length=50)

#cliente
#(rut, nombre, fechaNacimiento, correo, telefono, 
# fecha visita, hora visita)
class Cliente(models.Model):
	codigoSucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
	rut = models.CharField(max_length=9)
	nombre = models.CharField(max_length=50)
	correo = models.CharField(max_length=50)
	telefono = models.IntegerField(default=0)
	fechaNacimiento = models.DateTimeField('Fecha de Nacimiento')
	fechaVisita = models.DateTimeField('Fecha de visita')
	HoraVisita = models.DateTimeField('Hora de visita')