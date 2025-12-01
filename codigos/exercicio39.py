linha = int(input())
operacao = input()
#matriz tambem ~e um vetor
matriz = []
#estrutura de repetiçcao
for i in range(12):
    linhamatriz = []
    for j in range(12):
        linhamatriz.append(float(input()))
    matriz.append(linhamatriz)

resultado = sum(matriz[linha])

if operacao == "M":
    resultado = resultado/12

print(resultado)