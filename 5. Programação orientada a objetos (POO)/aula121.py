# Introdução ao método '__init__' (inicializador de atributos) (199)

'''
    O parâmetro 'self' faz referência à instância da classe
    No método '__init__' dentro da classe, o 'self' sempre virá primeiro; após ele, os outros atributos
'''

class Pessoa:
    def __init__(self, nome, sobrenome): # '__init__': utilizado para inicializar os atributos da classe
        self.nome = nome
        self.sobrenome = sobrenome

primeira_pessoa = Pessoa('Gabriel', 'Fernandes Feitosa')

print(f'Nome: {primeira_pessoa.nome}')
print(f'Sobrenome: {primeira_pessoa.sobrenome}')