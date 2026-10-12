from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import Projeto, Tarefa
from .forms import ProjetoForm, TarefaForm


def home(request):
    return render(request, "home.html", {
        'total_projetos': Projeto.objects.count(),
        'total_tarefas': Tarefa.objects.count(),
    })

def projetos(request):
    lista_projetos = Projeto.objects.all().order_by('id')

    return render(request, "projetos.html", {
        'projetos': lista_projetos,
    })

def tarefas(request):
    lista_tarefas = Tarefa.objects.select_related(
        'projeto'
    ).all().order_by('id')

    return render(request, "tarefas.html", {
        'tarefas': lista_tarefas,
    })

def formulario_projeto(request, pk=None):
    projeto = None

    if pk is not None:
        projeto = get_object_or_404(Projeto, pk=pk)

    if request.method == 'POST':
        form = ProjetoForm(
            request.POST,
            instance=projeto
        )

        if form.is_valid():
            form.save()

            if projeto:
                messages.success(
                    request,
                    'Projeto atualizado com sucesso!'
                )
            else:
                messages.success(
                    request,
                    'Projeto cadastrado com sucesso!'
                )

            return redirect('projetos')

    else:
        form = ProjetoForm(instance=projeto)

    return render(request, "formularioprojeto.html", {
        'form': form,
        'projeto': projeto,
    })

def formulario_tarefa(request, pk=None):
    tarefa = None

    if pk is not None:
        tarefa = get_object_or_404(Tarefa, pk=pk)

    if request.method == 'POST':
        form = TarefaForm(
            request.POST,
            instance=tarefa
        )

        if form.is_valid():
            form.save()

            if tarefa:
                messages.success(
                    request,
                    'Tarefa atualizada com sucesso!'
                )
            else:
                messages.success(
                    request,
                    'Tarefa cadastrada com sucesso!'
                )

            return redirect('tarefas')

    else:
        form = TarefaForm(instance=tarefa)

    return render(request, "formulariotarefa.html", {
        'form': form,
        'tarefa': tarefa,
    })

def confirmaexcl(request, tipo, pk):

    if tipo == 'projeto':
        objeto = get_object_or_404(Projeto, pk=pk)
        destino = 'projetos'

    elif tipo == 'tarefa':
        objeto = get_object_or_404(Tarefa, pk=pk)
        destino = 'tarefas'

    else:
        messages.error(
            request,
            'Tipo de registro inválido.'
        )
        return redirect('home')

    if request.method == 'POST':
        objeto.delete()

        if tipo == 'projeto':
            messages.success(
                request,
                'Projeto excluído com sucesso!'
            )
        else:
            messages.success(
                request,
                'Tarefa excluída com sucesso!'
            )

        return redirect(destino)

    return render(request, "confirmaexcl.html", {
        'objeto': objeto,
        'tipo': tipo,
        'destino': destino,
    })
