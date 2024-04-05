# Faça um for que peça 10 numeros a o usuario

"""
num = int(input("Digite um numero: "))
print(num)
num = int(input("Digite um numero: "))
print(num)
num = 2
print(num)

ex:

soma = 0 
num = (escolhido pelo usuario) 10
soma = 0 + com o num = 10 = 10
soma = 10 + com o proximo numero escolhido pelo usuario = 20 = soma = 30
.... loop até a quantidade de vezes escolhidas no for


"""

soma = 0 
for c in range (1, 11):
    num = int(input("Digite um numero: "))
    soma = num + soma 
print(soma)

#Desafio COMPLETO!