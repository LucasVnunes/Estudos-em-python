largura_terreno = float(input('Digite a largura do terreno: '))
comprimento_terreno = float(input('Digite o comprimento do terreno: '))
valor_metro = float(input('Digite o valor do metro: '))
Area_terreno = largura_terreno * comprimento_terreno
preco_terreno = Area_terreno * valor_metro
print ('A area do terreno é de {}, e o preço do terreno é de {}' .format(Area_terreno, preco_terreno))