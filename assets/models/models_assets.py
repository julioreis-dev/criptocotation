from django.db import models
from clients.models.models_clients import Clientstable
from assets.models import COIN_CHOICE, TIMER_CHOICE
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime



class Assetstable(models.Model):
    nameconfig = models.CharField(max_length=200, verbose_name='Nome da configuração', null=True, blank=True)
    coin = models.CharField(max_length=100, choices=COIN_CHOICE, default='BTC')
    sell = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Valor de venda', default=0.00)
    buy = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Valor de compra', default=0.00)
    timer = models.IntegerField(verbose_name='Timer de alerta', choices=TIMER_CHOICE, default=30, help_text='(mins)')
    emaildate = models.DateTimeField(default=timezone.now)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Cliente', null=True)

    # user_id = models.ManyToManyField(Clientstable, verbose_name='Cliente')

    def __str__(self):
        return f'{self.id}-{self.coin}'

    class Meta:
        """
        Classe para ordenar e contextualizar o admin
        """
        verbose_name = 'Ativo'
        verbose_name_plural = 'Ativos'


class Coincotationtable(models.Model):
    description = models.CharField(max_length=150, verbose_name='Nome da criptomoeda')
    price = models.FloatField(default=0)

    def __str__(self):
        return f'{self.description}'

    class Meta:
        """
        Classe para ordenar e contextualizar o admin
        """
        verbose_name = 'Cotações'
        verbose_name_plural = 'Cotação'
