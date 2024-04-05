#peça o nome e a idade de um usuario, se a idade for menor que 18 diga que ele é de menor caso for maior de um ola (nome do usuario)

nome = str(input("Digite o seu nome completo: ")).capitalize()
idade = int(input("Digite sua idade: "))
cidadania = str(input("Tem cidadania BR? |S/N|: ")).upper()

if idade >= 18:
    print("Parábens, você de nome:{}".format(nome))
    if cidadania == "S":
        print("{}, você é de maior e disse {}, então é brasileiro. Pode passar".format(nome, cidadania))
    else:
        print("não pode entrar,não é cidadão")
else:
    print("Caro {} ,você não pode entrar, pois tem menos de 18 anos".format(nome))
