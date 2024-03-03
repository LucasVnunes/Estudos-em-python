"""
Operações

+ Adição
- subtração
* multiplicação
/ Divisão
** potência 
// Divisão inteira
% resto da divisão

Ordem de precedência 

1 ()
2 **
3 *, /, //, %
4 + , -

"""
# para calcular uma raiz quadrada ou raiz cubica é utilizado o numero por 1/2 
# EX: 25**(1/2) Quadrada / 24**(1/3) Cubica

numero1 = int(input("Digite um número: "))
numero2 = int(input("digite um novo número: "))
soma = numero1 + numero2
multiplicação = numero1 * numero2
subtração = numero1 - numero2
resto_divisão = numero1 % numero2
print(">>> esse é o resultado da soma {} \n" .format(soma), end=">>>")
print (" Esse é o resultado de todas as operações: soma {} , multiplicação {} , subtração {}, o resto da divisão {}" .format(soma, multiplicação, subtração, resto_divisão))

# .format(####), end="" esse END serve para n quebrar linha 
# \n quebra linha 