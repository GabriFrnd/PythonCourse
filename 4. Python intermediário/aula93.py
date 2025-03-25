# Introdução aos packages (pacotes) em Python (157)

# O ponto de vista do '__main__' pode te confundir em módulos e pacotes Python (158)
# '__init__.py': arquivo de inicialização dos packages em Python (159)

'''
    Módulo: arquivo com a extensão '.py'
    Package: pasta com módulos Python
'''

'''
import aula93_package.modulo # Pasta + módulo

from aula93_package import modulo # Importando diretamente o módulo
from aula93_package.modulo import somar, falar

print(aula93_package.modulo.somar(10, 10))
print(modulo.somar(10, 10))

print(somar(10, 10))
falar()
'''

import aula93_package

print(aula93_package.somar(10, 10))
print(aula93_package.falar())