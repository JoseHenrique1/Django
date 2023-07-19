from django.db import models

class Carro(models.Model):
    tipo = models.CharField(max_length=30)
    valor = models.FloatField()
    

    def __str__(self):
        return self.tipo
