#Crie um programa que leia o nome completo de uma pessoa e mostre: 
#o nome com todas as letras maiúsculas e minúsculas.
#quantas letras ao todo (sem considerar espaços)
#quantas letras tem o pruimeiro nome

"""
nomeM = str(input("Digite o seu nome completo: "))
M = nomeM.upper()
m = nomeM.lower()
contagem = len(nomeM)
print("Esse é seu nome completo maiúsculo:{}\n" .format(M))
print("Esse é seu nome completo em minúsculo:{}\n".format(m))
print("Essa é a quantidade de caracteres que sue nome completo possui:{}\n".format(contagem))

^^^^ meu primeiro jeito de resolver
dps de ver a resolução vi que tbm poderia ser feito dessa forma:

"""
nome = str(input("Digite seu nome completo: ")).strip()

print("seu nome completo em maiúsculas é:{}".format(nome.upper()))
print("seu nome completo em minúsculas é:{}".format(nome.lower()))
print("seu nome possui o numero total de caracteres de:{}".format(len(nome) - nome.count(" ")))

#Desafio COMPLETO!