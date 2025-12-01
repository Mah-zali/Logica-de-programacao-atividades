#localizaçao de vetores
x, y = map(float, input(). split(" "))
if x == 0 and y == 0:
    print("Origem")
elif x == 0:
    print("Eixo Y")
elif y == 0:
    print("Eixo X")       
#calculos dos quadrantes
elif x > 0 and y > 0:
    print("Quadrante 1")
elif x > 0 and y < 0:
    print("Quadrante 4")
elif x < 0 and y > 0:
    print("Quadrante 2")
elif x < 0 and y < 0 :
    print("Quadrante 3")        