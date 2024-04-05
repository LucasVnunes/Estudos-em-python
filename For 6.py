# peça 6 numeros para o usuario, os números que forem pares soma e os impares ignora

soma = 0
for c in range (1, 7):
    num = int(input("Digite um numero: "))
    if num % 2 == 0:
        soma = num + soma
print("o resultado da soma entre pares é de: {}".format(soma))

#Desafio COMPLETO!
    