from django.db import models
from django.contrib.auth.models import User


class Titulo(models.Model):
    nome = models.CharField(max_length=128)
    ano = models.IntegerField()
    studio = models.CharField(max_length=128)
    preco = models.FloatField()

class Fita(models.Model):
    title = models.ForeignKey(Titulo, related_name='fitas', on_delete=models.CASCADE)
    status = models.BooleanField(default=True)


class Locacao(models.Model):
    data_locacao = models.DateTimeField(auto_now_add=True, blank=True)
    data_entrega =  models.DateTimeField()
    fitas = models.ManyToManyField(Fita)
    socio = models.ForeignKey(User, related_name='locacoes',on_delete=models.CASCADE)
    valor_total =  models.FloatField()