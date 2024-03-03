#Estrutura condicional:
"""
if: se
else: se não

Ex:

if carro.esquerda():
    bloco True
else:
    bloco False

== : dois sinais de iguais significa igual normal

"""

tempo = int(input("Diga quantos anos o seu carro tem: "))

if tempo >= 10:
    print("seu carro é antigo")
else:
    print("seu carro é novo")
print("--Fim--")