# Evitando uso de condicionais + Guard Clause (194)

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
    listar_tarefas(lista_tarefas)

def refazer(lista_tarefas, tarefas_refazer):
    print()

    if not lista_tarefas:
        print('Não há nada para refazer.')
        return
    
    tarefa = tarefas_refazer.pop()

    lista_tarefas.append(tarefa)
    listar_tarefas(lista_tarefas)

def adicionar_tarefas(tarefa, lista_tarefas):
    print()

    if not tarefa.strip():
        print('Nada foi digitado.')
        return
    
    lista_tarefas.append(tarefa)
    listar_tarefas(lista_tarefas)

while True:
    print('Comandos: listar, desfazer ou refazer')
    tarefa = input('Digite uma tarefa ou comando: ')

    comandos = {
        'listar': lambda: listar_tarefas(lista_tarefas),
        'desfazer': lambda: desfazer(lista_tarefas, tarefas_refazer),

        'refazer': lambda: refazer(lista_tarefas, tarefas_refazer),
        'adicionar': lambda: adicionar_tarefas(tarefa, lista_tarefas)
    }

    comando = comandos.get(tarefa) if comandos.get(tarefa) is not None else comandos['adicionar']
    comando()

    '''
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
    '''