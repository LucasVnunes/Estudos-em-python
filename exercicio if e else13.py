#peça o nome do usuario completo, telefone, idade e endereço, pergunte ao o usurario qual cores abaixo ele prefere que seja imprimido no terminal

nome = str(input("\033[35mDigite seu nome completo: ")).strip().capitalize()
tel = int(input("\033[36mDigite seu numero de telefone: "))
idade = int(input("\033[32mDigite sua idade: "))
endereco = str(input("\033[31mDigite seu endereço: ")).strip().capitalize()
cor = str(input("\n\033[32m[VERDE]\n\033[31m[VERMELHO]\n\033[36m[CIANO]\n\033[37mSua escolha: ")).upper().strip()

if cor == "VERDE":
    print("\033[32mNOME:{}\nTEL:{}\nIDADE:{}\nENDEREÇO:{}".format(nome, tel, idade, endereco))
else:
    if cor == "VERMELHO":
        print("\033[31mNOME:{}\nTEL:{}\nIDADE:{}\nENDEREÇO:{}".format(nome, tel, idade, endereco))
    else:
        if cor == "CIANO":
            print("\033[36mNOME:{}\nTEL:{}\nIDADE:{}\nENDEREÇO:{}".format(nome, tel, idade, endereco))
        else:
            print("ERRO, cor invalida!")
#Desafio COMPLETO!