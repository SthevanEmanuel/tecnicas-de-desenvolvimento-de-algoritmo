import json
import os

ARQUIVO = "tarefas.json"


def carregar_tarefas():
    """
    Carrega as tarefas do arquivo JSON.
    Se o arquivo não existir, cria um novo automaticamente.
    """
    if not os.path.exists(ARQUIVO):
        with open(ARQUIVO, "w") as f:
            json.dump([], f)

    with open(ARQUIVO, "r") as f:
        return json.load(f)


def salvar_tarefas(tarefas):
    """
    Salva a lista de tarefas no arquivo JSON.
    """
    with open(ARQUIVO, "w") as f:
        json.dump(tarefas, f, indent=4)


def adicionar_tarefa(descricao):
    """
    Adiciona uma nova tarefa ao sistema.
    :param descricao: Texto da tarefa a ser adicionada.
    """
    tarefas = carregar_tarefas()
    tarefas.append({"descricao": descricao, "concluida": False})
    salvar_tarefas(tarefas)
    print("✔ Tarefa adicionada com sucesso!")


def listar_tarefas():
    """
    Exibe todas as tarefas cadastradas no sistema.
    """
    tarefas = carregar_tarefas()

    if not tarefas:
        print("\nNenhuma tarefa cadastrada.\n")
        return

    print("\n===== LISTA DE TAREFAS =====")
    for i, tarefa in enumerate(tarefas):
        status = "✔ Concluída" if tarefa["concluida"] else "⏳ Pendente"
        print(f"{i + 1}. {tarefa['descricao']} — {status}")
    print()


def concluir_tarefa(indice):
    """
    Marca uma tarefa como concluída.
    :param indice: Número da tarefa na lista.
    """
    tarefas = carregar_tarefas()
    try:
        tarefas[indice]["concluida"] = True
        salvar_tarefas(tarefas)
        print("✔ Tarefa concluída!")
    except IndexError:
        print("❌ Índice inválido.")


def remover_tarefa(indice):
    """
    Remove uma tarefa da lista.
    :param indice: Número da tarefa na lista.
    """
    tarefas = carregar_tarefas()
    try:
        tarefas.pop(indice)
        salvar_tarefas(tarefas)
        print("✔ Tarefa removida com sucesso!")
    except IndexError:
        print("❌ Índice inválido.")


def menu():
    """
    Interface principal do sistema de tarefas.
    """
    while True:
        print("===== SISTEMA DE TAREFAS =====")
        print("1 - Listar tarefas")
        print("2 - Adicionar tarefa")
        print("3 - Concluir tarefa")
        print("4 - Remover tarefa")
        print("0 - Sair")
        opc = input("Escolha uma opção: ")

        if opc == "1":
            listar_tarefas()

        elif opc == "2":
            descricao = input("Descrição da tarefa: ")
            adicionar_tarefa(descricao)

        elif opc == "3":
            listar_tarefas()
            indice = int(input("Número da tarefa: ")) - 1
            concluir_tarefa(indice)

        elif opc == "4":
            listar_tarefas()
            indice = int(input("Número da tarefa: ")) - 1
            remover_tarefa(indice)

        elif opc == "0":
            print("Saindo...")
            break

        else:
            print("❌ Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
