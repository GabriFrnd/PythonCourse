# Shallow Copy x Deep Copy em dados mutáveis

import copy # Para shallow copy e deep copy

primeiro_dicionario = {
    'primeira_chave': 'primeiro valor',
    'segunda_chave': 'segundo valor'
}

'''
segundo_dicionario = primeiro_dicionario # 'segundo_dicionario' aponta para o mesmo dicionário que 'primeiro_dicionario'
segundo_dicionario['primeira_chave'] = 'outro valor' # 'primeiro_dicionario' foi afetado

print(primeiro_dicionario)
'''

segundo_dicionario = primeiro_dicionario.copy() # Retorna para 'segundo_dicionario' um novo dicionário (shallow copy)
segundo_dicionario['segunda_chave'] = 'uma coisa' # Um dicionário não afeta o outro

print(primeiro_dicionario)
print(segundo_dicionario)

'''
segundo_dicionario = copy.copy(primeiro_dicionario) # Shallow copy com 'import'
segundo_dicionario = copy.deepcopy(primeiro_dicionario) # Deep copy com 'import'
'''