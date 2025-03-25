# Dir, hasattr e getattr em Python

'''
Anotações da aula:

    - 'dir' (debug) lista todos os nomes.
    - 'hasattr' verifica se um objeto tem determinado nome dentro.
'''

string = 'Gabriel'

if hasattr(string, 'upper'): # Verifica se método 'upper()' está dentro de 'string'
    print('Upper existe!')
    print(getattr(string, 'upper')()) # Executa o método 'upper'

print(getattr(string, 'upper'))