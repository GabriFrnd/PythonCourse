# Interpolação de string com % em Python

'''
String: s
Inteiro: d ou i

Float: f
Hexadecimal: x ou X
'''

nome = 'Gabriel'
preco = 150.542
variavel = '%s, o preço foi de R$ %.3f' % (nome, preco)

print(variavel)
print('%s, o preço foi de R$ %.3f' % (nome, preco))
print('O hexadecimal de %i é %x' % (100, 100))