# Escopo da classe e de métodos da classe (202)

class Animal:
    def __init__(self, nome):
        self.nome = nome
        variavel = 'Valor da variável' # Apenas no escopo do método '__init__'

        print(variavel)
        print()

    def comer(self, comida):
        ''' print(variavel) # Erro: variável não definida '''

        return f'{self.nome} está comendo {comida}!'

leao = Animal('Leão')

print(f'Animal: {leao.nome}')
print(leao.comer('carne'))
