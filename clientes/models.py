from django.db import models

class Clientes(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    morada = models.CharField(max_length=200)

    def __str__(self):
        return self.nome
