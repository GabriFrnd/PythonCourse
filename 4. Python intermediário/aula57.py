# Escopo de funções e módulos em Python + global

'''
Anotações da aula:

    - Escopo: local onde um código pode atingir.
    - Tipos de escopo:

        1. Local: apenas nomes do mesmo local podem ser alcançados;
        2. Global: todo o código é alcançável.

    - Funções com o mesmo nome, declaradas em escopos diferentes, não são iguais.
    - A palavra 'global' faz uma variável do escopo externo ser a mesma do escopo interno.
'''

string = 'Olá, mundo!' # Variável disponível globalmente

def funcao():
    global string # Má prática de programação 
    string = 'Qualquer coisa' # Essa variável virou global

    return string

print(funcao())

def teste():
    outra_string = 'Isso é um teste.' # Disponível para as funções 'teste' e 'outro_teste'

    def outro_teste():
        variavel_teste = 123 # Disponível apenas dentro do escopo da função 'outro_teste'
        return variavel_teste, outra_string
    
    return outro_teste()

print(teste())
print(string) # Varíavel 'string' declarada dentro da função 'funcao'