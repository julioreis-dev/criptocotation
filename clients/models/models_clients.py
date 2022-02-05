from django.db import models
from django.utils.timezone import now



class Clientstable(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nome')
    birthday = models.DateField(default=now, verbose_name='Nascimento', editable=True)
    insc = models.DateField(default=now, verbose_name='Data de inscrição', editable=True)
    profession = models.CharField(max_length=150, blank=True, verbose_name='Profissão')
    address = models.CharField(max_length=250, verbose_name='Endereço', null=True, blank=True)
    email = models.EmailField(max_length=200, verbose_name='Email', unique=True)
    tel = models.CharField(max_length=11, unique=True, verbose_name='Telefone')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        """
        Classe para ordenar e contextualizar o admin
        """
        ordering = ('-insc',)
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
