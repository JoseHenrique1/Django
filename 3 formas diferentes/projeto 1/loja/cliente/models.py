from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=30)
    idade = models.IntegerField()
    
    
    def __str__(self):
        return self.nome