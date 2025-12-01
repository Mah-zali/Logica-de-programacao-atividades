soma = 0
positivos = 0
negativos = 0
maior = 0
numeroPositivos = 0

while soma <= 1000:
    valor = int(input("Insira o número da produção por hora: "))

    if valor == 0:
        continue
    if valor < 0:
        negativos += 1
        continue

    positivos +=1
    soma += valor
    numeroPositivos += 1

    if valor > maior:
        maior = valor

media = soma/numeroPositivos

print(f"Total de valores positivos: {positivos}")
print(f"Total de valores negativos: {negativos}")
print(f"Maior valor de produção por hora: {maior}")
print(f"Média dos valores positivos usados na soma: {media}")
print(f"Soma final: {soma}")


#exercicio 28, exercicio 34, exercicio 39 para elementos do código 