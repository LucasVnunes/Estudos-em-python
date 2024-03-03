#Escreva um programa em Python que, dado o código de um produto e a quantidade desejada, calcule o total da compra, aplicando descontos de 10 reais para compras acima de R$ 500 e 15 reais para compras acima de R$ 1000 e pra compras menores que 100 de um almento de 20 reais.  Se o código do produto for inválido, o programa deve imprimir uma mensagem de erro.



preco_produto_1 = 5
preco_produto_2 = 7.50
preco_produto_3 = 2.80
preco_produto_4 = 12.90
#mais indicado nao usar variavel pra isso pra n ocupar espaço na memoria


nome = str(input("Digite seu nome: ")).capitalize()
codigo_produto = int(input("Digite o codigo do produto: "))
quantidade = float(input("Digite a quantidade: "))

if codigo_produto == 1:
    total= quantidade * preco_produto_1 #colocar direto o valor
else:
    if codigo_produto == 2:
        total = quantidade * preco_produto_2
    else:
        if codigo_produto == 3:
            total = quantidade * preco_produto_3
        else:
            if codigo_produto == 4:
                total = quantidade * preco_produto_4
            else:
                print("Erro, produto não encontrado!")

if codigo_produto == 0 and codigo_produto > 4:
    if total >= 500:
        d_j = total - 10
    else:
        if total >= 1000:
            d_j = total - 15
        else:
            if total <= 100:
                d_j = total + 20
    print("{}, O valor da compra foi de:{} depois do ajuste ficou:{}".format(nome, total, d_j))