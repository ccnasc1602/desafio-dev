from django.db import models
from django.db.models.deletion import CASCADE

SIGNAL_CHOICES = (
    ("+", "Entrada"),
    ("-", "Saída"),
)

NATURE_CHOICES = (
    ("E", "Entrada"),
    ("S", "Saída"),
)


class Cnab_Type(models.Model):
    id = models.IntegerField(max_length=3, null=False, primary_key=True, unique=True, verbose_name='Código')
    name = models.CharField(max_length=30, null=False, verbose_name='Descrição')
    nature = models.CharField(max_length=1, choices=NATURE_CHOICES, blank=False, verbose_name='Natureza')
    signal = models.CharField(max_length=1, choices=SIGNAL_CHOICES, blank=False, verbose_name='Sinal')


class Cnab_Movto(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.ForeignKey(Cnab_Type, on_delete=models.CASCADE, verbose_name='Tipo de Transação')
    date = models.DateField(null=False, verbose_name='Data da Transação')
    value = models.DecimalField(max_digits=10, decimal_places=2, null=False, verbose_name='Valor da Transação')
    cpf = models.CharField(max_length=11, null=False, verbose_name='CPF do Baneficiário')
    card = models.CharField(max_length=12, null=False, verbose_name='Cartão Utilizado')
    time = models.TimeField(auto_now=False, auto_now_add=False, null=False, verbose_name='Hora da Transação')
    store_owner = models.CharField(max_length=14, verbose_name='Nome do Representante')
    store_name = models.CharField(max_length=19, verbose_name='Nome da Loja')
