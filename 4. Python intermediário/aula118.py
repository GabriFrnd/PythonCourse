# Exercício + solução: salvando a lista de tarefas em JSON (195)

import json

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

def salvar_arquivo(lista_tarefas):
    dados_lista = lista_tarefas

    if not lista_tarefas:
        print('A lista está vazia.')
        return
    
    with open('aula118.json', 'w', encoding='utf-8') as arquivo:
        json.dump(dados_lista, arquivo, indent = 4, ensure_ascii = False)

    return dados_lista

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
    salvar_arquivo(lista_tarefas)