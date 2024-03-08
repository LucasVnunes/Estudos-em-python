# Faça um algoritmo que leia três notas de um aluno, calcule e escreva a média final deste aluno. Se a média for maior que 7, o aluno é aprovado, senão aprovado, menor que 4 reprovado!
nota1 = float(input("Digite a sua primeira nota: "))
nota2 = float(input("Digite a sua segunda nota: "))
nota3 = float(input("Digite a sua terceira nota: "))

media = ((nota1 + nota2 + nota3) / 3)

if media >= 7:
    print("sua média é de {:.2f}, voce passou com nota alta".format(media))
else:
    if media >= 4:
        print("voce foi aprovado, sua media foi de {:.2f}".format(media))
    else:
        if media < 4:
            print("você infelizmente foi reprovado, sua media foi de:{:.2f}".format(media))
questionario = str(input("sua media foi boa? S/N: ")).upper()

if questionario == "S":
    print("Congratilations, até a proxima média")
else:
    print("Que pena, talvez na proxima vez que você for pensar em gazear aula, você também pense nas suas notas!")
print("\033[35mFIM!")
#Desafio COMPLETE!!
