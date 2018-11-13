from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    dados = models.CharField(max_length=50)

def __str__(self):
    return self.nome