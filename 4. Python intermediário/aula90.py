# Módulos: import, from, as e '*' (153)

'''
    Documentação: https://docs.python.org/3/py-modindex.html
    Formas de importação:

        Módulo inteiro: import + 'nome_módulo'
        Módulo por partes: from + 'nome_módulo' + import + 'primeiro, segundo'

        Primeiro alias: import + 'nome_módulo' + as + 'apelido'
        Segundo alias: from + 'nome_módulo' + import + 'primeiro' + as + 'apelido'

    Má prática de importação: from + 'nome_módulo' + import + '*'
'''

import sys # Módulo inteiro

print(sys.platform) # Kernel do sistema operacional
''' sys.exit() # Sai do programa '''

from sys import platform, exit # Módulo por partes

print(platform)
# exit()

import sys as s # Primeiro alias

print(s.platform)
# s.exit()

from sys import platform as pt, exit as ex # Segundo alias

print(pt)
ex()