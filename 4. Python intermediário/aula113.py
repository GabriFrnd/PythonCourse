# 'os.remove', 'os.unlink' e 'os.rename': apagando, renomeando e movendo arquivos (189)

'''
    'os.remove' ('os.unlink'): apaga o arquivo
    'os.rename': troca o nome ou move o arquivo
'''

import os

caminho_arquivo = 'aula113.txt'

with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
    arquivo.write('Início do meu novo arquivo\n')
    arquivo.write('Linha 1\n')

    arquivo.writelines(
        ('Linha 2\n', 'Linha 3')
    )

# os.remove(caminho_arquivo)
# os.unlink(caminho_arquivo)
# os.rename(caminho_arquivo, 'nova-aula113.txt')