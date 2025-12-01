M, N = map(int, input().split(" "))

while M > 0 and N > 0:
#ordenar os valores da saida
    if N < M:
        aux = N
        N = M
        M = aux
#sequencia numerica (vetor [])
    resultado = []
# variavel para soma
    strresultado = ""
#repetição
    for i in range(M, N + 1, 1):
        resultado.append(i)
#definir armazenamento de numeros
        strresultado += str(i) + " "

    print(f"{strresultado}Sum={sum(resultado)}")

    M, N = map(int, input().split(" "))