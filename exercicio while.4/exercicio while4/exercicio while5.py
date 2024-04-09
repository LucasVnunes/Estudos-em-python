"""
Crie um programa que leia vários números inteiros pelo teclado.
no final da execução, mostre a média entre todos os valores e qual foi o maior e o menor lido
o programa deve perguntar se o usuario quer continuar a digitar valores
"""
p = "S"
contador = 0 
soma = 0
maior = 0 
menor = 0
while p == "S":
    n = int(input("Digite um número inteiro: "))
    contador = contador + 1
    soma = soma + n
    p = str(input("você deseja continuar? [S/N]: ")).strip().upper()
    if contador == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
media = soma / contador
print("A media foi de {}".format(media))
print("O número maior foi:{}\nO número menor foi:{}".format(maior, menor))
print("FIM")
