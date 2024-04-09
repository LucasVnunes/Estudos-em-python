
#crie um programa que leia dois valores e mostre opção de somar, multiplicar, maior, novos números e sair do programa
print("\033[0;32mSEJA BEM VINDO(A), ME CHAMO BIT E HOJE ESTAREI LHE GUIANDO\033[0;0m")
from time import sleep
n1 = int(input("Escolha o primeiro número: "))
n2 = int(input("Escolha o segundo número: "))
op = 0

soma = n1 + n2
multi = n1 * n2

while op != 5:
    sleep(0.50)
    op = int(input("\n\033[1;34m\n\n[1]SOMAR\n\n[2]MULTIPLICAR\n\n[3]MAIOR\n\n[4]NOVOS NÚMEROS\n\n[5]SAIR DO PROGRAMA\033[0;0m\n\nEscolha qual opção você quer:"))
    if op == 5:
        print(">>> FIM <<<")
    elif op == 1:
        sleep(1)
        print("\n{} + {} = {}".format(n1, n2, soma))
    elif op == 2:
        sleep(1)
        print("{} x {} = {}".format(n1, n2, multi))
    elif op == 3:
        if n1 > n2:
            print("\nO maior número entre n1 e n2 é:{}".format(n1))
        else:
            print("\nO maior número entre n1 e n2 é:{}".format(n2))
    elif op == 4:
        print("\n[Escolha novos números]")
        n1 = int(input("Escolha o primeiro número: "))
        n2 = int(input("Escolha o segundo número: "))
        soma = n1 + n2
        multi = n1 * n2
        