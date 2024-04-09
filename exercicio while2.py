#crie um jogo que o computador vai "pensar" em um número entre 0 e 10, até o jogador acertar e mostrar no final quantas tentativas foram necessarias 

import random
print("Olá!, eu sou o computador...\nHoje serei seu adversário, será que irá adivinhar que número estou pensando?")
n = int(input("Adivinhe o numero que eu (CPU) estou pensando [1 - 10]: "))
contagem = random.randint(0, 10)
erros = 0
while n != contagem:
    erros = erros + 1
    print("você errou, tente novamente: ")
    n = int(input("Adivinhe o numero que eu (CPU) estou pensando [1 - 10]: "))
print("Parabéns!\nO número de tentativas foi de {} tentativas".format(erros))

#desáfio COMPLETO!