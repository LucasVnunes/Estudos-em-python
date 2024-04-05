#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F" caso esteja errado, peça a digitação novamente até ter um valor carreto 

sexo = str(input("Escreva qual é o seu sexo [M/F]: ")).strip().upper()

while sexo != "M" and sexo != "F":
    print("você digitou uma coisa invalida! tente novamente: ")
    sexo = str(input("Escreva qual é o seu sexo [M/F]: ")).strip().upper()
    
print("FIM")

#desáfio COMPLETO!
