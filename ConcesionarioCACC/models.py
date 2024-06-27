from django.db import models

class Marcas(models.Model):
    nombre_marca = models.CharField(max_length= 100)
    pais_origen = models.CharField(max_length= 100)
    fecha_fundacion = models.DateField()
    descripcion = models.CharField(max_length=300)
    estado = models.IntegerField(max_length= 11)
    
    class Meta:
        db_table = 'marcas'


class Proveedor(models.Model):
    nombre = models.CharField(max_length=200)
    cedula = models.IntegerField(max_length=20)
    celular = models.IntegerField(max_length=20)
    pais = models.CharField(max_length=100)
    estado = models.IntegerField(max_length= 11)

    class Meta:
        db_table = 'proveedor'


class Vehiculo(models.Model):
    nombre = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    capacidad = models.IntegerField(max_length=11)
    cilindraje = models.IntegerField(max_length=11)
    cantidad_de_vehiculos = models.IntegerField(max_length=11)
    precio = models.IntegerField(max_length=11)
    foto = models.CharField(max_length= 250)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    marcas = models.ForeignKey(Marcas, on_delete=models.CASCADE)
    estado = models.IntegerField(max_length= 11)

    class Meta:
        db_table = 'vehiculos'