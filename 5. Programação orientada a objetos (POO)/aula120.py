# Classe (class): molde para criar novos objetos (198)

'''
    As classes geram novos objetos (instâncias) que podem ter seus próprios atributos e métodos
    Por convenção, utiliza-se 'PascalCase' para nomes de classes 
'''

class Pessoa:
    ...

primeira_pessoa = Pessoa() # Instância da classe 'Pessoa'

primeira_pessoa.nome = 'Gabriel' # Atributo (característica): nome
primeira_pessoa.sobrenome = 'Fernandes Feitosa' # Atributo (característica): sobrenome

print(f'Nome: {primeira_pessoa.nome}')
print(f'Sobrenome: {primeira_pessoa.sobrenome}')