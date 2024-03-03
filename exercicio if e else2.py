#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça  para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu
import random
numAleatorio = int(input("Digite um numero: "))
num = random.randint(1, 5)
if numAleatorio != num:
    print("venceu")
else:
    print("perdeu")

#desafio COMPLETO!