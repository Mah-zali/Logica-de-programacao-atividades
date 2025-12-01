#entrada com mapeamento de linha, colocar aspas simples para caractere, um ponto flutuante pode ser inteiro, mas nao o contrario
item, quantidadeitem = map(float, input().split(" "))
#estrutura condicional, relativo a if e else, 2 simbolos de =, relação de numero exato
if (item == 1):
    preco = 4.00*quantidadeitem
elif(item == 2):
    preco = 4.50*quantidadeitem
elif(item == 3):
    preco = 5.00*quantidadeitem
elif (item == 4):
    preco = 2.00*quantidadeitem
elif (item == 5):
    preco = 1.50*quantidadeitem

print(f"Total: R$ {preco:.2f}") 