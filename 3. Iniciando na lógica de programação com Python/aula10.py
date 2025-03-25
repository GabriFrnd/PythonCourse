# Introdução às f-strings (formatação de strings)

nome = 'Gabriel'
altura = 1.70

peso = 60
imc = peso / (altura ** 2)

# print(nome, 'tem', altura, 'de altura, pesa', peso, 'kg e seu IMC é', imc)
print(f'{nome} tem {altura:.2f} de altura, pesa {peso} kg e seu IMC é {imc:.2f}')