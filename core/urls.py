
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('projetos/', views.projetos, name='projetos'),
    path('tarefas/', views.tarefas, name='tarefas'),

    # Cadastro
    path(
        'formulario/projeto/',
        views.formulario_projeto,
        name='formulario_projeto'
    ),
    path(
        'formulario/tarefa/',
        views.formulario_tarefa,
        name='formulario_tarefa'
    ),

    # Edição
    path(
        'projetos/<int:pk>/editar/',
        views.formulario_projeto,
        name='editar_projeto'
    ),
    path(
        'tarefas/<int:pk>/editar/',
        views.formulario_tarefa,
        name='editar_tarefa'
    ),

    # Exclusão
    path(
        'excluir/<str:tipo>/<int:pk>/',
        views.confirmaexcl,
        name='confirma'
    ),
]
