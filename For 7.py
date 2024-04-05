# peça a idade de 10 pessoas, no final diga quantas pessoas tem mais de 18 e quantas tem menos de 18 anos

soma = 0 
menor = 0

for c in range (1, 11):
    idade = int(input("Digite sua idade: "))
    if idade >= 18:
        soma = soma + 1
    else:
        menor = menor + 1
print("Quantidade de pessoas menores de idade: {}".format(menor))
print("Quantidade de pessoas maiores de idade: {}".format(soma))

#O + 1, vai atribuir como se tivesse contando como 1 pessoa e n juntanto com o input wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwdsaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa