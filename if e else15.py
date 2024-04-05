nome = str(input("Digite seu nome: ")).capitalize()
idade = int(input("Digite sua idade: "))
musica = str(input("Gosta de m83 ou cigarrets after sex?: ")).lower()

if musica == "m83":
    print("recomendo Midnight city")
else:
    if musica == "cigarrets after sex":
        print("recomendo Cry")
    else:
        print("essa musica não está na lista")