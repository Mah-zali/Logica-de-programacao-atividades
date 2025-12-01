def criamatriz():
    matriz = [[0 for i in range(12)] for j in range(12)]
    return matriz

def preenchermatriz(matriz):
    for i in range(12):
        for j in range(12):
            
            matriz[i][j] = float(input())
def soma(matriz, coluna):
    total = 0
    for i in range (12):
        total += matriz[i][coluna]
    return total 
def media(matriz, coluna):
    return soma(matriz, coluna) / 12

c = int(input())
t = input()
m = criamatriz()
preenchermatriz(m)

if t == 'S':
    print(f"{soma(m,c):.1f}")
elif t == 'M':
    print(f"{media(m,c):.1f}")    