positivos = []
#limitar entradas usando range
for i in range(6):
    numero = float(input())
#bloco de entrada com repetçcao (append armazena os numeros)
    if numero > 0:
        positivos.append(numero)
print(f"{len(positivos)} valores positivos\n{(sum(positivos)/len(positivos)):.1f}")  
#len funcao de lista para retornar os numeros armazenados  