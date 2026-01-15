import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.app import adicionar_tarefa, listar_tarefas, remover_tarefa

def test_adicionar_tarefa():
    resultado = adicionar_tarefa("Estudar GitHub")
    assert "Estudar GitHub" in resultado

def test_remover_tarefa():
    adicionar_tarefa("Testar")
    resultado = remover_tarefa("Testar")
    assert "Testar" not in resultado