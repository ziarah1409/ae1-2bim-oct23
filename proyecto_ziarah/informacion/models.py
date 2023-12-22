from django.db import models

# Create your models here.
class Pais(models.Model):
    nombre = models.CharField(max_length=30)
    capital = models.CharField(max_length=30)
    habitantes = models.IntegerField()

    def __str__(self):
        return """Nombre: %s\n
                Capital: %s\n
                Habitantes: %d\n
                """ % (self.nombre,
                self.capital,
                self.habitantes
                )
    

class Barrio(models.Model):
    nombre = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=30)
    num_calles = models.IntegerField()

    def __str__(self):
        return """Nombre: %s\n
                Ciudad: %s\n
                Numero de Calles: %d\n
                """ % (self.nombre,
                self.ciudad,
                self.num_calles
                )