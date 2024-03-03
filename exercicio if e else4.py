#calcule a media das 4 unidades e se for maior que 8 meta um print parabenizando e se for menor que 8 meta print que foi aprovado, se for menor que 6 meta print "RECUPERAÇÂO" e se for menor que 4 meta print "reprovado por media, e peça o nome do meliante

nome_aluno = str(input("Digite seu nome: ")).capitalize()
nota1 = float(input("Sua primeira nota: "))
nota2 = float(input("Sua segunda nota: "))
nota3 = float(input("Sua terceira nota: "))
nota4 = float(input("Sua quarta e ultima nota: "))
media = (nota1 + nota2 + nota3 + nota4) / 4
if media >= 8:
    print("{}, congratilations!".format(nome_aluno))
if media >= 6:
    print("{}, aprovado :/".format(nome_aluno))
if media >= 4:
    print("{}, infelizmente, Recuperação!!!".format(nome_aluno))
if media < 4:
    print("{}, pegue seu banquinho e saia de fininho, reprovado por media".format(nome_aluno))
print("FIM, se passou passou, se n passou n passa mais")

#desafio COMPLETO!





