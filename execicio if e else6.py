#Escreva um código Python que solicite a idade, o nome e se a pessoa tem RG. Com base nesses dados, o programa deve imprimir uma mensagem indicando se a pessoa pode fazer faculdade ou não. Se a pessoa tiver menos de 16 anos, ela é muito jovem para fazer faculdade. Se ela tiver entre 16 e 18 anos e tiver RG ela pode fazer faculdade. Se ela tiver 18 anos ou mais, ela pode fazer faculdade. mesmo sem RG

idade = int(input("Digite sua idade: "))
nome = str(input("Digite seu nome: ")).capitalize()
rg = str(input("você possui RG? S/N: ")).upper()

# 3 if e 3 else

if idade >= 18:
    print("o corno {}, pode entrar na faculdade, pois é maior de idade e n precisa de RG".format(nome))
else:
    if idade < 16:
            print("seu cabaço, vai aprender a chupar chupeta, que tu não tem idade pra fazer faculdade, senhor {}".format(nome))
    else:
        if idade >= 16 and rg == "S":
            print("o senhor corno:{}, poderá entrar nesta porra, pois possui 16 ou mais e possui o caralho do RG!".format(nome))
        else: 
            print("seu baitola viado manso, você não possui o k7 do RG!, caro {}".format(nome))    






# A PORRA DO ELSE VAI PRO IF MAIS PROXIMO QUE ENCONTRAR NESSA POHA