# Entendendo 'self' em classes Python (201)

'''
    A classe é o molde, mas geralmente não possui dados
    A instância da classe, por outro lado, possui dados
'''

class Carro: 
    def __init__(self, nome, marca): # O nome 'self' é convenção; pode-se colocar qualquer nome não reservado
        self.nome = nome
        self.marca = marca

    # Dentro da classe, o 'self' é a própria instância

    def acelerar_carro(self): 
        print(f'{self.marca} {self.nome} está acelerando!')

primeiro_carro = Carro('911', 'Porsche')
outro_carro = Carro('G63', 'Mercedes')

primeiro_carro.acelerar_carro() # Carro.acelerar_carro(primeiro_carro)
outro_carro.acelerar_carro() # Carro.acelerar_carro(outro_carro)