combustivel = 1
alcool = 0
gasoline = 0 
diesel = 0 
#diferente !=
while (combustivel!=4):
    combustivel = int(input())
    #estrutura de condiçcao/ incremendo +=
    if (combustivel==1):
        alcool +=1
    elif (combustivel==2):
        gasoline +=1
    elif (combustivel==3):
        diesel+=1
print(f"MUITO OBRIGADO\nAlcool: {alcool}\nGasolina: {gasoline}\nDiesel: {diesel}")        