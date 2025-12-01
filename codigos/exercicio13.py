valor = int(input())
#questao de vetores
notas = [100,50,20,10,5,2,1]

print(valor)
#trabalhar estrutura condicional
for nota in notas:
    quantidade = valor//nota
    valor = valor%nota
    print(f'{quantidade} notas(s) de R$ {nota}')
