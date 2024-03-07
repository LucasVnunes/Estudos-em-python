"""
Escreva um programa que pergunte o salário de um funcionario e calcule o valor do seu aumento.

para salários superiores a 1.250,00 calcule um auemento de 100 reais
para inferiores ou iguais, o aumento é de 150 reais

"""

salario = float(input("valor do seu salário: "))

if salario > 1250:
    a_j = salario + 1000
    print("seu salário foi de: {}\ncom o aumento ficou: {}".format(salario, a_j))
else:
    if salario <= 1250:
        a_j = salario + 10
        print("seu salário foi de {}\ncom o juros ficou: {}".format(salario, a_j))
print("\033[32mparabens pelo salario! be happy")

#desafio completo!