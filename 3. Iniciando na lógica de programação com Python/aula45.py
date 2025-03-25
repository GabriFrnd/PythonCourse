# Exercício: crie uma lista de compras com listas

import os
lista_compras = []

while True:
    print('Selecione uma opção')
    opcao = input('Inserir, apagar ou listar: ')

    if opcao == 'inserir':
        os.system('cls')

        item = input('Digite um item para inserir na lista: ')
        lista_compras.append(item)

    elif opcao == 'apagar':
        
        if len(lista_compras) >= 1:
            indice = input('Digite o índice para excluir: ')

            try:
                indice_inteiro = int(indice)
                del lista_compras[indice_inteiro]
            except:
                print('Não foi possível apagar esse item.')
                continue
        else:
            print('Nada para apagar.')
            continue

    elif opcao == 'listar':
        os.system('cls')

        if len(lista_compras) >= 1:
            for index, valor in enumerate(lista_compras):
                print(index, valor)
        else:
            print('Nada para listar.')
            continue

    else:
        print('Digite uma opção válida.')
        continue