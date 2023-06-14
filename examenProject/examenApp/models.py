from django.db import models

# Create your models here.
class oficina(models.Model):
    ciudad = models.CharField(max_length=10)
    calle =models.CharField(max_length=10)
    numero =models.IntegerField()
    abierta = models.BooleanField()
    fecha_apertura = models.DateField()

    def __str__(self):
        return self.ciudad
    

class empleado(models.Model):
    nombre = models.CharField(max_length=10)
    apellido = models.CharField(max_length=10)
    numeroOficina = models.ForeignKey(oficina, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre