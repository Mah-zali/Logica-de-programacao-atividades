N = int(input())
vetor = input()
vetor = vetor.split()
vetor = map(int, vetor)
#list é um vetor, varios numeros em uma linha so
vetor = list(vetor)
#acha o menor valor na entrada
menor = min(vetor)
#localizar a posicao do numero
posicao = vetor.index(menor)

print(f'Menor Valor:', menor)
print(f'Posição:', posicao)