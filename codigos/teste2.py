notas = []
i = 0

while i < 15:
    n = -1
    while n < 0 or n > 100:
        n = int(input(f"Nota da semana {i+1}: "))
    notas.append(n)
    i += 1

total = 0
for n in notas:
    total += n

media = total/15

abaixo = 0 
for n in notas:
    if n < media:
        abaixo +=1

menor = notas[0]
maior = notas[0]

for n in notas:
    if n < menor:
        menor = n
    if n > maior:
        maior = n

sequencia = 0
sequenciaMaior = 0

for n in notas:
    if n > 80:
        sequencia += 1
        if sequencia > sequenciaMaior:
            sequenciaMaior = sequencia
    else:
        sequencia = 0

print(f"Total de pontos obtidos no semestre: {total}")
print(f"Média Geral: {media}")
print(f"Semanas abaixo da média: {abaixo}")
print(f"Nota mais baixa: {menor}")
print(f"Nota mais alta: {maior}")           
print(f"Maior sequência consecutiva com notas acima de 80: {sequenciaMaior}")           

#exercicio 37, exercicio 39, questão 1 da revisao para realização do codigo