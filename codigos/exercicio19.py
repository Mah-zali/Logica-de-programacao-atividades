#media ponderada com peso
nota1, nota2, nota3, nota4 = map(float, input().split(" "))
#variavel separada, / para divisao
media = (nota1*2 + nota2*3 + nota3*4 + nota4*1)/(2+3+4+1)
print(f"Média: {media:.1f}")
#verificar se aluno foi aprovado com estrutura condicional usando if 
if media >= 7.0: 
    print("Aluno Aprovado.")

elif media >= 5:
    print("Aluno em exame.")    
#nota exame, ao ter outra entrada no meio do processo, metodo da casa decimal .format (usado para premissa continuar)
nota5 = 6.4
print("Nota do exame: {:.1f}".format(nota5))
media = (media+nota5)/2

#saida nota final
print("Aluno Aprovado.")
print(f"Média Final: {media:.1f}")