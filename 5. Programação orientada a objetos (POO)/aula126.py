# Atributos de classe (204)

class Pessoa:
    ano = 2025 # Atributo de classe (Pessoa.ano ou self.ano)

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def ano_nascimento(self):
        return f'{self.nome} nasceu em {Pessoa.ano - self.idade}.'

primeira_pessoa = Pessoa('Gabriel', 21)
''' Pessoa.ano = 10 # Isso afeta as minhas futuras chamadas '''

print(primeira_pessoa.ano_nascimento())
