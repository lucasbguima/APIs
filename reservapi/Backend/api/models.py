from django.db import models
from django.contrib.auth.models import AbstractUser

from datetime import datetime
import random

# Create your models here.

class User(AbstractUser):
    endereco = models.CharField(max_length=200, null=True)
    rg = models.IntegerField(null=True)
    cpf = models.IntegerField(null=True)
    telefone = models.IntegerField(null=True)

    pass

class Hotel(models.Model):

    nome = models.CharField(max_length=200)

    ESTADOS = ( ('AC','Acre'), ('AL','Alagoas'), ('AP','Amapá'), ('AM','Amazonas'), ('BA','Bahia'), ('CE','Ceará'), ('DF','Distrito Federal'), ('ES','Espírito Santo'), ('GO','Goiás'), ('MA','Maranhão'), ('MT','Mato Grosso'), ('MS','Mato Grosso do Sul'), ('MG','Minas Gerais'), ('PA','Pará'), ('PB','Paraíba'), ('PR','Paraná'), ('PE','Pernambuco'), ('PI','Piauí'), ('RJ','Rio de Janeiro'), ('RN','Rio Grande do Norte'), ('RS','Rio Grande do Sul'), ('RO','Rondônia'), ('RR','Roraima'), ('SC','Santa Catarina'), ('SP','São Paulo'), ('SE','Sergipe'), ('TO','Tocantins'), )

    localidade = models.CharField(max_length=2, choices=ESTADOS, blank=False, null=False)

    email = models.CharField(max_length=200)

    pass

    def __str__(self):
        return str(self.nome) + (" - ") + (str(self.localidade))

class Agendamento(models.Model):

    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    SITUACAO = (
        ("Confirmado", "Confirmado"),
        ("Cancelado", "Cancelado"),
        ("Finalizado", "Finalizado")
    )
    status = models.CharField(max_length=10, choices=SITUACAO, blank=False, null=False)
    data_inicio = models.DateField(null=False)
    data_termino = models.DateField(null=False)
    
    pass

    def __str__(self):

        return str(self.id) + (' - ') + str(self.cliente) + (' - ') + str(self.hotel) + (' - ') + str(self.status)
