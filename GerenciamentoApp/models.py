from django.db import models

# Create your models here.
class Agendamento(models.Model):
    local = models.CharField(max_length=200)
    datainicio = models.DateTimeField()
    datafim = models.DateTimeField()

class Pessoa(models.Model):
    nome = models.CharField(max_length=200)
    datadenascimento = models.DateTimeField()
    email = models.CharField(max_length=200)
    telefone = models.CharField(max_length=200)

class PessoaAgendamento(models.Model):
    pessoaid =models.ForeignKey(Agendamento, on_delete=models.CASCADE)
    agendamentoid = models.ForeignKey(Pessoa, on_delete=models.CASCADE)