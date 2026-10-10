from django.db import models

# Create your models here.
class Projeto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    data_inicio = models.DateField()

class Tarefa(models.Model):
    PRIORIDADES = [
        ('B', 'Baixa'),
        ('M', 'Média'),
        ('A', 'Alta'),
    ]
    titulo = models.CharField(max_length=200)
    prioridade = models.CharField(max_length=1, choices=PRIORIDADES)
    concluido = models.BooleanField(default=False)
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, related_name='tarefas')


