from django.db import models

# Create your models here.
class Familia (models.Model):
    nombre = models. CharField (max_length=30)
    edad = models. IntegerField ()
    fecha_cumpleaños = models. DateField()
    parentesco = models. CharField (max_length=40)

    def __str__ (self):

        return self.nombre
