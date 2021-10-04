from django.db import models
from django.db.models.deletion import CASCADE

SIGNAL_CHOICES = (
    ("+", "Somar"),
    ("-", "Subtrair"),
)

NATURE_CHOICES = (
    ("E", "Entrada"),
    ("S", "Saída"),
)


class Type_Movto(models.Model):
    id = models.IntegerField(null=False, primary_key=True, unique=True, verbose_name='Código')
    nome = models.CharField(max_length=30, null=False, verbose_name='Descrição')
    natureza = models.CharField(max_length=1, choices=NATURE_CHOICES, blank=False, verbose_name='Natureza')
    sinal = models.CharField(max_length=1, choices=SIGNAL_CHOICES, blank=False, verbose_name='Sinal')

    class Meta:
        ordering = ['id', 'nome']
    
    def __str__(self) -> str:
        return "%s - %s" % (self.id, self.nome)


class Movto(models.Model):
    id = models.AutoField(primary_key=True)
    tipo = models.ForeignKey(Type_Movto, on_delete=models.CASCADE, verbose_name='Tipo de Transação')
    data = models.DateField(null=False, verbose_name='Data da Transação')
    valor = models.DecimalField(max_digits=10, decimal_places=2, null=False, verbose_name='Valor da Transação')
    cpf = models.CharField(max_length=11, null=False, verbose_name='CPF do Baneficiário')
    cartao = models.CharField(max_length=12, null=False, verbose_name='Cartão Utilizado')
    hora = models.TimeField(auto_now=False, auto_now_add=False, null=False, verbose_name='Hora da Transação')
    representante_loja = models.CharField(max_length=14, verbose_name='Nome do Representante')
    nome_loja = models.CharField(max_length=19, verbose_name='Nome da Loja')

    class Meta:
        ordering = ['tipo', 'data', 'cpf', 'nome_loja']
    
    def __str__(self):
        return self.nome_loja
