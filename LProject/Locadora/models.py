from django.db import models
from django.contrib.auth.models import User


class Titulo(models.Model):
    nome = models.CharField()
    ano = models.IntergerField()
    studio = models.CharField()
    preco = models.FloatField()

class Fita(models.Model):
    title = models.ForeignKey(Titulo, related_name='fitas', on_delete=models.CASCADE)
    status = models.BooleanField(default=True)


class Locacao(models.Model):
    data_locacao = models.DataTimeField(auto_now_add=True, blank=True)
    data_entrega =  models.DataTimeField()
    fitas = models.ManyToManyFields(Fita, related_name='fitas', on_delete=models.CASCADE)
    socio = models.ForeignKey(User, related_name='locacoes',on_delete=models.CASCADE)
    valor_total =  models.FloatField()