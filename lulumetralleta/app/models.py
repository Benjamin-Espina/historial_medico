from django.db import models

# Create your models here.

opc_sexo = [
    [1, "Hombre"],
    [2, "Mujer"],
    [3, "No Binario"]
]

class Paciente(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=100)
    sexo = models.CharField(max_length=50)
    edad = models.IntegerField()

    def __str__(self):
        return self.nombre

class Medico(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=100)
    sexo = models.IntegerField(choices=opc_sexo)
    edad = models.IntegerField()
    especialidad = models.CharField(max_length=50)
    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre

class Cita(models.Model):
    fecha = models.CharField(max_length=30)
    hora = models.CharField(max_length=30)
    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT)
    medico = models.ForeignKey(Medico, on_delete=models.PROTECT)
    descripcion = models.TextField()
    
    def __str__(self):
        return self.fecha


