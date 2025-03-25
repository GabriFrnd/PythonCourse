# Modularização: entendendo os seus próprios módulos + 'sys.path' no Python (154)

'''
    O primeiro módulo executado pelo Python chama-se '__main__'
    Observações importantes:

        O Python conhece a pasta onde o '__main__' está e as pastas abaixo dele
        Ele não reconhece pastas e módulos acima do '__main__' por padrão
    
    O Python conhece todos os módulos e pacotes presentes nos caminhos de 'sys.path'
'''

import sys

import modulo91 # Importando o módulo por completo
from modulo91 import variavel_modulo # Importando apenas a variável

# print(f'Módulo: {__name__}')
# print(*sys.path, sep='\n')

print(f'Variável do módulo: {modulo91.variavel_modulo}') # print(f'Variável do módulo: {variavel_modulo}')
print(modulo91.somar(10, 10))