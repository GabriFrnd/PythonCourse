# Cuidados com tipos de dados mutáveis (list e copy)

'''
    = copia o valor (imutáveis)
    = aponta para o mesmo valor na memória (mutável)
'''

primeira = ['Gabriel', 123]
segunda = primeira.copy() # Realizando uma cópia da primeira lista, não mais apontando para o valor na memória

primeira[0] = 'Qualquer coisa'

print(primeira)
print(segunda) # A segunda lista não foi alterada devido ao método 'copy'