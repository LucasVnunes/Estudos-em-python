"""peça pro usuario escrever um numero, verifique se o numero é par ou impar, se posito ou negativo, print no final: voce escolheu o numero par positivo
                                                                                                                                    numero par negativo
                                                                                                                                    numero impar positivo
                                                                                                                                    numero impar negativo 
                                                                                                                                    tudo numa print só
5 if e 5 else """
numero = int(input("Digite um número: "))


"""
if numero % 2 == 0 and numero >= 0:
    print("o número: {} é par e positivo".format(numero)) 
else:
    if numero % 2 > 0:
        print("o número: {} é impar e positivo".format(numero))
    else:
"""
if numero % 2 == 0:
    print("o numero:{} é par e positivo".format(numero))
if numero % 2 == 1:
        print("o numero:{}, é impar e positivo".format(numero))
else:
    if numero < 0:
                print("seu numero:{}, é par e negativo".format(numero))

#tentar depois

    
