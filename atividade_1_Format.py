Numero1 = int(input("Digite um numero: "))
Numero2 = int(input("Digite outro numero "))
Soma = Numero1 + Numero2

# print ("a soma entre", Numero1, "e entre", Numero2, "é igual à:", Soma)

"""tbm pode ser feito: 
print ("a soma entre", Numero1)
print ("e entre", Numero2)
print ("é igual à:", Soma)

mas n sairia na mesma linha 
"""
# a melhor forma para ser feita é assim:

print ("a soma entre {} e {} é igual à {}" .format(Numero1, Numero2, Soma))