total = 0
menor = 101
maior = -1
notas = []
acima80_atual = 0
acima80_maior = 0

for semana in range(1, 16):
    nota = -1
    while nota < 0 or nota > 100:
        nota = int(input(f"Digite a nota da semana {semana} (0 a 100): "))
    notas.append(nota)

    total += nota

    if nota < menor:
        menor = nota
    if nota > maior:
        maior = nota

    if nota > 80:
        acima80_atual += 1
        if acima80_atual > acima80_maior:
            acima80_maior = acima80_atual
    else:
        acima80_atual = 0

media = total / 15
abaixo_media = 0

for n in notas:
    if n < media:
        abaixo_media += 1

print("\n--- RESULTADOS ---")
print("Total de pontos:", total)
print("Média geral:", media)
print("Semanas abaixo da média:", abaixo_media)
print("Maior sequência consecutiva > 80:", acima80_maior)
print("Menor nota:", menor)
print("Maior nota:", maior)
