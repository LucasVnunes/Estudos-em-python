"""
O objetivo é escrever um código que permita ao jogador escolher entre pedra, papel ou tesoura, e depois o programa irá gerar uma escolha aleatória para o computador. Em seguida, o programa determinará quem venceu o jogo e exibirá o resultado.
----------------
import random
computador_escolha = random.randint(1, 3)
"""
import random
jokenpow = str(input("\n\033[32mEscolha entre 1, 2 e 3 para\nOBS:escreva o nome:\n\n\033[31m1:[TESOURA]\n\033[36m2:[PAPEL]\n\033[35m3:[PEDRA]\n\n\033[32mRESPOSTA: ")).upper().strip()
aleatorio = random.randint(1, 3)

if jokenpow == "TESOURA" and aleatorio == 1:
    print("\033[37m1:{} VS {}:TESOURA = EMPATE".format(jokenpow, aleatorio))
else:
    if jokenpow == "TESOURA" and aleatorio == 2:
        print("\033[37m1:{} VS {}:PAPEL = VENCEU!".format(jokenpow, aleatorio))
    else:
        if jokenpow == "TESOURA" and aleatorio == 3:
            print("\033[37m1:{} VS {}:PEDRA = PERDEU!".format(jokenpow, aleatorio))
        else:
            if jokenpow == "PAPEL" and aleatorio == 1:
                print("\033[37m2:{} VS {}:TESOURA = PERDEU".format(jokenpow, aleatorio))
            else:
                if jokenpow == "PAPEL" and aleatorio == 2:
                    print("\033[37m2:{} VS {}:PAPEL = EMPATE".format(jokenpow, aleatorio))
                else:
                    if jokenpow == "PAPEL" and aleatorio == 3:
                        print("\033[37m2:{} VS {}:PEDRA = VENCEU!".format(jokenpow, aleatorio))
                    else:
                        if jokenpow == "PEDRA" and aleatorio == 1:
                            print("\033[37m3:{} VS {}:TESOURA = VENCEU!".format(jokenpow, aleatorio))
                        else:
                            if jokenpow == "PEDRA" and aleatorio == 2:
                                print("\033[37m3:{} VS {}:PAPEL = PERDEU!".format(jokenpow, aleatorio))
                            else:
                                if jokenpow == "PEDRA" and aleatorio == 3:
                                    print("\033[37m3:{} VS {}:PEDRA = EMPATE".format(jokenpow, aleatorio))
                                else:
                                    print("\033[31mESCOLHA INVALIDA!")
print("\033[31mFIM DO JOGO!")