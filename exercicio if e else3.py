#faça um programa que leia três números e mostre qual é o maior e qual é o menor.

numero1 = int(input("digite o primeiro número: "))
numero2 = int(input("digite o segundo número: "))
numero3 = int(input("digite o terceito número: "))

if numero1 > numero2 and numero1 > numero3:
    print("o maior numero é:{}".format(numero1))
if numero2 > numero1 and numero2 > numero3:
    print("o numero maior é:{}".format(numero2))
if numero3 > numero1 and numero3 > numero2:
    print("o numero maior é:{}".format(numero3))

#desafio COMPLETO!