from django.db import models

class alumno(models.Model):
    id=models.AutoField(primary_key=True)
    rut = models.CharField(max_length=12,null=True)
    nombre = models.CharField(max_length=100,null=True,verbose_name="nombre")
    edad = models.IntegerField(null=True,verbose_name="edad")
    asignaturas = models.CharField(max_length=100,null=True,verbose_name="asignaturas")
    celular = models.IntegerField(verbose_name="celular")
    apoderado= models.CharField(max_length=100,null=True,verbose_name="apoderado")

