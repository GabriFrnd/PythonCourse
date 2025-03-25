# Criando arquivos com Python + Context Manager with (186)
# 'with open' (context manager) e métodos úteis do TextIOWrapper (187)
# Modos de abertura de arquivo e encoding com 'with open' (188)

'''
    Utiliza-se a função 'open' p/ abrir um arquivo (ele pode existir ou não)
    Modos: leitura (r), escrita (w), p/ criação (x), escrever ao final (a), binário (b), modo texto (t) e leitura/escrita (+)

        O modo 'w' apaga tudo do arquivo e escreve de novo
        O modo 'a' não apaga nada do arquivo, mas começa a escrever na última linha

    Context manager: with (abre e fecha automaticamente)
    Ao abrir um arquivo com 'open', deve-se fechar com 'close' de imediato p/ evitar problemas
'''

caminho_arquivo = 'aula112.txt'

'''
arquivo = open(caminho_arquivo, 'w') # Cria o arquivo 'aula112.txt' 
arquivo.close() # Fechou o arquivo
'''

'''
with open(caminho_arquivo, 'w+') as arquivo: 
    arquivo.write('Meu novo arquivo\n')
    arquivo.write('Meu novo arquivo\n')

    arquivo.writelines(
        ('Qualquer coisa\n', 'Bom dia!')
    )

    arquivo.seek(0, 0) # Move o cursor do arquivo para o topo
    print(arquivo.read())

    print()

    print('Lendo arquivo ...\n')
    arquivo.seek(0, 0)

    print(arquivo.readline(), end='') # Lê o arquivo linha por linha
    print(arquivo.readline(), end='')

    print(arquivo.readline(), end='')
    print(arquivo.readline())

    print()

    print('Lendo arquivo c/ readlines:')

    arquivo.seek(0, 0)
    print()

    for linha in arquivo.readlines():
        print(linha, end='')

print()
'''

'''
with open(caminho_arquivo, 'r') as arquivo: 
    print(arquivo.read())
'''

with open(caminho_arquivo, 'w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')

    arquivo.writelines(
        ('Linha 3\n', 'Linha 4\n')
    )

with open(caminho_arquivo, 'a') as arquivo:
    arquivo.write('Linha 5\n')
    arquivo.write('Linha 6\n')

with open(caminho_arquivo, 'a', encoding='utf-8') as arquivo:
    arquivo.write('Uso de UTF-8\n')
    arquivo.write('Olá, mundo! (sem erro de acentuação)')