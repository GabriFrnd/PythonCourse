# Exercício: lista de tarefas com opções de desfazer e refazer (192)

lista_tarefas = []
tarefas_refazer = []

def listar_tarefas(lista_tarefas):
    print()

    if not lista_tarefas:
        print('Não há nada para listar.')
        return

    print('Tarefas: ')

    for tarefa in lista_tarefas:
        print(f'\t{tarefa}')

def desfazer(lista_tarefas, tarefas_refazer):
    print()

    if not lista_tarefas:
        print('Não há nada para desfazer.')
        return
    
    tarefa = lista_tarefas.pop()
    tarefas_refazer.append(tarefa)

def refazer(lista_tarefas, tarefas_refazer):
    print()

    if not lista_tarefas:
        print('Não há nada para refazer.')
        return
    
    tarefa = tarefas_refazer.pop()
    lista_tarefas.append(tarefa)

def adicionar_tarefas(tarefa, lista_tarefas):
    print()

    if not tarefa.strip():
        print('Nada foi digitado.')
        return
    
    lista_tarefas.append(tarefa)

while True:
    print('Comandos: listar, desfazer ou refazer')
    tarefa = input('Digite uma tarefa ou comando: ')

    if tarefa.lower() == 'listar':
        listar_tarefas(lista_tarefas)
        continue

    elif tarefa.lower() == 'desfazer':
        desfazer(lista_tarefas, tarefas_refazer)
        continue

    elif tarefa.lower() == 'refazer':
        refazer(lista_tarefas, tarefas_refazer)
        continue

    else:
        adicionar_tarefas(tarefa, lista_tarefas)
        continue