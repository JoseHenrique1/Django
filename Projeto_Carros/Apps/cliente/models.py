from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    carro = models.ForeignKey('carro.Carro', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

