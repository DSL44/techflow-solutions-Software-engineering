# Lista que vai guardar as tarefas
tarefas = []

# Função para adicionar uma tarefa
def adicionar_tarefa(nome):
    tarefas.append(nome)
    return tarefas

# Função para listar as tarefas
def listar_tarefas():
    return tarefas

# Função para remover uma tarefa
def remover_tarefa(nome):
    if nome in tarefas:
        tarefas.remove(nome)
    return tarefas