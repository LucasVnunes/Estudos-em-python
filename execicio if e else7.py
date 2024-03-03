"""
Problema "lanchonete" (adaptado de URI 1038)

Uma lanchonete possui vários produtos. Cada produto possui um código
e um preço. Você deve fazer um programa para ler o código e a
quantidade comprada de um produto (suponha um código válido), e daí
informar qual o valor a ser pago, com duas casas decimais, conforme
tabela de produtos ao lado.

Código do produto | Preço do produto
1 | R$ 5.00
2 | R$ 3.50
3 | R$ 4.80
4 | R$ 8.90
5 | R$ 7.32
"""
codigo_produto = int(input("Digite o codigo do produto:"))
quantidade = float(input("quantidade que deseja comprar: "))

if codigo_produto == 1:
    total1 = quantidade * 5
    print("o total da sua compra foi de:{}".format(total1))
else:
    if codigo_produto == 2:
        total2 = quantidade * 3.50
        print("o total da sua compra foi de:{}".format(total2))
    else:
        if codigo_produto == 3:
            total3 = quantidade * 4.80
            print("o total da sua compra foi de:{}".format(total3))
        else:
            if codigo_produto == 4:
                total4 = quantidade * 8.90
                print("o total da sua compra foi de:{}".format(total4))
            else:
                if codigo_produto == 5:
                    total5 = quantidade * 7.32
                    print("o total da sua compra foi de:{}".format(total5))

# ELSE = se o condenado do usuario não quiser o produto 1 que está no primeiro if (ELSE) então vai pro segundo if como se fosse o primeiro if