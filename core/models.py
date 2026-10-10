from django.db import models

# Create your models here.

class Projeto(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    data_inicio = models.DateField()

class Tarefa(models.Model):

    PRIORIDADES = [
        ('BAIXA', 'baixa'),
        ('MEDIA', 'media'),
        ('ALTA', 'alta'),
    ]

    titulo = models.CharField(max_length=150)
    prioridade = models.CharField(max_length=100)
    choices =PRIORIDADES

    projeto = models.ForeignKey(
        Projeto,
        on_delete=models.CASCADE,
        related_name="tarefas"
    )

    def __str__(self):
        return self.titulo