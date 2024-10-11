from django.db import models

class Produto(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    quantidade_em_estoque = models.IntegerField()
    data_criacao = models.DateTimeField(auto_now_add=True)