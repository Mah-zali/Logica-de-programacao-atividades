A, B = map(float,input().split(" "))
#se A é divisivel pelo B ou vice versa
if A%B == 0 or B%A == 0:
    print("São multiplicos")
else: 
    print("Não são multiplos")    