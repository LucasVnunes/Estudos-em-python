"""
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
"""

retaA = int(input("Digite quantos cm tem a primeira reta: "))
retaB = int(input("Digite quantos cm tem a segunda reta: "))
retaC = int(input("Digite quantos cm tem a terceira reta: "))

if retaA > retaC and retaB > retaC:
    print("pode ser feito um triângulo pois {} e {} são maiores que {}".format(retaA, retaB, retaC))
else:
    if retaA > retaB and retaC > retaB:
        print("pode ser feito um triângulo pois {} e {} são maiores que {}".format(retaA, retaC, retaB))
    else:
        if retaB > retaA and retaC > retaA:
            print("pode ser feito um triângulo pois {} e {} são maiores que {}".format(retaB, retaC, retaA))
        else:
            print("ERRO, não é possivel formar um triângulo")
#Desafio COMPLETO!
            
