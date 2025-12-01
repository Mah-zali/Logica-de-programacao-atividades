valores = list(map(int, input().split(" ")))
#estrutura ilicita, cada item separado
#lista nao ordenada: nao numerada; lista ordenada: numerada
auxNumeros = list(valores)
#variavel list, e puxa os valores
valores.sort()
#estrutura de repetiçao
for v in valores:
    print(v)
#nao esquecer o print vazio para pular linha
print()

for v in auxNumeros:
    print(v)