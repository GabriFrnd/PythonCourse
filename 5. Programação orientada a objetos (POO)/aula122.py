# Métodos em instâncias de classes Python (200)

class Carro:
    def __init__(self, nome, marca): # O método '__init__' sempre retorna None
        self.nome = nome
        self.marca = marca

    def acelerar_carro(self): # Método da classe 'Carro'
        print(f'{self.marca} {self.nome} está acelerando!')

primeiro_carro = Carro('911', 'Porsche')
outro_carro = Carro('G63', 'Mercedes')

# print(f'Carro: {primeiro_carro.marca} {primeiro_carro.nome}')
primeiro_carro.acelerar_carro() 

# print(f'Carro: {outro_carro.marca} {outro_carro.nome}')
outro_carro.acelerar_carro()