#crie um programa que leia dois valores e mostre opção de somar, multiplicar, maior, novos números e sair do programa
print("\033[0;32mSEJA BEM VINDO(A), ME CHAMO BIT E HOJE ESTAREI LHE GUIANDO\033[0;0m")
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
op = int(input("\n\033[1;34m\n\n[1]SOMAR\n\n[2]MULTIPLICAR\n\n[3]MAIOR\n\n[4]NOVOS NÚMEROS\n\n[5]SAIR DO PROGRAMA\033[0;0m\n\nEscolha qual opção você quer:"))

soma = n1 + n2
multi = n1 * n2

#poderia fazer o if em formato de escada mas para exercitar minha lógica vou fazer sem
"""
if op == 1:
    print("{} + {} = {}".format(n1, n2, soma))
else:
    if op == 2:
        print("{} x {} = {}".format(n1, n2, multi)) 
"""

while op == 4:
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
        op = int(input("\n\033[1;34m\n\n[1]SOMAR\n\n[2]MULTIPLICAR\n\n[3]MAIOR\n\n[4]NOVOS NÚMEROS\n\n[5]SAIR DO PROGRAMA\033[0;0m\n\nEscolha qual opção você quer:"))
if op == 1:
    print("\033[1;31m{} + {} = {}".format(n1, n2, soma))
if op == 2:
    print("\033[1;31m{} x {} = {}".format(n1, n2, multi))
if op == 5:
    print("\033[1;31mFIM DO PROGRAMA\033[0;0m")
if op == 3:
     if n1 > n2:
        print("\033[1;31mO maior número é {}\033[0;0m".format(n1))
     if n2 > n1:
        print("\033[1;31mO maior número é {}\033[0;0m".format(n2))
     if n1 == n2:
        print("\033[1;31mOs dois números são iguais.\033[0;0m")
print("\033[0;33mObrigado por participar\033[0;0m")

#Desáfio COMPLETO! porem usei pouco while irei refazer ele no proximo exercicio com mais while 