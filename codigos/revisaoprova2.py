soma = 0
positivos = 0
negativos = 0
maior = 0
contador_pos = 0

while soma <= 1000:
    valor = int(input("Digite a produção da hora: "))

    if valor == 0:
        continue

    if valor < 0:
        negativos += 1
        continue

    # valor positivo
    positivos += 1
    soma += valor
    contador_pos += 1

    if valor > maior:
        maior = valor

media = soma / contador_pos

print("Total de valores positivos:", positivos)
print("Total de valores negativos:", negativos)
print("Maior valor positivo informado:", maior)
print("Média dos valores positivos:", media)
print("Soma final:", soma)
