#dica colocar um if dentro do outro

#crie um programa que peça idade e se é cidadão brasileiro, se for maior de idade e brasileiro pode, se for menor de idade e for brasileiro não pode, e se for maior idade e não brasuca n pode, e for menor de idade e n brasilieto n pode.
# 2 if e 2 else

idade = int(input("Digite a sua idade para votar: "))
pergunta = str(input("voce brasileiro? SIM/NÂO: ")).upper()

if idade >= 18:
    if pergunta == "SIM":
        print("você pode votar!")
    else:
      print("não pode votar, estrangeiro")
else:
   print("não pode votar, jovem dms")

#Desafio completo