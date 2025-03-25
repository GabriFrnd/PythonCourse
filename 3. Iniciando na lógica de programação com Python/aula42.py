# Introdução ao empacotamento e desempacotamento

nomes = ['Maria', 'Helena', 'Luiz']

primeiro, segundo, terceiro = nomes # Criando variáveis para cada nome (desempacotamento)
# primeiro, segundo, terceiro = ['Maria', 'Helena', 'Luiz']

primeira, *outras_frutas = ['Banana', 'Morango', 'Maçã'] # outras_frutas = ['Morango', 'Maçã']
print(primeira, outras_frutas)