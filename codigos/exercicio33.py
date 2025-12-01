# estrutura de repeti~cao de while colocar := pra se tornar variavel
while (nota1 := float(input())) < 0 or nota1 > 10: print("Nota Inválida")
while (nota2 := float(input())) < 0 or nota2 > 10: print("Nota Inválida")

print(f"media = {(nota1+nota2)/2.0}")