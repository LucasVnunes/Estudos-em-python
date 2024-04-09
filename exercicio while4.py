"""
Crie um programa que leia vários números inteiros pelo teclado.
no final da execução, mostre a média entre todos os valores e qual foi o maior e o menor lido
o programa deve perguntar se o usuario quer continuar a digitar valores
"""

n = 0
d = "S"
contador = 0
soma = 0
maior = menor = 0
while d == "S":
    contador = contador + 1
    n = int(input("Digite um número: "))
    soma = soma + n
    d = str(input("Quer continuar: [S/N]: ")).upper()
    if contador == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n 

media = soma / contador
print("A média foi:{}".format(media))
print("O maior foi {} e o menor é: {}".format(maior, menor))